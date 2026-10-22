# Script sửa và kiểm tra Figma

Các file JavaScript là mã chạy qua **Figma MCP use_figma**, không phải JavaScript chạy trực tiếp bằng Node. File đích: `Cc2O3xSmxgjfvDI2hrsY3Q`. Chỉ chạy khi có quyền sửa và đã đọc các skill Figma liên quan.

- `fix-components.js`: thêm variants thiếu, border control có tương phản và sắp khu vực thư viện.
- `fix-wireframes.js`: xóa đúng IDs của bộ trùng đã kiểm kê, sắp bộ chính 52:*.
- `refine-wireframes.js`: tinh giản 11 frame thành low-fi trắng–xám, sửa thứ tự icon/nhãn bằng Auto Layout và đồng bộ nội dung trạng thái. Phạm vi chỉ trang 02 Wireframe; giữ IDs và vị trí 11 khung.
- `fix-prototype.js`: nối Goal choices, inactive tabs, empty entry và native starting points.
- `fix-screen-accessibility.js`: đồng bộ nội dung/state labels và thứ tự đọc; đổi PAGE_ID giữa Final UI/Prototype theo phạm vi.
- `fix-noncolor-states.js`: dấu ✓ và text alternative của biểu đồ.
- `preview-states.js`: instances review và spinner pattern.
- `check-responsive-412.js`: tạo khung đối chiếu 412 dp cho mọi màn.
- `audit-accessibility.js`: đọc màu, chữ, bounds, click targets và field border; không sửa thiết kế.

Đây là các bước sửa có phụ thuộc node ID, không phải pipeline dựng lại từ đầu. Một số sửa sau QA (timer MCP `1.3`, nút Xem kết quả, reading order bên trong overlay/launch) được ghi trong [review hiện tại](../../docs/reviews/current-fix-review.md) và [audit cuối](../../design/figma-audit.json). Không chạy lại toàn bộ scripts trên file đã sửa mà không đọc trạng thái trước; snapshot và PNG cuối mới mô tả trạng thái được bàn giao.
