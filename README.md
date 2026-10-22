# Nhóm 6 — Nếp Lành | PRM323 Lab 2

Ứng dụng hướng dẫn và theo dõi thói quen ăn uống, lấy cảm hứng từ sách **Ăn gì không chết – Sức mạnh chữa lành của thực phẩm**. Persona giả định: **Minh, 20 tuổi, sinh viên**, cần ghi nhanh bữa ăn, xem tiến trình và đọc bài ngắn trên điện thoại.

**Thiết kế:** [Figma của Nhóm 6](https://www.figma.com/design/Cc2O3xSmxgjfvDI2hrsY3Q). Mở trang **06 Prototype**, chọn điểm bắt đầu rồi bấm Present.

**Cập nhật 22/10/2026:** đã bổ sung component states, sửa prototype và Wireframe, kiểm tra accessibility ở 360/412 dp và chạy ba flow trực tiếp. Có 8 màn chức năng, 3 trạng thái, overlay và 25 PNG. **Present mở công khai khi không đăng nhập**; quyền xem editor/design công khai còn chưa xác minh do CloudFront 403 trong môi trường. Xem [kết quả sau sửa](docs/reviews/current-fix-review.md).

**Quy trình AI:** Codex đọc đề, persona, user flow và brief rồi dùng Figma MCP để thiết kế, phản biện và tinh chỉnh. Không dùng Stitch hoặc dựng lịch sử ba vòng lặp giả. [AI log](ai/ai-design-log.md) lưu prompt và bằng chứng thực tế; việc thay công cụ theo đề gốc cần giảng viên chấp thuận.

## Các flow

1. Bắt đầu: Chào mừng → Thiết lập mục tiêu → Trang chủ.
2. Ghi bữa ăn: Trang chủ → Ghi bữa ăn → Đang phân tích → Kết quả → Nhật ký; có mô phỏng lỗi/thử lại và overlay xác nhận hủy.
3. Theo dõi và học: Trang chủ → Tiến trình tuần → Bài học nhỏ → quay lại.

QA trong Present đã chạy ba lựa chọn mục tiêu, 15 inactive tab destinations, lỗi/retry, empty, overlay, loading/result và Back theo nguồn vào. S05/S07/S09 là trạng thái; dialog không tính thành màn chức năng riêng. [Flow 1](https://www.figma.com/proto/Cc2O3xSmxgjfvDI2hrsY3Q?node-id=13-373&starting-point-node-id=13%3A373), [Flow 2](https://www.figma.com/proto/Cc2O3xSmxgjfvDI2hrsY3Q?node-id=13-378&starting-point-node-id=13%3A378), [Flow 3](https://www.figma.com/proto/Cc2O3xSmxgjfvDI2hrsY3Q?node-id=13-383&starting-point-node-id=13%3A383).

## Hồ sơ bàn giao

| Sản phẩm | Đường dẫn |
| --- | --- |
| Kết quả đối chiếu yêu cầu và checklist còn thiếu | [docs/submission-review.md](docs/submission-review.md) |
| Đề PDF, hướng dẫn DOCX nguyên bản và tóm tắt | [docs/requirements/](docs/requirements/README.md) |
| Persona | [ux/persona.md](ux/persona.md) |
| Ba sơ đồ flow và mapping màn hình | [ux/user-flow.md](ux/user-flow.md) |
| Brief, token và components | [design/DESIGN.md](design/DESIGN.md) |
| Đặc tả 11 frame và overlay | [design/screen-spec.md](design/screen-spec.md) |
| Quyết định và accessibility | [design/design-decisions.md](design/design-decisions.md) |
| Sáu trang Figma | [design/figma-page-plan.md](design/figma-page-plan.md) |
| Prompt và AI log | [ai/ai-design-log.md](ai/ai-design-log.md) |
| PNG Final UI, overlay, responsive và manifest | [assets/figma/](assets/figma/README.md) |
| Trạng thái bằng chứng Stitch | [assets/stitch/](assets/stitch/README.md) |
| Handoff: 6 mục/frame, token/widget maps | [handoff/flutter-handoff.md](handoff/flutter-handoff.md) |
| Kịch bản demo | [presentation/demo-script.md](presentation/demo-script.md) |
| Review căn chỉnh và metadata Figma mới | [docs/reviews/](docs/reviews/README.md) |
| Bản HTML thử nghiệm cũ | [archive/prototype-html/](archive/prototype-html/README.md) |

Giữ các thư mục sản phẩm theo cấu trúc đề yêu cầu; đề gốc nằm trong `docs/requirements/`, biên bản kiểm tra trong `docs/reviews/`, bản nháp cũ trong `archive/`. Không cần viết Flutter trong Lab này.

## Kiểm tra repository

Chạy từ thư mục gốc với Python 3, không cần cài thêm thư viện:

```sh
python tools/validate_lab2.py
```

Lệnh kiểm tra cấu trúc, đường dẫn Markdown nội bộ, SHA-256/kích thước/CRC của PNG và các đường đi trong snapshot audit Figma. PASS chỉ nói về tính toàn vẹn của hồ sơ; các thiếu sót để nộp bài được in riêng, không được xem là đã đạt rubric.

## Công cụ AI và giới hạn bằng chứng

- **OpenAI Codex:** hỗ trợ tài liệu, rà soát UI/yêu cầu, prototype cũ và script kiểm tra.
- **Figma MCP:** đọc cấu trúc/token, sửa variants, Wireframe, prototype và accessibility; xuất lại 25 PNG và lưu audit sau sửa.
- **Playwright:** sau khi Browser trong ứng dụng lỗi khởi tạo, dùng trình duyệt dự phòng chạy ba flow và xác minh Present trong context mới chưa đăng nhập. Endpoint editor/design vẫn bị CloudFront chặn; [QA](docs/reviews/browser-check.md) phân biệt rõ hai kết quả.
- **Impeccable:** chưa có skill/lệnh cài trong phiên trước; chỉ tham khảo tiêu chí review thủ công.
- **Google Stitch:** không dùng theo lựa chọn của người thực hiện bài; bằng chứng thực tế dùng Codex + Figma MCP, được ghi đúng trong log.

Persona chưa được nghiên cứu thực địa. Bộ wireframe `52:*` được dựng hồi cứu từ Final UI ngày 22/10/2026; không chứng minh quy trình trước Stitch. Figma chỉ mô phỏng tương tác, chưa thực hiện phân tích dinh dưỡng hay lưu/đồng bộ dữ liệu. Nội dung ứng dụng mang tính giáo dục, không thay thế tư vấn y tế.
