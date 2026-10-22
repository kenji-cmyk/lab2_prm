# Đối chiếu yêu cầu PRM323 Lab 2

Ngày rà soát: **22/10/2026**. **Kết luận: chưa đủ yêu cầu để xác nhận hoàn tất Lab.** Việc sắp xếp và push repository chỉ hoàn thiện hồ sơ hiện có.

Nguồn: [hai đề PDF và hướng dẫn DOCX nguyên bản](requirements/README.md), đặc biệt mục 5–8 trang 3–8 và rubric trang 9–11 của đề tiếng Anh. Đã đọc văn bản cả hai PDF và hai DOCX; các file nguồn được giữ nguyên. Đối chiếu toàn bộ Markdown, manifest/PNG, [snapshot audit](../design/figma-audit.json) và [metadata Figma đọc trực tiếp](reviews/figma-metadata-2026-10-22.json). Đã xem tổng quan 13 ảnh UI/overlay/responsive; ảnh không chứng minh tương tác chạy được.

## Bảng yêu cầu

| Yêu cầu | Kết quả và bằng chứng | Còn phải làm |
| --- | --- | --- |
| Chủ đề được duyệt, hình thức nhóm được cho phép (tr. 1–2) | Hồ sơ ghi Nhóm 6; chưa có xác nhận giảng viên trong repo. | Xác nhận đề tài và hình thức nhóm theo thông báo lớp. |
| Persona, vấn đề, chỉ số đo được (tr. 4) | [Persona](../ux/persona.md) có bối cảnh, goals, pain points, nhu cầu tiếp cận và mục tiêu thời gian; là persona giả định. | Kiểm thử các chỉ số sau này; đề không bắt buộc nghiên cứu thực địa. |
| Ít nhất 8 màn khác nhau (tr. 2) | Có 8 màn chức năng S01–S04, S06, S08, S10–S11, tất cả 360 × 800 trong metadata và PNG. | Không tính S05/S07/S09 hoặc dialog vào số màn chức năng. |
| IA, 3 flow có start/goal/end/alternative, một nhánh lỗi (tr. 4) | [User flow](../ux/user-flow.md) có inventory, Mermaid và mapping. Snapshot có đường chính, retry và overlay. | S09 chưa có đường vào từ launch chính; hoàn thiện điều hướng và kiểm thử thực tế. |
| DESIGN.md trước prompt đầu tiên (tr. 3, 7) | [Brief](../design/DESIGN.md) có palette/type/spacing/tone/rules; Stitch chưa chạy. | Dùng brief khi chạy thật, lưu lịch sử đúng thời gian. |
| UI ban đầu từ Stitch, prompt nguyên văn và screenshot (tr. 3–4) | **Chưa đạt**: [log](../ai/ai-design-log.md) chỉ có prompt chuẩn bị; assets/stitch chỉ có README. | Chạy Stitch và lưu output thật; công cụ tương đương cần giảng viên chấp thuận theo đề tr. 3. |
| 3 vòng lặp giải quyết 3 vấn đề, ảnh trước/sau (tr. 4) | **Chưa đạt**: ba vòng đều được ghi là dự kiến. | Lưu prompt/output/ảnh trước–sau của mỗi vòng thực tế. |
| Critique theo Nielsen/accessibility/persona, ≥5 phát hiện và toàn bộ response (tr. 4) | **Chưa đạt**: chưa có prompt đã chạy và toàn bộ response tương ứng. Review căn chỉnh không thay thế chuỗi bằng chứng này. | Chạy critique trên ảnh thật, lưu nguyên văn prompt và toàn bộ trả lời. |
| Quyết định accept/modify/reject có lý do (tr. 4) | Có 10 design decisions, chưa truy vết từng khuyến nghị AI tới prompt/response/ảnh. | Ghi quyết định của nhóm và dẫn tới thay đổi Figma. |
| Đúng 6 trang Figma, đúng thứ tự (tr. 5) | **Đạt kiểm kê trực tiếp**: 01 User Flow, 02 Wireframe, 03 Final UI, 04 Design System, 05 Components, 06 Prototype. | Trang 01 cần xác minh mỗi flow liên kết tới các màn dùng trong flow. |
| Wireframe cho mọi màn (tr. 5) | Có coverage nhưng trang 02 hiện có **22 frame**: bộ `12:*` và bộ hồi cứu `52:*` đặt chồng. Snapshot cũ chỉ lưu 11 frame `52:*`. | Chọn một bộ làm bản chính, sắp xếp rõ; không coi bộ hồi cứu là bằng chứng trước AI generation. |
| Color/type/spacing/radius/elevation tokens dùng trong components (tr. 5–6) | Snapshot có 24 variables, 7 Text Styles, 1 Effect Style, 164 bound nodes/174 bound paints. Có light theme. | Kiểm tra từng component; số bindings không chứng minh đã loại toàn bộ hardcode. |
| 9 nhóm component với Auto Layout và đủ states (tr. 5–6) | Có đủ 9 nhóm; **chưa đủ states**, xem bảng dưới. | Bổ sung states, instances và kiểm tra Auto Layout từng variant. |
| 3 flow clickable và flow starting point (tr. 6) | Snapshot có 3 launch card, 32 reactions, 31 đích hợp lệ. Launch card chưa chứng minh native flow starting point. | Kiểm tra starting point trong Figma và chạy đủ 3 flow bằng Present. |
| Back đúng, overlay, loading → result, không dead end (tr. 6) | Snapshot nối overlay hủy và timer 1.300 ms. Một số control hiển thị nhưng chưa có reaction. | Nối control thiếu; kiểm tra Back theo đường vào, overlay và retry trực tiếp. |
| Accessibility và responsive 360/412 (tr. 6) | Có checklist, contrast token, ghi nhận sửa hit area 48 dp; có ảnh Home 412. **Chưa đủ bằng chứng toàn bộ UI.** | Đo control/text/contrast thực tế; rà mọi màn ở 360/412, ý nghĩa không chỉ bằng màu. |
| Handoff 6 mục/màn, 2 bảng mapping, hành vi ≥600 dp (tr. 7–8) | Có 6 đề mục cho 11 frame + overlay và hai bảng trong [handoff](../handoff/flutter-handoff.md), có mô tả ≥600 dp. | Cần spacing/scroll/max length cụ thể hơn theo màn; chuẩn hóa variant và từng Text Style. Chưa có bằng chứng bạn cùng lớp dựng một màn chỉ từ handoff. |
| README, PNG xuất, AI disclosure (tr. 7–8) | Có bản đồ tài liệu, Figma link, khai báo công cụ và **14 PNG** kèm manifest. | Bằng chứng AI vẫn thiếu như trên. |
| Repository `prm323-lab2-<student-id>` (tr. 7) | **Chưa đúng tên mẫu**: remote là `kenji-cmyk/lab2_prm`. Hồ sơ chưa có mã SV để đặt tên. | Đặt tên theo mã SV/quy ước nhóm được cho phép; giữ remote hiện có khi chưa có thông tin đó. |
| Link Figma mở khi chưa đăng nhập (tr. 11–12) | **Chưa xác minh**. MCP dùng tài khoản kết nối; Browser lượt này lỗi khởi tạo, lượt trước ghi HTTP 403. | Mở cửa sổ riêng tư, kiểm tra quyền Anyone with the link can view và demo. |
| Lịch sử công việc (bản EN tr. 12) | Trước lần sắp xếp này local Git chỉ có commit `e8fc3a8`. Chỉ tiêu `[N]` commits/ngày trong đề chưa điền. | Giữ lịch sử thật; giảng viên xác định bản áp dụng/chỉ tiêu. |

