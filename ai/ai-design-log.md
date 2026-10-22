# Nếp Lành — AI design log

## Trạng thái công cụ

**Google Stitch:** chưa chạy; chưa có công cụ Stitch trong môi trường làm việc hiện tại. Không có output, screenshot Stitch, phản hồi AI hay vòng lặp Stitch đã hoàn tất.<br>
**ChatGPT/Codex:** được dùng để soạn tài liệu dự án và các prompt chuẩn bị trong phiên này. Những nội dung này không phải output của Stitch.<br>
**Figma:** file hiện tại [Nếp Lành — Cc2O3xSmxgjfvDI2hrsY3Q](https://www.figma.com/design/Cc2O3xSmxgjfvDI2hrsY3Q). Các thao tác rà soát/căn chỉnh Figma đã ghi ở mục riêng phía dưới; không xem chúng là vòng lặp Stitch.<br>
**Ảnh:** chưa có ảnh Stitch. Đã có 14 ảnh render Figma trong [assets/figma](../assets/figma/README.md); không đưa ảnh đó vào assets/stitch/ hoặc gắn nhãn là ảnh Stitch.

## Prompt khởi đầu — chuẩn bị, chưa gửi

Prompt dưới đây được chuẩn bị cho lần chạy đầu tiên. **Chưa gửi tới Stitch.** Nếu nhóm sửa nội dung trước khi dùng, hãy lưu nguyên văn bản thực tế đã gửi và không ghi bản chuẩn bị này thành lịch sử chạy.

~~~text
Design a polished Vietnamese mobile habit app called Nếp Lành. It is intended to help adults record meals, explore plant-forward food learning, and choose a gentle optional habit goal. Optional goal, reminders, skip, edit, and Back interactions are future refinements; the current Goal frame is static. The product is educational, not medical: never diagnose, treat, claim disease prevention, prescribe a diet, promise a health result, or shame the user. Do not copy book text. Use a warm light UI. Current Figma palette: primary #2F6B4F, onPrimary #FFFFFF, primaryContainer #E1F1E6, onContainer #183D2D, canvas #F7F8F4, surface #FFFFFF, textPrimary #1F2B24, textSecondary #526258, border #D6DFD7, error #A4261D, errorContainer #F9DEDC, success #196C46, peach #F4E4D2, sky #E6EEF8. Use Roboto. Use spacing 4/8/12/16/24/32 dp and radii 12/20/pill. Design for a 360 x 800 dp phone. Create these 11 named frames in one coherent system: Welcome, Goal, Home, Meal form, Loading, Result, Offline error, Journal, Empty journal, Weekly, and Article. The current Goal frame is static; optional goals, reminders, skip, edit, and Back are planned refinements, not implemented behavior. Frame 5 Loading processes a meal to generate suggestions. Frame 6 Result shows suggestions and a “Lưu vào nhật ký” CTA that leads to frame 8 Journal; do not label it as a saved meal. Frame 7 Offline error belongs to suggestion processing. Preserving the form and Retry are proposed behaviors that require prototype validation. Keep Journal and Empty journal truthful to whether records exist. Make weekly progress descriptive rather than a health score. Give Article a visible source and educational disclaimer. Use familiar Vietnamese examples without medical claims or copied book content. Keep all controls at least 48 dp, body content at least 14 sp, labels clear, state meaning independent of color, and navigation with a sensible Back path. Avoid calories, body weight, dense charts, moralizing language, and invented personal data. Generate a light design system and reusable components with variants.
~~~

**Kết quả/prompt thực tế:** chưa có; chưa có ngày chạy, response hay ảnh output. Khi chạy thật, lưu chúng và cập nhật trạng thái, không tạo response thay AI.

## Ba vòng lặp Stitch dự kiến — chưa chạy

Các mục tiêu sau là giả định/kiểm tra cần làm khi có output. Chúng chưa phải phát hiện từ ảnh.

| Vòng | Mục tiêu cần kiểm tra | Prompt chỉnh sửa dự kiến | Trạng thái bằng chứng |
|---|---|---|---|
| 1 — Goal tĩnh sang tương tác | Goal hiện tại là frame tĩnh; skip, reminders, edit và Back là phần dự kiến. | “Refine only the Goal frame as a proposed future interaction. Add an explicit optional goal choice and a clear Skip action; make editing and Back behavior visible in the flow. Do not imply these interactions exist in the current Figma. Preserve the existing Roboto styles and palette.” | Chưa gửi. Đây là yêu cầu dự kiến, chưa có ảnh/response. |
| 2 — lỗi khi tạo gợi ý | Frame Offline error thuộc luồng xử lý gợi ý, không phải xác nhận lỗi lưu nhật ký. | “Refine only the Offline error state for meal suggestion processing. Keep the meal form recoverable and explain that suggestions could not be generated offline. Offer Retry and a safe return path. Do not say the meal was saved; saving happens only after the user chooses Lưu vào nhật ký on Result. Treat draft retention as a proposed behavior unless the prototype demonstrates it.” | Chưa gửi. Đây là yêu cầu dự kiến, chưa có ảnh/response. |
| 3 — nhật ký rỗng có hướng đi | Kiểm tra Empty journal có giải thích trạng thái rỗng và hành động tiếp theo mà không bịa dữ liệu hay không. | “Refine only Empty journal. Explain that there are no meal records yet, show no sample entries or invented user statistics, and provide one clear action to start a first meal record plus a route back to Home. Keep the design supportive and non-judgmental.” | Chưa gửi. Ảnh trước/sau và response: chưa có. |

Khi hoàn tất mỗi vòng thực tế, lưu screenshot trước/sau, prompt gửi thật, response AI nguyên văn, phát hiện gắn với frame, quyết định nhận/sửa/từ chối và lý do. Không điền giả kết quả vào bảng này.

## Prompt critique dự kiến

Chỉ dùng sau khi có ảnh thật từ Stitch. Đính kèm các ảnh đã tạo và thay mô tả persona bằng bản được duyệt.

~~~text
Review the attached actual Nếp Lành screens as a UX critic. The target persona is [paste the approved persona]. This is a non-clinical Vietnamese meal habit and learning app: do not suggest diagnosis, treatment, disease-prevention claims, health guarantees, or shaming language. Evaluate the visible screens using Nielsen’s 10 usability heuristics and these checks: normal text contrast >= 4.5:1, large text/controls >= 3:1, touch targets >= 48 x 48 dp, content text >= 14 sp, no color-only meaning, visible focus/state, clear error recovery, and responsive behavior at 360 dp and 412 dp. Return at least five findings tied to specific visible frames. For each finding state the frame, screenshot evidence, heuristic or accessibility criterion, severity, concrete recommendation, and a verification step. Separate observed problems from assumptions. Do not invent UI or user data that is not visible in the attachments.
~~~

## Ghi nhận rà soát Figma — thực tế, không phải Stitch

Nguồn: [review căn chỉnh](../docs/reviews/figma-alignment.md), ngày 22/10/2026. File: [Nếp Lành — Figma](https://www.figma.com/design/Cc2O3xSmxgjfvDI2hrsY3Q). Đây là các chỉnh sửa và phép đếm được ghi trong review của Figma; không có prompt/response AI tương ứng.

**Hành vi frame hiện tại theo `design/figma-audit.json`:** S02 Goal cards là tĩnh; Back → S01 và Save → S03 đã nối, nhưng chọn card chưa tương tác. S04 Back mở overlay; Continue đóng overlay để trở lại S04; xác nhận hủy → S03; link mô phỏng offline → S07. S05 tự chuyển sau 1.3 giây → S06. CTA S06 “Lưu vào nhật ký” → S08. Tại S07, Back/secondary → S04 và Retry → S05; đường đi đã nối nhưng việc giữ dữ liệu sau lỗi chưa được xác minh. CTA S09 → S04; S11 Back/CTA → S10. S06 vẫn không phải xác nhận đã lưu. Các prompt refinement bên trên vẫn là đề xuất tương lai, không phải hành vi hiện có.

Điều hướng tab mới chỉ hoàn tất một phần: ba tab chưa chọn ở S03 có link; trong S08/S09/S10 chỉ tab Home nối về S03; các tab tại S11 chưa được nối. Không ghi rằng mọi tab đều hoạt động. Audit cũng ghi nhận 24 variables (14 màu), 7 Text Styles, 1 Effect Style `Elevation/Level 1`, 164 bound nodes và 174 bound paints. Đây là audit tĩnh qua plugin/API, không phải lượt kiểm thử trực tiếp trong Present.

| Hạng mục | Thao tác/kiểm tra được ghi nhận | Kết quả |
|---|---|---|
| Button | Căn giữa nhãn ngang/dọc; Roboto Medium 16/24; đồng bộ bốn state. | 26 button kiểm tra; lệch tâm còn 0. |
| Card/header | Khớp chiều cao text frame với line-height; title 20/28, body 14/20; chỉnh padding và căn logo giữa vòng tròn. | Card tràn đáy 0; frame thấp hơn một dòng 0. |
| Form | Căn nội dung giữa theo chiều dọc, padding ngang 16 px; thống nhất khoảng nhãn, field và trợ giúp. | Áp dụng vào Final UI, Prototype và home 412 px. |
| Navigation | Đưa vector vào component Navigation Item, căn icon/nhãn cùng trục và chọn đúng variant; bỏ 44 icon rời. | 44 item kiểm tra; lỗi icon/state/tab label còn 0. |
| Loading/empty | Gom icon với vòng nền trong một frame để Auto Layout giữ đồng tâm; căn giữa tiêu đề/mô tả. | Chỉnh sửa được ghi nhận. |
| Dialog/ngày/lỗi | Căn nút chữ phụ, nhãn ngày chart, thao tác hủy; bỏ Retry lặp trong error card; chỉnh khoảng CTA. | Chỉnh sửa được ghi nhận. |
| Hit areas | Tăng 11 secondary actions lên h48; bọc icon Back 40 × 40 trong target 48 × 48; dialog source và cancel actions 48 dp. | Các kích thước được xác nhận trong lượt trước; PNG đã xuất, chưa đo mọi control. |
| Prototype links | Audit reactions, destinations và đích điều hướng. | 32 reactions, 31 destinations, 0 đích thiếu trong `design/figma-audit.json`; các tab điều hướng còn một phần như mô tả phía trên. Audit tĩnh, không phải live Present walkthrough. |
| Font | Rà soát các lớp chữ trong phần đã kiểm tra. | Font thiếu 0; các lớp đã kiểm tra dùng Roboto. |

Snapshot cũ ghi 11 frame grayscale 52:*, dựng hồi cứu từ Final UI ngày 22/10/2026. Metadata mới ghi tổng 22 frame trên Page 02: còn bộ 12:* đặt chồng; xem báo cáo đối chiếu. Bộ 52:* không phải wireframe nguyên gốc trước Final UI và không phải bằng chứng tiền-Stitch.

Review đã xem render của màn chính, dialog hủy, component điều hướng và màn responsive. Renderer/cấu trúc Figma được dùng; kiểm thử trực tiếp trong trình xem Figma bằng Playwright không thực hiện được vì trả HTTP 403. Ảnh cuối và provenance nằm trong [manifest](../assets/figma/manifest.json). Lượt đo ban đầu phát hiện secondary action target 44 dp và icon Back 40 dp; lượt trước đã sửa 11 secondary actions lên 48 dp và bọc Back trong hit area 48 dp. Dialog source/cancel actions cũng đã đạt 48 dp. Cần rà các control còn lại; chưa có hardware, 200% text scaling hay public-sharing checks.

## Rà soát yêu cầu và sắp xếp hồ sơ — 22/10/2026

Codex đọc hai đề PDF/hai hướng dẫn DOCX, đối chiếu tài liệu, kiểm tra ảnh/manifest và đọc metadata trực tiếp bằng Figma MCP. Kết quả nằm ở [bảng đối chiếu](../docs/submission-review.md); [metadata mới](../docs/reviews/figma-metadata-2026-10-22.json) phát hiện 22 wireframe, khác snapshot cũ chỉ ghi 11. Đã chỉnh README, đường dẫn và cấu trúc thư mục, thêm validator; không chạy Stitch, không tạo lịch sử prompt/output giả và không chỉnh Figma trong lượt này. Browser không khởi tạo được, nên quyền xem công khai và Present chưa xác minh.

## Bằng chứng thực tế cần bổ sung sau khi chạy Stitch

| Vòng | Prompt đã gửi nguyên văn | Response AI đầy đủ | Screenshot trước/sau | Phát hiện và quyết định nhóm |
|---|---|---|---|---|
| Khởi đầu | Chưa chạy | Chưa có | Chưa có | Chưa có |
| Lặp 1 | Chưa chạy | Chưa có | Chưa có | Chưa có |
| Lặp 2 | Chưa chạy | Chưa có | Chưa có | Chưa có |
| Lặp 3 | Chưa chạy | Chưa có | Chưa có | Chưa có |

Không thay “chưa có” bằng nội dung suy đoán. Ảnh Figma thuộc assets/figma; ảnh Stitch chỉ được lưu trong assets/stitch sau khi Stitch thật sự được dùng.
