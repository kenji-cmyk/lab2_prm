"""Validate repository evidence, not completion of the teacher's rubric.

Python 3 standard library only. Run from any working directory.
"""

import hashlib
import json
import re
import struct
import sys
import zlib
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {'.git', '.tool-cache', '.playwright-mcp', '__pycache__', 'node_modules'}
PAGES = ['01 User Flow', '02 Wireframe', '03 Final UI',
         '04 Design System', '05 Components', '06 Prototype']
REQUIRED = [
    'README.md', 'ux/persona.md', 'ux/user-flow.md', 'design/DESIGN.md',
    'design/screen-spec.md', 'design/design-decisions.md', 'ai/ai-design-log.md',
    'handoff/flutter-handoff.md', 'assets/stitch/README.md',
    'assets/figma/README.md', 'assets/figma/manifest.json', 'design/figma-audit.json',
    'docs/submission-review.md', 'docs/requirements/README.md',
    'docs/requirements/summary.md', 'docs/reviews/figma-metadata-2026-10-22.json',
    'archive/prototype-html/README.md', 'presentation/demo-script.md',
]


def check(condition, message):
    if not condition:
        raise ValueError(message)


def read_json(relative):
    return json.loads((ROOT / relative).read_text(encoding='utf-8-sig'))


def check_structure():
    for relative in REQUIRED:
        check((ROOT / relative).is_file(), f'Missing file: {relative}')
    source = ROOT / 'docs/requirements'
    check(len(list(source.glob('*.pdf'))) == 2, 'Expected two original PDF files')
    check(len(list(source.glob('*.docx'))) == 2, 'Expected two original DOCX files')
    print('PASS structure: required deliverables, 2 PDFs and 2 DOCX files')


def check_links():
    count = 0
    broken = []
    pattern = re.compile(r'!?\[[^\]\n]*\]\((<[^>\n]+>|[^\s)]+)(?:\s+"[^"]*")?\)')
    for path in ROOT.rglob('*.md'):
        if EXCLUDED.intersection(path.relative_to(ROOT).parts):
            continue
        # Ignore examples inside fenced code blocks.
        content = re.sub(r'(?ms)^(`{3,}|~{3,}).*?^\1[^\n]*$', '',
                         path.read_text(encoding='utf-8-sig'))
        for match in pattern.finditer(content):
            link = match.group(1).strip('<>')
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            count += 1
            target = (path.parent / unquote(parsed.path)).resolve()
            if not target.is_relative_to(ROOT) or not target.exists():
                broken.append(f'{path.relative_to(ROOT)} -> {link}')
    check(not broken, 'Broken internal paths:\n' + '\n'.join(broken))
    print(f'PASS Markdown: {count} internal paths exist (anchors/external access not tested)')


def png_size(data):
    check(data[:8] == b'\x89PNG\r\n\x1a\n', 'Invalid PNG signature')
    offset, size, ended = 8, None, False
    while offset < len(data):
        check(offset + 12 <= len(data), 'Truncated PNG chunk')
        length = struct.unpack_from('>I', data, offset)[0]
        kind = data[offset + 4:offset + 8]
        end = offset + 8 + length
        check(end + 4 <= len(data), 'Truncated PNG data')
        crc = struct.unpack_from('>I', data, end)[0]
        check(zlib.crc32(data[offset + 4:end]) & 0xffffffff == crc,
              f'PNG CRC mismatch in {kind!r}')
        if offset == 8:
            check(kind == b'IHDR' and length == 13, 'Invalid PNG header')
            size = struct.unpack_from('>II', data, offset + 8)
        offset = end + 4
        if kind == b'IEND':
            check(length == 0 and offset == len(data), 'Invalid PNG end')
            ended = True
            break
    check(ended and size is not None, 'PNG has no end/header')
    return size