## Component states phải bổ sung hoặc xác minh

Đối chiếu bảng gốc tr. 5–6 với variants đọc trực tiếp ở trang 05 Components. Không coi Focused là Pressed.

| Component | Đề gốc yêu cầu | Hiện có / thiếu |
| --- | --- | --- |
| Button | Default, Pressed, Disabled, Loading | Có Default/Focused/Loading/Disabled; **thiếu Pressed**. |
| Text Field | Default, Focused, Filled, Error, Disabled | Có Default/Focused/Error; **thiếu Filled và Disabled**. |
| Card | Default, Pressed nếu tappable | Có Default/Selected; cần Pressed khi bổ sung tương tác chọn goal card. |
| Navigation | Mỗi destination có selected | Navigation Item có Selected/Unselected; Navigation Icons có Home/Journal/Progress/Learn × Selected/Unselected. Cần kiểm tra instances và reactions. |
| App Bar | Default, with actions | Có Root/Back; cần chứng minh actions sử dụng được. |
| Dialog | Confirmation và destructive/error variant | Có Open/Confirmed; overlay có “Hủy bữa ăn”. **Chưa có variant destructive/error phân biệt rõ** trong component set; cần bổ sung hoặc chứng minh mapping. |
| Loading | Pattern mức màn, spinner/skeleton | Có S05/Processing và Complete; cần kiểm tra loading indicator, không chỉ icon tĩnh và timer. |
| Empty | Icon/illustration, message, một action | S09 có đủ hình/nội dung/CTA; hiện mở thủ công. |
| Error | Message, cause dễ hiểu, retry | S07 có thông báo/nguyên nhân/Retry; cần chạy phục hồi trong Present. |

