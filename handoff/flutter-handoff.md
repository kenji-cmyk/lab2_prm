# Nếp Lành — Flutter handoff theo 11 frame Figma

Nguồn giao diện: [Figma — Nhóm 6: Ăn gì không chết](https://www.figma.com/design/Cc2O3xSmxgjfvDI2hrsY3Q), trang 03 Final UI. Danh mục frame và đặc tả đầy đủ nằm trong [screen-spec.md](../design/screen-spec.md). Tài liệu này là handoff, không phải mã Flutter. Chưa có kiểm thử Flutter được thực hiện.

## Phạm vi bằng chứng

Final UI gồm 11 frame 360 × 800 dp: **8 màn hình chức năng** (S01–S04, S06, S08, S10–S11) và **3 frame trạng thái** (S05 loading, S07 lỗi kết nối, S09 nhật ký trống). Có biến thể Home rộng 412 dp (node 16:164) và overlay Final UI 10:126; overlay không tính là màn hình. Prototype là các frame riêng ở trang 06 (node 13:*). Không trộn ID của hai trang. Audit JSON ghi 32 reactions, 31 đích hợp lệ, không có đích thiếu; 24 variables, 7 local text styles, 1 effect style (Elevation/Level 1), 164 bound nodes và 174 bound paints. Đây là audit tĩnh, không phải walkthrough live. Liên kết prototype không chứng minh đã có backend, validation chạy thật, lưu trữ bền vững, sync, phân tích dinh dưỡng hay xử lý thông báo.

Trong Flutter, dùng cùng route để trình diễn flow; xây validation, lưu draft, offline recovery và persistence như công việc ứng dụng riêng. Không báo “đã lưu”, “đã đồng bộ” hoặc “đã phân tích” nếu service/local transaction tương ứng chưa thành công.

## Token → Flutter

| Token Figma | Giá trị | Ánh xạ gợi ý |
|---|---|---|
| Brand primary | #2F6B4F | ColorScheme.primary; FilledButton và trạng thái chọn |
| On primary | #FFFFFF | ColorScheme.onPrimary |
| Primary container | #E1F1E6 | ColorScheme.primaryContainer |
| On container | #183D2D | ColorScheme.onPrimaryContainer |
| Canvas | #F7F8F4 | scaffoldBackgroundColor |
| Surface | #FFFFFF | ColorScheme.surface; Card/dialog |
| Text primary | #1F2B24 | ColorScheme.onSurface |
| Text secondary | #526258 | ColorScheme.onSurfaceVariant |
| Border | #D6DFD7 | ColorScheme.outlineVariant |
| Error / error container | #A4261D / #F9DEDC | ColorScheme.error / errorContainer |
| Success | #196C46 | ColorScheme.tertiary hoặc custom semantic success; luôn kèm nhãn |
| Accent peach / sky | #F4E4D2 / #E6EEF8 | container phụ, không dùng làm tín hiệu trạng thái duy nhất |
| Spacing | 4, 8, 12, 16, 24, 32 dp | AppSpacing.xs, s, m, l, xl, xxl |
| Radius | 8, 12, 20, pill token 999 dp | BorderRadius.circular(8/12/20); StadiumBorder cho pill |
| Elevation | Figma có Card Level 1 | CardTheme elevation 1; không tự gán số cho dialog nếu chưa xác nhận |

Font là Roboto (không phải Inter). Ánh xạ TextTheme: Display 30/38 → displayLarge; Headline 24/32 → headlineSmall; Title 20/28 → titleLarge; Body 16/24 → bodyLarge; Body Small 14/20 → bodyMedium; Label 14/20 → labelLarge. Dùng Roboto hệ thống hoặc asset Roboto đã đóng gói, kiểm tra dấu tiếng Việt và textScaleFactor.

Primary button trong Figma cao 52 dp, nhãn Roboto Medium 16/24, căn giữa. Item điều hướng là 82 × 68 dp, icon 24 dp; thanh navigation cao 84 dp. App bar Back có Leading wrapper 48 × 48 dp đã được xác nhận trong Figma; vòng tròn hiển thị 40 × 40 dp đặt lệch 4 dp và chứa icon 24 dp. Giữ hit frame 48 dp trong Flutter. Hành động chữ phụ và hành động hủy dialog cũng cao 48 dp.

Figma Design System ghi contrast trắng/primary 6.29:1, secondary/white 6.47:1, text-primary/canvas 13.77:1 và error/error-container 5.75:1. Đây là giá trị của swatch, chưa phải kết quả đo tất cả nội dung từng frame. Dùng chữ thường ≥4.5:1, chữ lớn/điều khiển ≥3:1; trạng thái có text/icon/hình dạng, không chỉ đổi màu.

## Component Figma → widget Flutter

| Nhóm component Figma | Variants thấy trong Components | Widget/triển khai Flutter |
|---|---|---|
| Button | Default, Focused, Loading, Disabled | FilledButton, OutlinedButton, TextButton; custom minimumSize 52 dp và loading label |
| Text Field | Default, Focused, Error | TextFormField + InputDecoration; label, helper/error text, input actions |
| Card | Default, Selected | Card kết hợp InkWell/Selectable semantics; variant qua state |
| Navigation Item | Selected, Unselected | NavigationBar/NavigationDestination; responsive target dùng NavigationRail nếu phù hợp |
| App Bar | Root, Back | AppBar; leading IconButton có constraints/hit target 48 dp |
| Dialog | Open, Confirmed; chưa có destructive/error variant riêng | AlertDialog/Dialog, modal barrier, focus management và semantics |
| Loading | Processing, Complete | ProcessingPanel với CircularProgressIndicator hoặc status icon + live-region label |
| Empty State | No meals, No results | EmptyStateView riêng, mô tả và CTA rõ ràng |
| Error & Recovery | Offline, Retrying | Inline error card/MaterialBanner, Retry và đường quay lại; không phủ mất dữ liệu |

Giữ variants bằng ThemeData, ButtonStyle, InputDecorationTheme, CardThemeData, NavigationBarThemeData và component wrappers tập trung; không hardcode hex hoặc kích thước tùy từng màn hình.

Inventory này mô tả component hiện có, chưa xác nhận đủ states theo đề. Còn thiếu Button/Pressed, Text Field/Filled và Disabled; Card/Pressed khi tappable; Dialog destructive/error cần làm rõ. “Primary”, “Tip”, “Highlight”, “No connection” trong mô tả từng màn là vai trò/nội dung UI, không phải tên variant đã xác minh. Xem [đối chiếu chi tiết](../docs/submission-review.md).

## Responsive và accessibility

- Khung chuẩn 360 × 800 dp; Home responsive ở 412 dp có frame node 16:164. Không suy diễn rằng các frame khác đã được kiểm tra ở 412 dp.
- Từ 600 dp trở lên giữ cột đọc có max width, có thể chia dashboard thành hai cột và dùng navigation rail khi còn đủ chỗ. Đây là hành vi Flutter cần thiết kế/kiểm tra, trừ frame 412 dp đã nêu.
- Dùng SafeArea và nội dung cuộn tự nhiên. CTA cuối trang phải còn nhìn thấy hoặc cuộn tới được khi bàn phím mở. Không khóa chiều cao của card có text.
- Tối thiểu 14 sp cho nội dung; text scale tới 200%; tap target tối thiểu 48 × 48 dp. Back icon có thể vẽ 24 dp nhưng hit frame 48 dp.
- Chart phải có summary đọc được; ngày, trạng thái đã chọn, loading, lỗi và sync đều có nhãn semantics. Hỗ trợ TalkBack/VoiceOver, keyboard focus, reduced motion và thứ tự focus theo thứ tự đọc.
- Bản Figma hiện có menu 4 mục: Trang chủ, Nhật ký, Tiến trình, Học. Mục đang chọn phải biểu đạt bằng cả icon, nhãn và state semantics.

## Bản đồ prototype Figma

Các ID Prototype dưới đây thuộc trang 06 và khác node Final UI tương ứng. Đây là phản ứng điều hướng được audit, không phải dịch vụ dữ liệu:

- Onboarding: S01 (13:418) CTA → S02 (13:434); S02 Back → S01, Save → S03 (13:447). Ba thẻ mục tiêu S02 không có reaction chọn card; phần tô chọn là hình ảnh tĩnh.
- Home: CTA → S04 (13:465); ba nav item chưa chọn mở Journal S08 (13:507), Progress S10 (13:534), Learn S11 (13:563). Text link “Xem tiến trình tuần” nhìn thấy trên Home không có reaction; dùng tab Progress để vào S10 trong flow.
- Meal: S04 AppBar Back mở overlay Prototype 13:579; CTA → S05 (13:476); link mô phỏng lỗi → S07 (13:497). S05 chỉ có timer 1300 ms → S06 (13:485), cùng AppBar Back/CTA sửa → S04. Không có nhánh S05 → S07 trong prototype.
- Result: S06 AppBar Back và Edit đều → S04; Save → S08.
- Error: S07 Back và “Quay lại món ăn” → S04; Retry → S05. S07 không mở overlay.
- Journal: S08 và S09 đều có CTA ghi bữa → S04, cùng nav Home → S03. Nav Journal trên Home mở S08; S09 là frame trạng thái được trình bày thủ công, không được chọn tự động khi nhật ký rỗng.
- Progress/Learn: S10 link đọc → S11, nav Home → S03. S11 Back và primary CTA đều → S10; S11 không có reaction cho bottom-nav items.
- Overlay: Final UI 10:126, Prototype 13:579. “Tiếp tục chỉnh sửa” dùng CLOSE để lộ lại S04 phía dưới; “Hủy bữa ăn” → S03. Overlay chỉ mở từ AppBar Back của S04.

## Handoff theo frame (8 màn hình chức năng + 3 trạng thái)

Mỗi màn hình có đủ sáu mục. “Figma” mô tả frame/route trình diễn; “Flutter” ghi hành vi cần xây nếu triển khai sản phẩm.

### S01 — Chào mừng · Final UI 6:2 / Prototype 13:418

- **Layout:** Status bar, brand mark, hero illustration, heading/body, nút Thiết lập mục tiêu và disclaimer.
- **Component + variant:** Brand, Hero panel, Display/Body, Button/Primary/Default.
- **States:** Figma default; không có form, loading hoặc lỗi riêng.
- **Interaction / validation:** Prototype CTA tới S02; không có field validation. Flutter không yêu cầu dữ liệu cá nhân để tiếp tục.
- **Navigation / Back:** Điểm vào; Back hệ thống theo hành vi thoát nền tảng; CTA mở S02.
- **Constraints:** Không có keyboard; disclaimer đọc được; button 52 dp. 412+ giữ thứ tự hero → heading → CTA; từ 600 dp giới hạn cột, không kéo dài dòng.

### S02 — Thiết lập mục tiêu · Final UI 6:19 / Prototype 13:434

- **Layout:** AppBar Back, bước 1/2, câu hỏi, 3 goal cards, Save goal, note.
- **Component + variant:** AppBar/Back, progress indicator, Card/Default|Selected, Button/Primary.
- **States:** Frame tô nền thẻ đầu; hai thẻ kia nền thường. Audit không thấy reaction chọn card, nên trạng thái chọn là tĩnh trong Prototype; save-error không được thể hiện.
- **Interaction / validation:** Prototype chỉ có Back → S01 và Save → S03; không có tương tác chọn card. Flutter có thể bổ sung chọn một mục tiêu theo thiết kế và cần lưu/validate thật; hành vi này chưa được wiring trong Figma.
- **Navigation / Back:** Back về S01; Save tới S03.
- **Constraints:** Keyboard không dùng; mỗi card/button có hit target ≥48 dp; không chỉ tô nền để báo selected; từ 600 dp dùng cột giới hạn.

### S03 — Trang chủ · Final UI 6:42 / Prototype 13:447

- **Layout:** AppBar root, greeting/date, goal card, progress line, tip card, CTA ghi bữa, link tiến trình, bottom nav.
- **Component + variant:** AppBar/Root, Card/Goal|Tip, Progress, Button/Primary, TextButton, Navigation/Selected Home.
- **States:** Prototype hiển thị goal và log count mẫu; empty/error/load chưa có frame riêng.
- **Interaction / validation:** Prototype CTA → S04; ba nav item chưa chọn → S08/S10/S11. Text link tuần không có reaction. Nhật ký S09 được mở thủ công để trình bày state; Flutter có thể route tới empty state theo dữ liệu thật.
- **Navigation / Back:** Root tab; tab state giữ khi chuyển trang; Back theo hệ điều hành.
- **Constraints:** 360 dp và biến thể Home 412 dp node 16:164; nav 84 dp, item 82×68 dp; chart/progress có mô tả text. ≥600 dp có thể chia card hai cột; không có keyboard.

### S04 — Ghi bữa ăn · Final UI 6:76 / Prototype 13:465

- **Layout:** AppBar Back, heading, tên món input, thời điểm input, ghi chú trợ giúp, CTA Phân tích, offline demo link, disclaimer.
- **Component + variant:** AppBar/Back; Text Field/Default|Focused|Error; Card/Tip; Button/Primary; TextButton.
- **States:** Figma có giá trị mẫu trong field; component library có default/focus/error.
- **Interaction / validation:** Link demo tới S07; CTA tới S05. Flutter trim và yêu cầu tên món, cho sửa time, không bắt calorie/portion; giữ input khi Back/lỗi.
- **Navigation / Back:** AppBar Back mở overlay 13:579; CTA → S05; offline demo → S07. Trong overlay, Continue đóng về S04 và Confirm → S03.
- **Constraints:** Keyboard văn bản; scroll/resize để field và CTA không bị che. Back hit frame 48 dp với visual circle 40 dp; 600+ form một cột max-width.

### S05 — Đang phân tích · Final UI 6:101 / Prototype 13:476

- **Layout:** AppBar Back, loading title/subtitle, processing card, note, action quay lại chỉnh sửa.
- **Component + variant:** AppBar/Back; Loading/Processing; Text/Heading; Button/Primary.
- **States:** Frame Processing; component set còn Complete. Timer Prototype 1300 ms đi S06; không có timer/error branch tới S07.
- **Interaction / validation:** Prototype sau 1300 ms → S06. Flutter có thể thêm timeout/error handling riêng và giữ draft; không xem nhánh đó là interaction Figma hiện có.
- **Navigation / Back:** AppBar Back và CTA chỉnh sửa → S04; timer → S06.
- **Constraints:** Không keyboard; spinner có semantic label và giảm chuyển động; CTA/back không bị khóa. Hit frame Back ≥48 dp; cột loading giữ max-width ở màn rộng.

### S06 — Kết quả · Final UI 6:118 / Prototype 13:485

- **Layout:** AppBar Back, label tham khảo, title, meal summary, highlight card, next suggestion card, save CTA, edit link, disclaimer.
- **Component + variant:** AppBar/Back; Card/Highlight|Suggestion; Button/Primary; TextButton/Edit; disclaimer.
- **States:** Figma hiển thị kết quả mẫu; chưa có result-empty/error variant.
- **Interaction / validation:** Prototype save CTA mở S08, edit về S04. Flutter ghi vào journal chỉ sau commit local thành công; nội dung phải có nguồn/biên tập, không có claim y khoa.
- **Navigation / Back:** AppBar Back và Edit đều → S04; Save → S08.
- **Constraints:** Không keyboard; text scale, line wrapping và disclaimer; Back hit frame ≥48 dp; ≥600 dp có thể bố trí hai card cạnh nhau, CTA theo thứ tự focus.

### S07 — Lỗi kết nối · Final UI 6:138 / Prototype 13:497

- **Layout:** AppBar Back, offline heading/copy, Error & Recovery card, Retry, link về món ăn, privacy note.
- **Component + variant:** AppBar/Back; Error & Recovery/No connection|Retrying; Button/Primary; TextButton.
- **States:** Frame No connection; component có Retrying; retry success route quay S05.
- **Interaction / validation:** Prototype Retry → S05; AppBar Back và secondary “Quay lại món ăn” → S04. Không có action mở overlay từ S07. Flutter retry không tạo duplicate; nói “đã lưu trên thiết bị” chỉ khi local write thành công.
- **Navigation / Back:** Back và secondary → S04; Retry → S05; overlay không thuộc route của S07.
- **Constraints:** Error có text, icon và hành động; không phụ thuộc màu đỏ. Back hit target ≥48 dp; keyboard không dùng; error card không bị tách xa CTA ở màn rộng.

### S08 — Nhật ký bữa ăn · Final UI 6:155 / Prototype 13:507

- **Layout:** AppBar root, ngày, hai card (meal và note), daily summary, nút Ghi thêm, bottom nav.
- **Component + variant:** AppBar/Root; Card/Meal|Note; Button/Primary; Navigation/Selected Journal.
- **States:** Frame có dữ liệu mẫu; pending sync/error chưa được thể hiện.
- **Interaction / validation:** Prototype Home Journal nav và Save result đều mở S08; nút Ghi thêm → S04. Figma không cho thấy action edit/delete trên card. Flutter chỉ hiển thị log đã tồn tại; thao tác edit/delete phải có semantics/xác nhận nếu được bổ sung.
- **Navigation / Back:** AppBar root; trong các nav reaction được audit, chỉ Home tab → S03. Hành vi các tab khác là phần Flutter cần xây nếu muốn.
- **Constraints:** Semantics ngày/giờ và text; không keyboard; list cuộn; ở ≥600 dp có thể đặt summary bên cạnh journal nhưng giữ focus order.

### S09 — Nhật ký trống · Final UI 6:186 / Prototype 13:522

- **Layout:** AppBar root, Hôm nay heading, Empty State illustration/message, nút Ghi bữa ăn, bottom nav.
- **Component + variant:** AppBar/Root; Empty State/No meals; Button/Primary; Navigation/Selected Journal.
- **States:** Figma empty; loading/error cần phân biệt riêng trong Flutter.
- **Interaction / validation:** CTA → S04; audit chỉ ghi reaction nav Home → S03. Prototype không tự điều hướng tới S09 khi journal rỗng; đây là state frame mở thủ công.
- **Navigation / Back:** AppBar root; Home tab → S03. Sau khi log lưu, route tới S08 là hành vi Flutter mục tiêu.
- **Constraints:** Empty copy và CTA có semantics; illustration không phải nội dung duy nhất; không keyboard; vùng rỗng co giãn, không làm CTA mất tầm với.

### S10 — Tiến trình tuần · Final UI 6:213 / Prototype 13:534

- **Layout:** AppBar root, Week heading, goal card, caption, 7-day bar chart, highlight card, learn link, bottom nav.
- **Component + variant:** AppBar/Root; Card/Goal|Highlight; Accessible weekly chart; TextButton; Navigation/Selected Progress.
- **States:** Figma có mẫu 5/7 và cột theo ngày; no-data/error chưa có frame.
- **Interaction / validation:** Prototype link mở S11. Flutter tính từ log thực; ưu tiên “đã ghi nhận 5 ngày tuần này” thay streak nếu cần ngôn ngữ trung tính; không cho tuần tương lai nếu thêm selector.
- **Navigation / Back:** Prototype entry từ Home Progress nav; link S11; nav Home → S03. Hành vi nav khác cần wiring riêng.
- **Constraints:** Chart có text summary và label từng ngày; không chỉ dùng màu/cao thấp; không keyboard; chart labels giữ đọc được ở 360 dp, hai cột tại ≥600 nếu phù hợp.

### S11 — Bài học nhỏ · Final UI 6:257 / Prototype 13:563

- **Layout:** AppBar Back, thời lượng 3 phút, title, hai đoạn, action prompt card, source/disclaimer, Mark as read button, bottom nav.
- **Component + variant:** AppBar/Back; Text/Article; Card/Action prompt; source/disclaimer; Button/Primary; Navigation/Selected Learn.
- **States:** Figma bài chưa đọc; đã đọc/loading/error chưa có frame.
- **Interaction / validation:** Prototype Mark as read minh họa hoàn tất; Flutter chỉ đánh dấu local sau khi lưu state. Nội dung diễn giải và trích dẫn nguồn, không sao chép dài từ sách hay đưa khuyến nghị điều trị.
- **Navigation / Back:** Prototype Back và primary CTA đều cố định về S10; S11 còn mở trực tiếp từ Home Learn nav. Bottom-nav items trên S11 không có reaction được audit.
- **Constraints:** Cuộn, Roboto text scale, line height thoáng, link nguồn gạch chân; keyboard không dùng; cột đọc tối đa khoảng 720 dp ở màn rộng; Back target ≥48 dp.

### Overlay hủy ghi bữa · Final UI 10:126 / Prototype 13:579

- **Layout:** Scrim và dialog 320×252 dp ở giữa, title/body, “Tiếp tục chỉnh sửa” và “Hủy bữa ăn”.
- **Component + variant:** Dialog/Open|Confirmed; Button/Secondary; destructive TextButton.
- **States:** Closed, Open, dismissed, confirmed.
- **Interaction / validation:** Continue đóng mà giữ dữ liệu; confirm hủy bỏ draft theo ý người dùng. Không xóa draft khi tap ngoài hoặc Back nếu không có xác nhận rõ.
- **Navigation / Back:** Chỉ được gọi từ AppBar Back của S04; dismiss/CLOSE lộ lại S04; confirm → S03.
- **Constraints:** Modal semantics, focus trap/restore, Back/Escape hợp lý; hit target mỗi action ≥48 dp; max width khoảng 320–400 dp trên màn lớn.

## Validation, log thiếu và offline recovery cần triển khai

Đây là hợp đồng hành vi mục tiêu cho Flutter, không phải tính năng đã tồn tại trong prototype:

1. Tạo draft ID khi bắt đầu nhập ở S04; lưu local tên món, thời điểm và ghi chú sau chỉnh sửa. Giữ draft khi đi qua các trạng thái chờ/lỗi hoặc ứng dụng bị đóng giữa luồng. Prototype hiện tại có nhánh S04 → S07 riêng và S04 → S05 → S06; nếu dịch vụ thật phát lỗi trong S05 thì Flutter có thể thêm chuyển S05 → S07 như hành vi mới.
2. Khi người dùng lưu từ S06, tạo/tái sử dụng một log ID ổn định, commit vào kho local rồi mới hiện trạng thái đã lưu; hàng đợi sync dùng cùng ID làm idempotency key. Double tap/retry không sinh duplicate.
3. Offline: nếu local commit thành công, hiện “Đã lưu trên thiết bị — chờ đồng bộ” trong S08 và cho sync retry sau; nếu chưa commit, nói “Bản nháp còn trên thiết bị” thay vì “Đã lưu”. Giữ dữ liệu qua lỗi mạng.
4. Log không thấy khi mở Nhật ký: query local theo ID trước. Nếu log tồn tại nhưng chưa sync, hiện rõ trạng thái pending. Nếu log không tồn tại nhưng draft còn, khôi phục draft và cho lưu lại bằng ID cũ. Nếu cả hai mất, hiện lỗi có hành động nhập lại; không bịa bản ghi hoặc báo thành công.
5. Nếu retry server không xác định được kết quả, tra lại theo cùng ID trước khi gửi lần nữa. Nếu local storage lỗi, giữ form state trong route, cho thử lưu local lại; không xóa route state.
6. Khi xác nhận hủy ở overlay, xóa draft chỉ sau confirm. Khi sửa/xóa log đã lưu, yêu cầu xác nhận và cập nhật sync queue theo cùng ID.

## Mức độ xác minh

- Đặc tả này đối chiếu design/figma-audit.json, metadata và ảnh render Figma của Final UI, Design System và Components. Audit là tĩnh, không phải live Present walkthrough.
- Tài liệu không tuyên bố đã có Flutter app hoặc đã chạy test Flutter.
- Kiểm tra còn cần làm khi triển khai: 360/412 và ≥600 dp, keyboard, text scale, screen reader, focus, tap target Back sau wrapper 48 dp, local database recovery và retry idempotent.
