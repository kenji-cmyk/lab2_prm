# Ảnh xuất từ Figma sau sửa

Đã có **25 PNG** từ Figma MCP: 11 frame chuẩn (8 chức năng + 3 trạng thái), 1 overlay, 11 bản412dp, 1 overview wireframe và 1 states review. Đây là bằng chứng Codex/Figma, không phải Stitch. [Manifest](manifest.json) ghi node, kích thước/byte/SHA-256 và link nguồn.

| File | Vai trò | Kích thước |
| --- | --- | --- |
| [01-chao-mung.png](01-chao-mung.png) | functional | 360 × 800 |
| [02-thiet-lap-muc-tieu.png](02-thiet-lap-muc-tieu.png) | functional | 360 × 800 |
| [03-trang-chu.png](03-trang-chu.png) | functional | 360 × 800 |
| [04-ghi-bua-an.png](04-ghi-bua-an.png) | functional | 360 × 800 |
| [05-dang-phan-tich.png](05-dang-phan-tich.png) | state | 360 × 800 |
| [06-ket-qua.png](06-ket-qua.png) | functional | 360 × 800 |
| [07-loi-ket-noi.png](07-loi-ket-noi.png) | state | 360 × 800 |
| [08-nhat-ky-bua-an.png](08-nhat-ky-bua-an.png) | functional | 360 × 800 |
| [09-nhat-ky-trong.png](09-nhat-ky-trong.png) | state | 360 × 800 |
| [10-tien-trinh-tuan.png](10-tien-trinh-tuan.png) | functional | 360 × 800 |
| [11-bai-hoc-nho.png](11-bai-hoc-nho.png) | functional | 360 × 800 |
| [12-overlay-xac-nhan-huy.png](12-overlay-xac-nhan-huy.png) | overlay | 360 × 800 |
| [13-trang-chu-412.png](13-trang-chu-412.png) | responsive | 412 × 800 |
| [14-wireframe-overview.png](14-wireframe-overview.png) | wireframe-overview | 593 × 1800 |
| [15-component-states.png](15-component-states.png) | component-review | 736 × 460 |
| [responsive/01-chao-mung-412.png](responsive/01-chao-mung-412.png) | responsive | 412 × 800 |
| [responsive/02-thiet-lap-muc-tieu-412.png](responsive/02-thiet-lap-muc-tieu-412.png) | responsive | 412 × 800 |
| [responsive/04-ghi-bua-an-412.png](responsive/04-ghi-bua-an-412.png) | responsive | 412 × 800 |
| [responsive/05-dang-phan-tich-412.png](responsive/05-dang-phan-tich-412.png) | responsive | 412 × 800 |
| [responsive/06-ket-qua-412.png](responsive/06-ket-qua-412.png) | responsive | 412 × 800 |
| [responsive/07-loi-ket-noi-412.png](responsive/07-loi-ket-noi-412.png) | responsive | 412 × 800 |
| [responsive/08-nhat-ky-bua-an-412.png](responsive/08-nhat-ky-bua-an-412.png) | responsive | 412 × 800 |
| [responsive/09-nhat-ky-trong-412.png](responsive/09-nhat-ky-trong-412.png) | responsive | 412 × 800 |
| [responsive/10-tien-trinh-tuan-412.png](responsive/10-tien-trinh-tuan-412.png) | responsive | 412 × 800 |
| [responsive/11-bai-hoc-nho-412.png](responsive/11-bai-hoc-nho-412.png) | responsive | 412 × 800 |

Wireframe hiện chỉ còn bộ52:* với11frame low-fi trắng–xám, không chồng; icon/nhãn navigation cách4px, nguồn hồi cứu được khai báo. Ảnh overview đã xuất lại sau lượt tinh chỉnh bằng MCP; [audit Wireframe](../../docs/reviews/wireframe-audit.json) ghi 143 text layers, cỡ nhỏ nhất14px, không text bounding box chồng nhau hoặc vượt khung. Bộ412đối chiếu đủS01–S11, không tính tăng số màn chức năng. [Review sau sửa](../../docs/reviews/current-fix-review.md) và [QA Present](../../docs/reviews/browser-check.md) tách bằng chứng hình ảnh khỏi tương tác/quyền truy cập.

Chạy python tools/validate_lab2.py từ thư mục gốc để kiểm tra manifest, PNG, đường dẫn, component states, native starting points và audit accessibility. Fixture không chứng minh lưu dữ liệu thật.
