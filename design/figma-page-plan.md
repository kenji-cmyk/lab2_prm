# Sáu trang Figma — Nếp Lành

[File Figma](https://www.figma.com/design/Cc2O3xSmxgjfvDI2hrsY3Q).

| Thứ tự | Trang | Nội dung hiện tại |
| --- | --- | --- |
| 1 | 01 User Flow | Persona Minh, vấn đề và ba flow card; Mermaid chi tiết trong ux/user-flow.md. |
| 2 | 02 Wireframe | Metadata mới có 22 frame: bộ 12:* và bộ grayscale 52:* dựng hồi cứu ngày 22/10/2026 đang đặt chồng; cần chọn/sắp xếp một bộ chính. Không chứng minh thứ tự trước AI generation. |
| 3 | 03 Final UI | S01–S11 ở 360 × 800; 8 màn chức năng, 3 trạng thái S05/S07/S09; overlay xác nhận hủy. |
| 4 | 04 Design System | 14 màu, typography Roboto, spacing, radius, elevation. Variable/binding được lưu trong audit JSON. |
| 5 | 05 Components | 9 nhóm bắt buộc và Navigation Icons, dùng Auto Layout và variants. |
| 6 | 06 Prototype | Ba flow, overlay hủy, loading → result, lỗi/retry; thêm trang chủ 412 px. |

## Mapping

S01 Chào mừng; S02 Thiết lập mục tiêu; S03 Trang chủ; S04 Ghi bữa ăn; S05 Đang phân tích; S06 Kết quả; S07 Lỗi kết nối; S08 Nhật ký bữa ăn; S09 Nhật ký trống; S10 Tiến trình tuần; S11 Bài học nhỏ.

Đối chiếu node ID với [screen-spec.md](screen-spec.md) và [manifest ảnh](../assets/figma/manifest.json). Overlay không tính vào tám màn chức năng.

## Cần xác minh ngoài file

- Mở link bằng tài khoản khác để xác nhận quyền xem; Playwright trước gặp HTTP 403.
- Chạy ba flow bằng Present để kiểm tra Back, overlay, timer và retry thực tế.
- Bổ sung bằng chứng Google Stitch nguyên bản; không dùng wireframe hồi cứu hoặc PNG Figma làm ảnh Stitch.
