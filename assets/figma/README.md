# Figma evidence

Đã có **14 PNG** xuất qua Figma MCP, không phải output Stitch. [Manifest](manifest.json) ghi node ID, vai trò, kích thước, số byte, SHA-256 và link Figma của từng ảnh.

| Ảnh | Vai trò |
| --- | --- |
| [01 Chào mừng](01-chao-mung.png) | Màn chức năng |
| [02 Thiết lập mục tiêu](02-thiet-lap-muc-tieu.png) | Màn chức năng |
| [03 Trang chủ](03-trang-chu.png) | Màn chức năng |
| [04 Ghi bữa ăn](04-ghi-bua-an.png) | Màn chức năng |
| [05 Đang phân tích](05-dang-phan-tich.png) | Loading |
| [06 Kết quả](06-ket-qua.png) | Màn chức năng |
| [07 Lỗi kết nối](07-loi-ket-noi.png) | Trạng thái lỗi |
| [08 Nhật ký bữa ăn](08-nhat-ky-bua-an.png) | Màn chức năng |
| [09 Nhật ký trống](09-nhat-ky-trong.png) | Trạng thái rỗng |
| [10 Tiến trình tuần](10-tien-trinh-tuan.png) | Màn chức năng |
| [11 Bài học nhỏ](11-bai-hoc-nho.png) | Màn chức năng |
| [12 Xác nhận hủy](12-overlay-xac-nhan-huy.png) | Overlay |
| [13 Trang chủ 412 dp](13-trang-chu-412.png) | Responsive |
| [14 Tổng quan wireframe](14-wireframe-overview.png) | Snapshot trang 02 |

S01–S11 và overlay là 360 × 800 px; Home responsive 412 × 800 px; wireframe overview 592 × 1800 px. Có đúng **8 màn chức năng**, không cộng trạng thái hoặc overlay.

Bộ wireframe 52:* được dựng hồi cứu từ UI cuối. [Metadata mới](../../docs/reviews/figma-metadata-2026-10-22.json) ghi nhận trang 02 có thêm bộ 12:* đặt chồng; ảnh overview là snapshot đã xuất, chưa xuất lại sau khi dọn trang. PNG không chứng minh reactions, lưu dữ liệu, quyền xem công khai hay chạy được Present.

Chạy `python tools/validate_lab2.py` từ thư mục gốc để kiểm tra hồ sơ. Xem [checklist còn thiếu](../../docs/submission-review.md).
