# Review căn chỉnh Figma — Nếp Lành, Nhóm 6

Ngày kiểm tra: 22/10/2026.

File thiết kế: [Nhóm 6 — Ăn gì không chết](https://www.figma.com/design/Cc2O3xSmxgjfvDI2hrsY3Q).

## Quyền thư mục

Đã thử tạo, ghi và xóa file trong `D:\lab2_prm`: thành công. Không cần cấp quyền thêm bằng PowerShell. Ảnh PNG tạm do Playwright tạo trong lượt trước cũng đã được xóa thành công.

## Các lỗi đã sửa trên Figma

- Button: nhãn trước đây căn trái trong khung đã căn giữa. Đã căn giữa ngang và dọc, dùng Roboto Medium 16 px, dòng 24 px, đồng bộ bốn trạng thái của component.
- Card và header: sửa chiều cao khung chữ theo chiều cao dòng; tiêu đề 20/28 px, nội dung 14/20 px; đồng bộ padding và căn logo NL vào giữa vòng tròn.
- Form: căn nội dung giữa theo chiều dọc, padding ngang 16 px; thống nhất khoảng cách giữa nhãn, ô nhập và hướng dẫn.
- Điều hướng: tích hợp vector vào component Navigation Item, đặt icon và nhãn cùng trục giữa, dùng đúng biến thể Icon/State; xóa 44 icon rời từng đặt bên ngoài component.
- Trạng thái tải/rỗng: gom icon và vòng tròn nền vào cùng một frame để Auto Layout giữ chúng đồng tâm; căn giữa tiêu đề và mô tả.
- Nút chữ phụ, nhãn ngày trên biểu đồ và thao tác hủy trong hộp thoại: căn giữa; loại bỏ dòng “Thử lại” bị lặp trong thẻ lỗi và chỉnh lại khoảng cách CTA.
- Áp dụng đồng bộ cho Final UI, Prototype và màn trang chủ rộng 412 px.

## Kết quả kiểm tra cuối

| Hạng mục | Kết quả |
| --- | --- |
| Button được kiểm tra | 26 |
| Button lệch tâm nhãn | 0 |
| Navigation Item được kiểm tra | 44 |
| Lỗi icon, trạng thái hoặc căn nhãn tab | 0 |
| Card có chữ vượt cạnh dưới | 0 |
| Khung chữ thấp hơn chiều cao một dòng | 0 |
| Font thiếu | 0; các lớp chữ được kiểm tra dùng Roboto |
| Prototype reactions | 32 |
| Đích điều hướng | 31 |
| Đích điều hướng bị thiếu | 0 |

Đã xem ảnh render của các màn chính, hộp thoại hủy, component điều hướng và màn responsive. Kiểm tra này sử dụng renderer và cấu trúc Figma; không phải kiểm thử thao tác trực tiếp trong trình xem Figma bằng Playwright, vốn đã trả HTTP 403 trong lượt trước.
