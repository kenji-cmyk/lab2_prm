# Kết quả sửa Figma và kiểm tra trực tiếp

Ngày: **22/10/2026**. File: [Nếp Lành](https://www.figma.com/design/Cc2O3xSmxgjfvDI2hrsY3Q). Quy trình thực tế: **đọc đề/UX/brief → Codex phân tích → Figma MCP chỉnh thiết kế → kiểm tra → sửa theo kết quả Present → cập nhật handoff**. Không dùng Stitch hoặc dựng lịch sử ba vòng lặp giả.

## Kết quả thay đổi

| Hạng mục | Thay đổi đã thực hiện | Bằng chứng |
| --- | --- | --- |
| Component states | Thêm Button Pressed `61:78`, Text Field Filled `61:80` và Disabled `61:85`, Card Pressed `61:90`, Dialog Destructive `61:93`. Giữ Auto Layout và bindings từ component gốc. | [Ảnh instances của các states](../../assets/figma/15-component-states.png), [audit](../../design/figma-audit.json). |
| Wireframe | Xóa chính xác 11 duplicate frame `12:*`; giữ 11 frame `52:*`, grid ba cột không chồng. Có note nguồn hồi cứu. | [Ảnh wireframe mới](../../assets/figma/14-wireframe-overview.png), [script](../../tools/figma/fix-wireframes.js). |
| Chọn mục tiêu | Ba lựa chọn chuyển giữa S02 `13:434`, `63:267`, `63:291`; lựa chọn hiện ✓ và “Đã chọn”. Save tới Home. | [QA trực tiếp](browser-check.md). Đây là lựa chọn trình diễn; chưa có persistence hoặc Home tùy biến theo goal. |
| Điều hướng | Nối 15 inactive bottom-tab destinations; Home secondary link mở Weekly; Journal có lối vào ngày trống; Article Back về nguồn gọi. | [QA trực tiếp](browser-check.md), 95 reactions/92 destinations trong audit. |
| Starting points | Đặt ba native flow starting point ở launch `13:373`, `13:378`, `13:383`. | Sidebar Flows và walkthrough được xác nhận trong QA. |
| Loading → result | Sửa timer từ giá trị MCP `1300` không chạy trong Present thành `1.3`, xác nhận tự tới S06. Thêm “Xem kết quả” 320 × 48 dp làm đường tiếp tục chủ động. Indicator có vòng spinner 40 dp và nhãn. | QA đo khoảng 2,072 giây từ thao tác Analyze tới article S06, gồm điều hướng/render; retry cũng qua loading/result. |
| Offline và empty | Gỡ câu khẳng định draft đã được giữ trên thiết bị; có retry/quay lại biểu mẫu. S08 → “Xem ngày chưa ghi bữa” → S09 → S04. | QA chạy được lỗi/retry, empty và overlay; fixture không chứng minh dữ liệu nhập thật được lưu. |
| Thứ tự đọc | Sắp foreground layers của màn/launch/overlay để Figma đọc từ trên xuống; giữ thứ tự Auto Layout trong component. | QA xác nhận sau reload với “Adapt content for screen readers”. |
| Không chỉ bằng màu | Goal/tab được chọn có ✓, Goal có chữ “Đã chọn”; biểu đồ có text ngày đã/chưa ghi và viền tương phản. | [Ảnh Weekly](../../assets/figma/10-tien-trinh-tuan.png), QA quan sát. |
| Responsive | Có 11 frame 412 × 800 trên trang Prototype, đối chiếu đủ S01–S11 với bản 360 × 800. | [Manifest 25 PNG](../../assets/figma/manifest.json), [ảnh 412](../../assets/figma/README.md). |

## Accessibility đã kiểm tra

[Audit đo thực tế](accessibility-audit.json) bao gồm **12 frame Final UI, 148 text layers hiển thị** và **25 frame Prototype/responsive, 316 text layers hiển thị**:

- Font nội dung/nhãn hiển thị tối thiểu **14 px** trong Figma, dùng Roboto.
- Tương phản chữ thấp nhất **5,52:1**, đạt ngưỡng 4,5:1 cho các cặp màu đo được. Phép đo dùng màu chữ và nền solid gần nhất trong cây layer; không mô phỏng toàn bộ blending/assistive technology.
- Các click target được audit đều đạt **48 × 48 dp** trở lên; AppBar leading wrapper 48 dp, button chính cao 52 dp, nav item 82 × 68 dp ở bản chuẩn.
- Field border dùng token mới `color/border/control`, tương phản khoảng **6,47:1** trên nền trắng, vượt ngưỡng 3:1. Viền biểu đồ dùng primary, không phụ thuộc light fill để phân biệt cột.
- Không có text bounding box vượt cạnh màn ở 360/412 trong audit; đã xem render toàn bộ bộ ảnh sau sửa.
- QA dùng tên control trong accessibility tree, focus + Enter để chạy ba flow, nhánh lỗi, empty, overlay và 15 inactive tab destinations. Không dùng Next frame để bỏ qua liên kết.

Đây là kiểm tra thiết kế và Figma Present. Chưa kiểm tra thiết bị trợ năng thực, text scaling hệ điều hành, bàn phím ảo hoặc toàn bộ thứ tự Tab/focus trap. Figma xuất overlay dưới dạng article; không coi đó là semantic dialog của ứng dụng Flutter đã triển khai. ≥600 dp được mô tả trong handoff; đề không yêu cầu vẽ breakpoint này.

## Quyền truy cập và Present

**Present công khai đã đạt:** browser context mới, không cookies/đăng nhập, nhận HTTP 200 và render launch card thực; UI hiện “Log in or create account”. Không đổi quyền chia sẻ.

[Flow 1](https://www.figma.com/proto/Cc2O3xSmxgjfvDI2hrsY3Q?node-id=13-373&starting-point-node-id=13%3A373), [Flow 2](https://www.figma.com/proto/Cc2O3xSmxgjfvDI2hrsY3Q?node-id=13-378&starting-point-node-id=13%3A378), [Flow 3](https://www.figma.com/proto/Cc2O3xSmxgjfvDI2hrsY3Q?node-id=13-383&starting-point-node-id=13%3A383) đều chạy được; [biên bản browser](browser-check.md) lưu từng kết quả.

**Quyền xem editor/design công khai còn chưa xác minh:** endpoint design bị CloudFront 403 trong môi trường kiểm tra, chưa tới màn Figma xin quyền. Không kết luận file riêng tư hoặc tự khẳng định “Anyone with the link can view” đã bật. Cần mở link design trong cửa sổ riêng tư bên ngoài môi trường này để xác nhận người chấm có thể xem đủ sáu trang.

## Tài liệu và nguồn thực thi

- [AI log](../../ai/ai-design-log.md) khai báo Codex/Figma MCP, đầu vào, prompt thực tế, phát hiện và quyết định; không giả lập Stitch.
- [Các script Figma](../../tools/figma/README.md) ghi thao tác đã thực hiện và giới hạn chạy lại; audit cuối là bằng chứng trạng thái hiện tại.
- [Đối chiếu đề gốc](../submission-review.md) giữ rõ việc công cụ thay thế cần giảng viên chấp thuận; đây không phải xác nhận đã đạt trọn rubric AI generation/iteration lịch sử.

Các tài liệu API chính thức đã đối chiếu: [Reaction](https://developers.figma.com/docs/plugins/api/Reaction/), [Trigger](https://developers.figma.com/docs/plugins/api/Trigger/), [flowStartingPoints](https://developers.figma.com/docs/plugins/api/properties/PageNode-flowstartingpoints/). Tài liệu Trigger mô tả timeout theo milliseconds; giá trị MCP dùng trong file này được chọn theo hành vi thực tế trong Present, không chỉ suy diễn từ nhãn đơn vị của snapshot cũ.

## Kiểm tra repository và review độc lập

Validator đạt: 144 đường dẫn nội bộ, 25 PNG khớp byte/SHA-256/CRC, 11 wireframe không chồng, đủ states/Auto Layout, 3 native flow starts, 95 reactions và coverage accessibility khớp từng node/kích thước với audit. Đã thử sáu dữ liệu lỗi trong bộ nhớ: thiếu Filled, wireframe chồng, thiếu starting point, timer cũ, contrast thấp và mất coverage Final UI/360 dp; tất cả bị validator từ chối. Review độc lập xác nhận kết quả và không còn finding cần sửa; git diff --check đạt.