def check_images():
    manifest = read_json('assets/figma/manifest.json')
    entries = manifest['entries']
    names = [entry['file'] for entry in entries]
    check(len(names) == len(set(names)), 'Duplicate PNG manifest entry')
    actual = {path.name for path in (ROOT / 'assets/figma').glob('*.png')}
    check(set(names) == actual, 'PNG files and manifest differ')
    for entry in entries:
        data = (ROOT / 'assets/figma' / entry['file']).read_bytes()
        check(len(data) == entry['bytes'], f"Size mismatch: {entry['file']}")
        check(hashlib.sha256(data).hexdigest() == entry['sha256'],
              f"SHA-256 mismatch: {entry['file']}")
        check(png_size(data) == (entry['width'], entry['height']),
              f"Dimension mismatch: {entry['file']}")
        if entry['role'] in {'functional', 'state', 'overlay'}:
            check((entry['width'], entry['height']) == (360, 800),
                  f"Expected 360 x 800: {entry['file']}")
    check(sum(e['role'] == 'functional' for e in entries) >= 8,
          'Fewer than eight functional screen exports')
    print(f'PASS PNG: {len(entries)} files, byte sizes, SHA-256, dimensions and chunk CRCs')


def check_snapshot():
    audit = read_json('design/figma-audit.json')
    manifest = read_json('assets/figma/manifest.json')
    check(audit['fileKey'] == manifest['fileKey'], 'Figma file keys differ')
    check([p['name'] for p in audit['pages']] == PAGES, 'Wrong Figma pages/order')
    ids = {frame['id'] for p in audit['pages'] for frame in p['frames']}
    check(all(e['nodeId'] in ids or e['nodeId'] in {p['id'] for p in audit['pages']}
              for e in manifest['entries']), 'Export node missing from snapshot')
    reactions = audit['reactions']
    check(len(reactions) == audit['reactionCount'], 'Reaction count mismatch')
    graph = set()
    destinations = []
    for reaction in reactions:
        action = reaction['action']
        dest = action.get('destinationId')
        if dest:
            destinations.append(dest)
            check(dest in ids, f'Missing prototype destination: {dest}')
            graph.add((reaction['sourceScreen']['id'], dest))
        if reaction['trigger']['type'] == 'ON_CLICK':
            check(reaction['width'] >= 48 and reaction['height'] >= 48,
                  f"Undersized click target: {reaction['sourceNodeId']}")
    check(len(destinations) == audit['destinationCount'], 'Destination count mismatch')
    paths = [
        ['13:418', '13:434', '13:447'],
        ['13:447', '13:465', '13:476', '13:485', '13:507'],
        ['13:447', '13:534', '13:563', '13:534'],
        ['13:465', '13:497', '13:476'],
        ['13:465', '13:579', '13:447'],
    ]
    for path in paths:
        check(all(edge in graph for edge in zip(path, path[1:])),
              f'Broken snapshot path: {path}')
    check(any(r['action'].get('navigation') == 'OVERLAY' for r in reactions),
          'No overlay action in snapshot')
    check(any(r['action']['type'] == 'CLOSE' for r in reactions),
          'No close-overlay action in snapshot')
    check(any(r['sourceScreen']['id'] == '13:476'
              and r['trigger']['type'] == 'AFTER_TIMEOUT'
              and r['action'].get('destinationId') == '13:485' for r in reactions),
          'No loading-to-result timeout in snapshot')
    print(f'PASS snapshot: 6 pages, {len(reactions)} reactions, 3 main paths, retry/overlay/timer')
    print('NOTE snapshot validation is static; it does not test Figma Present or public access.')


def print_open_items():
    metadata = read_json('docs/reviews/figma-metadata-2026-10-22.json')
    wireframes = metadata['pages'][0]['frames']
    print(f'OPEN latest metadata: {len(wireframes)} wireframes; overlapping sets need review.')
    audit = read_json('design/figma-audit.json')
    requirements = {'Button': {'Default', 'Pressed', 'Disabled', 'Loading'},
                    'Text Field': {'Default', 'Focused', 'Filled', 'Error', 'Disabled'}}
    for name, required in requirements.items():
        component = next(c for c in audit['components'] if c['name'] == name)
        states = {v['name'].removeprefix('State=') for v in component['variants']}
        missing = sorted(required - states)
        if missing:
            print(f"OPEN component {name}: missing {', '.join(missing)} in snapshot.")
    print('OPEN submission: Stitch output, 3 iterations, full AI critique/decisions,')
    print('     component states, prototype wiring/starting points, accessibility,')
    print('     public Figma access, handoff details and teacher-approved repository name.')
    print('See docs/submission-review.md. Repository PASS does not mean rubric complete.')


def main():
    try:
        check_structure()
        check_links()
        check_images()
        check_snapshot()
        print_open_items()
    except (ValueError, KeyError, OSError, StopIteration, struct.error) as error:
        print(f'FAIL: {error}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
