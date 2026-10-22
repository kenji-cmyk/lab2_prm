# Đối chiếu yêu cầu PRM323 Lab 2

Cập nhật **22/10/2026 sau sửa Figma**. Hai nhóm vấn đề states/prototype/wireframe và accessibility/Present đã được sửa và kiểm tra. Present mở công khai khi không đăng nhập; quyền mở editor/design công khai vẫn cần xác minh bên ngoài môi trường CloudFront 403.

Nguồn: [đề gốc](requirements/README.md), [review sau sửa](reviews/current-fix-review.md), [audit Figma](../design/figma-audit.json), [QA trực tiếp](reviews/browser-check.md) và [accessibility](reviews/accessibility-audit.json).

| Yêu cầu | Trạng thái hiện tại |
| --- | --- |
| Chủ đề/persona/vấn đề/chỉ số | Có persona giả định Minh, bối cảnh, pain points, mục tiêu đo được và IA; xem [persona](../ux/persona.md), [flow](../ux/user-flow.md). Duyệt đề tài/hình thức nhóm theo thông báo lớp. |
| ≥8 màn chức năng | Có 8 màn S01–S04/S06/S08/S10/S11, 360 × 800; S05/S07/S09 là trạng thái, overlay không tính riêng. |
| 3 flow, nhánh thay thế/lỗi và mapping | Có sơ đồ và mapping; cả ba flow, retry, empty, overlay và Back đã được chạy trong Present. |
| 6 trang Figma đúng thứ tự | Đạt kiểm kê: User Flow, Wireframe, Final UI, Design System, Components, Prototype. |
| Wireframe đủ màn, rõ ràng | Còn đúng 11 frame bộ 52:*; xóa bộ trùng 12:*, grid không chồng. Đây là wireframe dựng hồi cứu, không chứng minh thứ tự trước generation. |
| Design tokens/theme sáng | Có 25 variables (thêm border control), 7 Text Styles, 1 Effect Style; bindings ghi trong audit. Không coi số bindings là chứng nhận đã loại mọi hardcode. |
| 9 nhóm component và states | Đủ inventory và states đã bổ sung: Button Pressed, Text Field Filled/Disabled, Card Pressed, Dialog Destructive. Có Auto Layout và instances review. |
| Starting points và prototype | Có 3 native starting point, 95 reactions, 92 destinations, không đích thiếu. 15 inactive bottom tabs, goal choices, Home link, empty entry và Back theo ngữ cảnh đã chạy được. |
| Loading → result, overlay | Đã sửa timer theo hành vi runtime; auto transition, retry, Continue/Cancel overlay và nút Xem kết quả đều có bằng chứng trong QA. |
| Contrast/type/touch | Đo trên 12 Final UI và 25 Prototype/responsive frames: text ≥14 px, min contrast 5,52:1, field borders khoảng 6,47:1; click targets ≥48 × 48 dp, không text vượt màn trong audit. |
| Không chỉ dùng màu | Goal/nav selected có ✓; Goal có chữ Đã chọn; chart có text ngày đã/chưa ghi và viền rõ. |
| Responsive 360/412, mô tả ≥600 | Có 11 bản 412 đối chiếu đủ S01–S11 và 11 bản chuẩn 360; ≥600 mô tả trong handoff, không cần vẽ theo đề. |
| Handoff 6 mục/màn và 2 mapping | [Handoff](../handoff/flutter-handoff.md) đủ 6 mục cho 11 frame + overlay, token→Flutter/component→widget; chưa có bằng chứng bạn cùng lớp dựng một màn chỉ từ handoff. |
| AI workflow | Theo lựa chọn người thực hiện bài: Codex đọc đề/UX/brief, thiết kế và sửa bằng Figma MCP; [AI log](../ai/ai-design-log.md) giữ prompt thực tế, phát hiện/quyết định và bằng chứng. Không dùng Stitch, không tạo lịch sử ba vòng giả. |
| Chấp thuận công cụ thay thế | Đề gốc yêu cầu Stitch/3 vòng có bằng chứng, hoặc công cụ tương đương được giảng viên duyệt. User đã chọn Codex + Figma MCP; repo chưa có xác nhận giảng viên, nên chưa tự đánh dấu đạt toàn bộ rubric AI lịch sử. |
| Truy cập công khai | Present đã xác minh context sạch HTTP 200/render thực/không đăng nhập. Editor/design bị CloudFront 403 trong môi trường, chưa tới màn xin quyền: còn cần xác minh người chấm xem đủ sáu trang. |
| Repository và PNG | Cấu trúc gốc đúng các thư mục yêu cầu, có 25 PNG/manifest và map tài liệu. Đề trang 7 yêu cầu tên prm323-lab2-<student-id>; remote hiện là lab2_prm, cần mã SV/quy ước nhóm được cho phép nếu đổi tên. |
| Git history | Giữ lịch sử thật. Chỉ tiêu [N] commits/ngày trong bản EN chưa điền; không tạo lịch sử giả để lấp thiếu sót. |

## Kết quả kỹ thuật đã xác minh

- Ba native flows, ba lựa chọn mục tiêu, 15 inactive bottom-tab destinations, Back theo nguồn vào, error/retry, empty state và overlay đã chạy trực tiếp bằng keyboard trong Present.
- Kiểm tra file gồm cấu trúc, đường dẫn nội bộ, 25 PNG/SHA-256/CRC, component states, wireframe không chồng, native starting points, graph reactions và audit accessibility.
- Công khai đã xác nhận cho Present. Không suy ra quyền editor hoặc hỗ trợ TalkBack/VoiceOver trên thiết bị từ kết quả đó.
- Dữ liệu mẫu và chuyển màn không chứng minh backend, nhập dữ liệu thật hay persistence.

## Việc còn phụ thuộc xác nhận ngoài phiên

- [ ] Mở link design bằng cửa sổ riêng tư ngoài môi trường này, kiểm tra người chấm thấy đủ sáu trang.
- [ ] Xác nhận giảng viên chấp thuận Codex + Figma MCP thay Stitch và cách đánh giá phần iteration/log.
- [ ] Xác nhận duyệt đề tài/hình thức nhóm và tên repo theo mã SV/quy ước lớp.
- [ ] Thử bàn giao một màn cho bạn cùng lớp theo yêu cầu handoff.

Không ước lượng điểm tổng hoặc tự xác nhận đạt trọn rubric khi các xác nhận trên chưa có.
