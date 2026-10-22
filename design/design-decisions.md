# Nếp Lành — Design decisions

Cập nhật sau sửa Figma ngày 22/10/2026. Có tối đa 10 quyết định chính; [AI log](../ai/ai-design-log.md) ghi đầu vào, phát hiện và quyết định theo quy trình Codex + Figma MCP.

| # | Quyết định | Lý do và kết quả |
| --- | --- | --- |
| 1 | Giữ app ở phạm vi giáo dục và tự theo dõi. | Persona cần ghi/học nhẹ nhàng; không chẩn đoán hoặc hứa kết quả sức khỏe. |
| 2 | Đếm 8 màn chức năng, tách loading/error/empty và overlay. | Đúng quy tắc rubric; không tăng số màn bằng trạng thái. |
| 3 | Chỉ giữ 11 wireframe bộ 52:*. | Xóa bộ 12:* chồng nhau; grid rõ. Khai báo bộ hồi cứu, không sửa lịch sử. |
| 4 | Goal có ba lựa chọn với ✓ và chữ Đã chọn. | Minh cần biết đang chọn gì; ba prototype variants phản hồi rõ, Save dẫn Home mẫu. Không khẳng định persistence. |
| 5 | Dùng lại component, thêm states thiếu. | Bổ sung Pressed/Filled/Disabled/Destructive, giữ Auto Layout, bindings và instances review. |
| 6 | Hoàn thiện control hiển thị và Back theo nguồn vào. | Nối Home link, 15 inactive tabs, empty entry; Article dùng BACK thay đích cố định. QA chạy trực tiếp đạt. |
| 7 | Loading có timer đã kiểm thử và nút Xem kết quả. | Runtime không chuyển với giá trị MCP cũ; sau sửa tự chuyển, có đường chủ động cho người dùng. |
| 8 | Error copy chỉ nói điều prototype chứng minh. | Không hứa đã giữ trên thiết bị khi chỉ có dữ liệu mẫu; retry/back/overlay kiểm thử riêng. |
| 9 | Không truyền trạng thái chỉ bằng màu. | Goal/nav có ✓, biểu đồ có text ngày đã/chưa ghi và viền rõ; field border có token tương phản riêng. |
| 10 | Giữ quy trình AI có thể truy vết. | Codex đọc đề/UX/brief rồi dùng Figma MCP; không gắn ảnh Figma thành Stitch hoặc tạo ba vòng lặp lịch sử giả. |

## Accessibility và responsive checklist

| Tiêu chí | Kết quả sau sửa | Phạm vi bằng chứng |
| --- | --- | --- |
| Text contrast ≥4,5:1 | Đạt trong audit: thấp nhất 5,52:1. | 148 text layers Final UI và 316 Prototype/responsive; màu chữ/nền solid gần nhất. |
| UI control contrast ≥3:1 | Field border khoảng 6,47:1; selected/primary/chart outlines đạt ngưỡng. | Token color/border/control và primary; hình trang trí không dùng riêng làm thông tin. |
| Tap targets ≥48 × 48 dp | Không click target dưới ngưỡng trong audit; Back wrapper 48, CTA52, nav82×68. | Reactions và component geometry, không suy ra thử chạm trên phần cứng. |
| Body/labels ≥14 sp | Các text layers hiển thị tối thiểu 14 px trong thiết kế, font Roboto. | Figma dp/px tương ứng ở khung chuẩn; app Flutter cần giữ đơn vị sp. |
| Không chỉ bằng màu | ✓/Đã chọn cho goal, ✓ cho selected nav, chart có text alternative. | Render mới và QA quan sát. |
| 360/412 dp | 11 frame chuẩn360 và 11 frame412; audit không text vượt màn. | Có PNG đối chiếu, không chỉ Home. |
| ≥600 dp | Có mô tả trong handoff. | Đề không yêu cầu thiết kế frame breakpoint này. |
| Reading order/keyboard | Đã sửa top-level, launch và overlay; focus+Enter chạy ba flow và15tabs. | Figma Present bật Adapt content for screen readers. |
| Lỗi/phục hồi/overlay | Retry, sửa, Continue/Cancel, empty entry và loading/result đạt. | Walkthrough thực tế; fixture không chứng minh giữ input thật. |

Bằng chứng: [audit accessibility](../docs/reviews/accessibility-audit.json), [QA browser](../docs/reviews/browser-check.md), [review tổng hợp](../docs/reviews/current-fix-review.md) và [PNG](../assets/figma/README.md).

Chưa thử TalkBack/VoiceOver trên thiết bị, text scaling hệ điều hành, bàn phím ảo hoặc toàn bộ thứ tự Tab/focus trap. Figma xuất overlay dạng article; chưa có semantic dialog của ứng dụng Flutter. Không coi kết quả này là chứng nhận toàn bộ WCAG.