Đã sửa tên inventory chính trong handoff theo metadata. Các mô tả như Button/Primary hoặc Card/Tip ở từng màn là vai trò thiết kế, chưa phải tên variant được xác minh.

## Những tương tác cần ưu tiên

1. S02: goal card tĩnh nhưng CTA ghi “Lưu mục tiêu”; cần có lựa chọn và phản hồi rõ.
2. S03: link “Xem tiến trình tuần” hiển thị nhưng snapshot không có reaction; tab Progress đã nối, dễ khiến Minh chọn control không hoạt động.
3. S08/S09/S10: chỉ tab Home có reaction; S11 chưa có bottom-nav reaction. Cần nối các destination hiển thị.
4. S09: thêm lối vào để demo empty state trong flow hoặc native starting point riêng cho state này.
5. S11: Back cố định về S10 cả khi mở từ tab Học trên S03; kiểm tra hành vi theo ngữ cảnh.
6. S07: câu “được giữ lại trên thiết bị” là nội dung prototype; chưa có bằng chứng draft được giữ khi lỗi. Lab không yêu cầu backend nhưng dữ liệu mẫu chưa chứng minh hành vi đã kiểm thử.

## Checklist trước khi nộp

- [ ] Chạy Stitch, lưu output ban đầu và ba vòng lặp thật, ảnh trước/sau, full prompt/response.
- [ ] Lưu critique ≥5 phát hiện, quyết định accept/modify/reject và truy vết tới Figma.
- [ ] Bổ sung states thiếu, dọn wireframe chồng, hoàn thiện reactions/starting points.
- [ ] Chạy 3 flow trong Present, nhánh lỗi, overlay, loading/result và Back.
- [ ] Hoàn tất accessibility cho UI thực tế ở 360/412; ≥600 chỉ cần mô tả trong handoff theo đề.
- [ ] Chuẩn hóa handoff với tên token/style/variant và thông số mỗi màn; thử bàn giao một màn cho bạn cùng lớp.
- [ ] Xác minh quyền xem công khai, tên repo theo mã SV/quy ước nhóm, duyệt đề tài và cho phép làm nhóm.

Không ước lượng điểm tổng khi kiểm tra thực tế và bằng chứng AI còn thiếu. Các mục tạo UI bằng AI (10), lặp/critique (15) và phần AI log (3) đang bị ảnh hưởng trực tiếp; tiêu chí sản phẩm tùy mức hoàn thiện.

## Việc đã hoàn thiện trong repository

- Giữ `ux`, `design`, `ai`, `assets`, `handoff` ở gốc theo đề.
- Gom 2 PDF + 2 DOCX và tóm tắt vào `docs/requirements/`; review vào `docs/reviews/`.
- Chuyển HTML cũ vào `archive/prototype-html/`, giữ nội dung lịch sử.
- Sửa README ảnh Figma, link hỏng tới MIGRATION_STATUS và các tài liệu chuyển chỗ.
- Bổ sung validator Python dùng thư viện chuẩn. Kiểm tra file không thay thế xác nhận đạt yêu cầu giáo viên.

## Kết quả kiểm tra hồ sơ sau sắp xếp

`python tools/validate_lab2.py` đã chạy thành công: đủ cấu trúc, 71 đường dẫn Markdown nội bộ tồn tại, 14 PNG khớp manifest về kích thước/byte/SHA-256/CRC, snapshot có 32 reactions và đủ đường chính của 3 flow cùng nhánh retry/overlay/timer. Đã thử dữ liệu lỗi trong thư mục tạm: link không tồn tại, PNG bị sửa byte và cạnh prototype bị xóa đều bị validator từ chối. Script không kiểm tra anchor Markdown, external links hay chạy Figma Present.
