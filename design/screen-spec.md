# Nếp Lành — đặc tả Final UI và prototype

File [Figma](https://www.figma.com/design/Cc2O3xSmxgjfvDI2hrsY3Q), cập nhật sau sửa ngày22/10/2026. Final UI có **8 màn chức năng, 3 trạng thái** ở360×800, cộng overlay; có11 frame412 đối chiếu trên Prototype. [Handoff](../handoff/flutter-handoff.md) ghi đủ6mục/frame và mapping Flutter.

| Mã | Frame | Final node | Prototype node | Vai trò/flow |
| --- | --- | --- | --- | --- |
| S01 | Chào mừng | 6:2 | 13:418 | Màn chức năng, flow1 |
| S02 | Thiết lập mục tiêu | 6:19 | 13:434 | Màn chức năng, flow1; alternatives63:267/63:291 |
| S03 | Trang chủ | 6:42 | 13:447 | Màn chức năng, entry flow2/3 |
| S04 | Ghi bữa ăn | 6:76 | 13:465 | Màn chức năng, flow2 |
| S05 | Đang phân tích | 6:101 | 13:476 | Trạng thái loading, flow2 |
| S06 | Kết quả | 6:118 | 13:485 | Màn chức năng, flow2 |
| S07 | Lỗi kết nối | 6:138 | 13:497 | Trạng thái lỗi/retry, flow2 |
| S08 | Nhật ký bữa ăn | 6:155 | 13:507 | Màn chức năng, kết thúc flow2 |
| S09 | Nhật ký trống | 6:186 | 13:522 | Trạng thái ngày chưa ghi, nhánh flow2 |
| S10 | Tiến trình tuần | 6:213 | 13:534 | Màn chức năng, flow3 |
| S11 | Bài học nhỏ | 6:257 | 13:563 | Màn chức năng, flow3 và tab Học |
| — | Xác nhận hủy | 10:126 | 13:579 | Overlay của S04, không tính màn riêng |

## Nội dung và ý đồ từng màn

- **S01:** thương hiệu/hero, giải thích ghi bữa và học nhẹ nhàng; CTA Thiết lập mục tiêu→S02; disclaimer. Không yêu cầu tài khoản hoặc dữ liệu cá nhân.
- **S02:** Back→S01, ba goal cards, dấu✓/Đã chọn và CTA Lưu mục tiêu→Home. Chọn card chuyển giữa ba frame trạng thái để biểu thị lựa chọn. Home vẫn là fixture, không suy ra dữ liệu goal được lưu.
- **S03:** greeting/date, goal/progress mẫu, tip, CTA Ghi bữa→S04, link tuần→S10, bốn tab. Selected tab có✓; mọi inactive destination đã nối.
- **S04:** Text Field/Filled cho tên món và thời điểm mẫu, hướng dẫn không cần đếm calo, CTA→S05, link mô phỏng offline→S07. Back mở overlay. Không có input/validation động thật.
- **S05:** spinner ring40dp, title/body, timer tự→S06 và Xem kết quả→S06; Back/nút sửa→S04. MCP timeout hiện1.3 được xác minh bằng Present; không dùng diễn giải1300ms của snapshot cũ để khẳng định timer hoạt động.
- **S06:** kết quả/gợi ý tham khảo, meal summary và hai card, Lưu vào nhật ký→S08, edit/Back→S04. Đây là nội dung mẫu; chưa phải xác nhận transaction lưu thật.
- **S07:** thông báo chưa tải gợi ý, nguyên nhân kết nối, Retry→S05, Back/Quay lại món ăn→S04. Copy yêu cầu quay lại biểu mẫu kiểm tra, không hứa đã giữ dữ liệu trên thiết bị.
- **S08:** ngày, bản ghi/note mẫu, summary, Ghi thêm→S04, Xem ngày chưa ghi bữa→S09, nav đầy đủ.
- **S09:** heading Ngày chưa ghi bữa, icon/message/CTA→S04, nav đầy đủ; có đường vào từ S08.
- **S10:** tuần/mục tiêu mẫu,7cột có outline, text Đã ghi:T2–T6/Chưa ghi:T7,CN, highlight trung tính; link đọc→S11 và nav đầy đủ.
- **S11:** article/topic/card hành động/nguồn/disclaimer; AppBar BACK theo nguồn gọi Home/Weekly, CTA Đánh dấu đã đọc→Weekly. Bottom tabs hoạt động.
- **Overlay:** title/body nói rõ hủy thông tin, Continue dùng CLOSE để lộ lại S04, Confirm→Home. Figma mô phỏng fixture; ứng dụng Flutter phải quản lý draft/focus/semantics thật.

## Design system và ràng buộc chung

Roboto; text hiển thị≥14px. Spacing4/8/12/16/24/32dp, radius8/12/20/pill999. Primary CTA52dp; Back hit48×48; nav item82×68 ở360dp; secondary48dp.

Color tokens và style inventory nằm trong [brief](DESIGN.md) và [audit](figma-audit.json). Có Button Default/Focused/Pressed/Loading/Disabled, Text Field Default/Focused/Filled/Error/Disabled, Card Default/Selected/Pressed, Dialog Open/Confirmed/Destructive và các nhóm bắt buộc khác.

Giữ nội dung cuộn/không bị bàn phím che khi triển khai, không khóa text height khi font scale tăng, CTA có thể cuộn tới. Breakpoint≥600 giữ cột đọc giới hạn, có thể dùng hai cột/NavigationRail theo handoff. Figma layout/fixture không chứng minh hành vi Flutter đã triển khai.

[Audit accessibility](../docs/reviews/accessibility-audit.json) ghi text contrast thấp nhất5,52:1 và không text vượt màn trong phạm vi đo; [QA](../docs/reviews/browser-check.md) xác nhận ba flow,15inactive tabs, lỗi/overlay/loading/Back. Giới hạn thiết bị trợ năng và quyền editor công khai ghi trong [review hiện tại](../docs/reviews/current-fix-review.md).
