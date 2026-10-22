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
    'docs/reviews/current-fix-review.md', 'docs/reviews/browser-check.md',
    'docs/reviews/accessibility-audit.json', 'tools/figma/README.md',
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
    image_root = ROOT / 'assets/figma'
    actual = {path.relative_to(image_root).as_posix() for path in image_root.rglob('*.png')}
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
    wireframes = audit['pages'][1]['frames']
    check(len(wireframes) == 11, 'Expected one set of eleven wireframes')
    for i, first in enumerate(wireframes):
        for second in wireframes[i + 1:]:
            overlap = (first['x'] < second['x'] + second['width']
                       and second['x'] < first['x'] + first['width']
                       and first['y'] < second['y'] + second['height']
                       and second['y'] < first['y'] + first['height'])
            check(not overlap, f"Overlapping wireframes: {first['id']}, {second['id']}")
    starts = audit.get('flowStartingPoints', [])
    check({s['nodeId'] for s in starts} == {'13:373', '13:378', '13:383'},
          'Expected three native flow starting points')
    required_states = {
        'Button': {'Default', 'Pressed', 'Disabled', 'Loading'},
        'Text Field': {'Default', 'Focused', 'Filled', 'Error', 'Disabled'},
        'Card': {'Default', 'Selected', 'Pressed'},
        'Dialog': {'Open', 'Confirmed', 'Destructive'},
    }
    for name, required in required_states.items():
        component = next(c for c in audit['components'] if c['name'] == name)
        states = {v['name'].removeprefix('State=') for v in component['variants']}
        check(required <= states, f'Missing component states in {name}: {required - states}')
        check(all(v.get('layoutMode') in {'HORIZONTAL', 'VERTICAL'}
                  for v in component['variants']), f'No Auto Layout in {name}')
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
              and abs(r['trigger']['timeout'] - 1.3) < 0.01
              and r['action'].get('destinationId') == '13:485' for r in reactions),
          'Loading timer differs from the configuration verified in Present')
    print(f'PASS snapshot: 6 pages, 11 wireframes, required states/Auto Layout, 3 native starts,')
    print(f'     {len(reactions)} reactions, 3 main paths and retry/overlay/timer')
    print('NOTE snapshot validation is static; it does not test Figma Present or public access.')


def check_accessibility():
    reports = read_json('docs/reviews/accessibility-audit.json')
    audit = read_json('design/figma-audit.json')
    check({r['page'] for r in reports} == {'03 Final UI', '06 Prototype'},
          'Missing accessibility page report')
    check(len(reports) == 2, 'Duplicate accessibility page report')
    for report in reports:
        page = next(p for p in audit['pages'] if p['name'] == report['page'])
        expected = {f['id']: (f['width'], f['height']) for f in page['frames']
                    if f['width'] in {360, 412}}
        screens = report['screens']
        check(len(screens) == len({s['id'] for s in screens}),
              f"Duplicate accessibility screen: {report['page']}")
        actual = {s['id']: (s['width'], s['height']) for s in screens}
        check(actual == expected, f"Incomplete accessibility coverage: {report['page']}")
        for screen in report['screens']:
            check(not screen['failures'], f"Accessibility failures: {screen['id']}")
            check(screen['minFontSize'] >= 14, f"Small text: {screen['id']}")
            check(screen['minTextContrast'] >= 4.5, f"Low text contrast: {screen['id']}")
            check(screen['fontFamilies'] == ['Roboto'], f"Unexpected font: {screen['id']}")
            check(all(b['contrast'] >= 3 for b in screen['controlBorders']),
                  f"Low control contrast: {screen['id']}")
            check(all(t['width'] >= 48 and t['height'] >= 48 for t in screen['clickTargets']),
                  f"Small touch target: {screen['id']}")
    proto = next(r for r in reports if r['page'] == '06 Prototype')
    check(sum(s['width'] == 412 for s in proto['screens']) == 11,
          'Expected 412dp evidence for all eleven screens')
    final = next(r for r in reports if r['page'] == '03 Final UI')
    print(f"PASS accessibility evidence: {len(final['screens'])} Final UI and "
          f"{len(proto['screens'])} Prototype/responsive frames,")
    print('     text >=14, contrast >=4.5, measured borders >=3 and click targets >=48')


def print_open_items():
    print('QA evidence: docs/reviews/browser-check.md records actual Present/anonymous checks.')
    print('OPEN: access to all six design pages/Share settings, lecturer approval')
    print('     of Codex + Figma MCP substitution, repository naming/group approval, classmate handoff.')
    print('See docs/submission-review.md. Repository PASS does not mean rubric complete.')


def main():
    try:
        check_structure()
        check_links()
        check_images()
        check_snapshot()
        check_accessibility()
        print_open_items()
    except (ValueError, KeyError, OSError, StopIteration, struct.error) as error:
        print(f'FAIL: {error}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
