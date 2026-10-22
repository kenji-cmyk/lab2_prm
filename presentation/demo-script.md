# Demo Lab 2 — Nhóm 6

10 phút trình bày, 5 phút demo và 5 phút hỏi đáp là gợi ý trong hướng dẫn; không khẳng định slide là sản phẩm bắt buộc của đề gốc.

## Trình bày gợi ý

1. Đề tài Nếp Lành, sách tham khảo, persona Minh và vấn đề.
2. Tám màn chức năng, ba frame trạng thái và ba flow.
3. Sáu trang Figma; trang Wireframe giữ 11 frame `52:*` dựng hồi cứu từ Final UI, grid ba cột không chồng; 11 frame trùng `12:*` đã xóa. Không trình bày chúng là wireframe có trước thiết kế.
4. Roboto, màu, spacing/radius và chín nhóm component.
5. Các lỗi đã sửa: thiếu Pressed/Filled/Disabled/Destructive; chọn mục tiêu chưa phản hồi; tab/link chưa nối; Back bài học sai ngữ cảnh; wireframe chồng; timer loading sai giá trị. Dẫn chứng chi tiết trong [review lượt sửa](../docs/reviews/current-fix-review.md).
6. Handoff theo sáu mục/frame, token → Flutter và component → widget.
7. Khai báo AI: Codex đọc tài liệu rồi dùng Figma MCP sửa thiết kế; không dùng Stitch và không dựng lại ba vòng lặp lịch sử. Đề gốc cần giảng viên chấp thuận công cụ thay thế. Audit thiết kế không thay kiểm thử Flutter trên thiết bị.

## Demo Figma Present

- Chọn một trong ba native starting points trên trang 06: launch `13:373` / `13:378` / `13:383`. QA đã đạt ba flow, ba lựa chọn mục tiêu, 15 tab chưa chọn, retry, overlay, empty và Back theo ngữ cảnh; [review hiện tại](../docs/reviews/current-fix-review.md) lưu bằng chứng.
- Flow 1: S01 → S02; bấm cả ba thẻ để thấy ✓ / “Đã chọn”; Lưu mục tiêu → S03. Nói rõ Home là dữ liệu mẫu, không chứng minh lưu lựa chọn.
- Flow 2: S03 → S04 (fields Filled mẫu) → S05 → S06 → S08. Loading tự đi sau khoảng 1,3 giây, có “Xem kết quả” dự phòng.
- Tại S04, liên kết mô phỏng lỗi mở S07; Retry trở lại loading/result. Back ở S04 mở overlay hủy; tiếp tục chỉnh sửa hoặc xác nhận hủy.
- Flow 3: mở S10 bằng tab Tiến trình hoặc link tuần trên S03 → S11 → Back về S10. Thử Home → tab Học → S11 → Back về Home; CTA cuối bài luôn mở Weekly.
- Tại S08 bấm “Xem ngày chưa ghi bữa” → S09 → Ghi bữa ăn → S04. Giải thích đây là ngày trống trong nhật ký mẫu, không tính thành màn chức năng thứ chín.
- Thử mọi tab chưa chọn trên Home/Journal/Empty/Weekly/Article; tab đang chọn có ✓ và không chuyển trang.
- So sánh S01–S11 ở 360/412 dp; chỉ dấu chọn và text chart chứng minh trạng thái ngoài màu sắc. Mở trang Components để thấy đủ các states mới.

Prototype mô phỏng chuyển màn; không thực hiện phân tích AI, database hay đồng bộ.

Present đã mở và kiểm tra được khi không đăng nhập. Trang editor trả CloudFront 403 trong lượt kiểm tra nên chưa xác minh được quyền truy cập editor; khi demo dùng link Present đã kiểm tra trong review.

Audit 25 frame 360/412 ghi contrast chữ thấp nhất 5.52:1, body ≥14 px và vùng bấm được audit ≥48 dp. Không trình bày đây là kết quả TalkBack/VoiceOver, text scaling 200% hoặc kiểm thử Flutter; các kiểm tra đó cần thiết bị/ứng dụng thật.

## Hồ sơ hỏi đáp

- [Bảng đối chiếu yêu cầu](../docs/submission-review.md)
- [Persona](../ux/persona.md), [flow](../ux/user-flow.md)
- [AI log](../ai/ai-design-log.md)
- [Review lượt sửa và bằng chứng Present/quyền xem](../docs/reviews/current-fix-review.md)
- [Screen spec](../design/screen-spec.md), [handoff](../handoff/flutter-handoff.md)
- [Ảnh Figma](../assets/figma/README.md)

Không trình bày prompt dự kiến, phản hồi ví dụ, wireframe hồi cứu hoặc HTML cũ như bằng chứng Google Stitch hay ba vòng lặp AI lịch sử.
