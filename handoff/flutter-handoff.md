# Nếp Lành — Flutter handoff theo 11 frame Figma

Nguồn giao diện: [Figma — Nhóm 6: Ăn gì không chết](https://www.figma.com/design/Cc2O3xSmxgjfvDI2hrsY3Q), trang 03 Final UI. Danh mục frame và đặc tả đầy đủ nằm trong [screen-spec.md](../design/screen-spec.md). Tài liệu này là handoff, không phải mã Flutter. Chưa có kiểm thử Flutter được thực hiện.

## Phạm vi bằng chứng

Final UI gồm 11 frame 360 × 800 dp: **8 màn hình chức năng** (S01–S04, S06, S08, S10–S11) và **3 frame trạng thái** (S05 loading, S07 lỗi kết nối, S09 ngày chưa ghi bữa). Có đủ 11 bản responsive rộng 412 dp trên trang 06, hai bản chọn mục tiêu bổ sung và overlay Final UI `10:126` / Prototype `13:579`; không tính bản responsive, trạng thái hay overlay thành màn chức năng mới. Prototype thuộc trang 06, khác node Final UI. Kết quả mới và phạm vi Present/quyền xem nằm trong [review lượt sửa](../docs/reviews/current-fix-review.md); không dùng số liệu snapshot trước sửa làm số liệu cuối. Liên kết prototype không chứng minh backend, validation chạy thật, lưu trữ bền vững, sync, phân tích dinh dưỡng hay xử lý thông báo.

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
| color/border/control | #526258 | ColorScheme.outline; phân biệt biên field/control với đường phân cách trang trí |
| Error / error container | #A4261D / #F9DEDC | ColorScheme.error / errorContainer |
| Success | #196C46 | ColorScheme.tertiary hoặc custom semantic success; luôn kèm nhãn |
| Accent peach / sky | #F4E4D2 / #E6EEF8 | container phụ, không dùng làm tín hiệu trạng thái duy nhất |
| Spacing | 4, 8, 12, 16, 24, 32 dp | AppSpacing.xs, s, m, l, xl, xxl |
| Radius | 8, 12, 20, pill token 999 dp | BorderRadius.circular(8/12/20); StadiumBorder cho pill |
| Elevation | Figma có Card Level 1 | CardTheme elevation 1; không tự gán số cho dialog nếu chưa xác nhận |

Font là Roboto (không phải Inter). Ánh xạ TextTheme: Display 30/38 → displayLarge; Headline 24/32 → headlineSmall; Title 20/28 → titleLarge; Body 16/24 → bodyLarge; Body Small 14/20 → bodyMedium; Label 14/20 → labelLarge. Dùng Roboto hệ thống hoặc asset Roboto đã đóng gói, kiểm tra dấu tiếng Việt và textScaleFactor.

Primary button trong Figma cao 52 dp, nhãn Roboto Medium 16/24, căn giữa. Item điều hướng là 82 × 68 dp, icon 24 dp; thanh navigation cao 84 dp. App bar Back có Leading wrapper 48 × 48 dp đã được xác nhận trong Figma; vòng tròn hiển thị 40 × 40 dp đặt lệch 4 dp và chứa icon 24 dp. Giữ hit frame 48 dp trong Flutter. Hành động chữ phụ và hành động hủy dialog cũng cao 48 dp.

Audit sau sửa trên 25 frame ở 360/412 dp ghi nhận contrast chữ thấp nhất 5.52:1, nội dung tối thiểu 14 px và mọi vùng bấm được audit đạt ít nhất 48 × 48 dp. Token biên control dùng #526258; chart có viền phân biệt và bản text theo ngày. Đây là kiểm tra thiết kế Figma, không chứng minh khả năng truy cập trên thiết bị. Khi triển khai, giữ chữ thường ≥4.5:1, chữ lớn/điều khiển ≥3:1 và trạng thái có text/icon/hình dạng ngoài màu sắc.

## Component Figma → widget Flutter

| Nhóm component Figma | Variants thấy trong Components | Widget/triển khai Flutter |
|---|---|---|
| Button | Default, Focused, Pressed, Loading, Disabled | FilledButton, OutlinedButton, TextButton; minimumSize 52 dp, WidgetState.pressed và loading label |
| Text Field | Default, Focused, Filled, Error, Disabled | TextFormField + InputDecoration; label, helper/error text, enabled và input actions |
| Card | Default, Selected, Pressed | Card kết hợp InkWell/Selectable semantics; phân biệt pressed với selected |
| Navigation Item | Selected, Unselected | NavigationBar/NavigationDestination; responsive target dùng NavigationRail nếu phù hợp |
| App Bar | Root, Back | AppBar; leading IconButton có constraints/hit target 48 dp |
| Dialog | Open, Confirmed, Destructive | AlertDialog/Dialog, modal barrier, focus management; hành động hủy có nhãn rõ |
| Loading | Processing, Complete | ProcessingPanel với CircularProgressIndicator hoặc status icon + live-region label |
| Empty State | No meals, No results | EmptyStateView riêng, mô tả và CTA rõ ràng |
| Error & Recovery | Offline, Retrying | Inline error card/MaterialBanner, Retry và đường quay lại; không phủ mất dữ liệu |

Giữ variants bằng ThemeData, ButtonStyle, InputDecorationTheme, CardThemeData, NavigationBarThemeData và component wrappers tập trung; không hardcode hex hoặc kích thước tùy từng màn hình.

States bổ sung đã có trong Components: Button Pressed `61:78`; Text Field Filled `61:80` / Disabled `61:85`; Card Pressed `61:90`; Dialog Destructive `61:93`. Focused vẫn là state riêng, không thay cho Pressed. “Primary”, “Tip”, “Highlight”, “No connection” trong mô tả từng màn là vai trò/nội dung UI, không phải tên variant mới. Xem [review sau sửa](../docs/reviews/current-fix-review.md).

## Responsive và accessibility

- Khung chuẩn 360 × 800 dp; trang 06 có đủ S01–S11 ở 412 dp. [Script kiểm tra responsive](../tools/figma/check-responsive-412.js) và review hiện tại ghi phạm vi kiểm tra. Bản Home 412 cũ node `16:164` không còn là bằng chứng responsive duy nhất.
- Từ 600 dp trở lên giữ cột đọc có max width, có thể chia dashboard thành hai cột và dùng navigation rail khi còn đủ chỗ. Đây là hành vi Flutter cần thiết kế/kiểm tra, chưa có bản tablet thực thi.
- Dùng SafeArea và nội dung cuộn tự nhiên. CTA cuối trang phải còn nhìn thấy hoặc cuộn tới được khi bàn phím mở. Không khóa chiều cao của card có text.
- Thiết kế đã được audit cỡ chữ nội dung ≥14 px và vùng bấm ≥48 × 48 dp; Flutter cần giữ ≥14 sp và kiểm thử text scale tới 200%. Back icon có thể vẽ 24 dp nhưng hit frame 48 dp.
- Chart hiện có text “Đã ghi: T2–T6 · Chưa ghi: T7, CN”. Thứ tự đọc top-level đã được sửa và kiểm tra trong browser; khi triển khai vẫn phải kiểm thử semantics, TalkBack/VoiceOver, keyboard focus và reduced motion.
- Menu 4 mục: Trang chủ, Nhật ký, Tiến trình, Học; mọi tab chưa chọn đã có destination. Mục đang chọn có dấu ✓, không chuyển trang khi bấm; Flutter thêm selected semantics tương ứng.

## Bản đồ prototype Figma

Các ID Prototype dưới đây thuộc trang 06 và khác node Final UI tương ứng. Ba native flow starting points ở các launch cards `13:373`, `13:378`, `13:383`. Đây là phản ứng điều hướng được audit, không phải dịch vụ dữ liệu:

- Onboarding: S01 (`13:418`) CTA → S02 (`13:434`, chọn 1). Chọn thẻ chuyển giữa `13:434` / `63:267` / `63:291`; thẻ chọn có ✓ và “Đã chọn”. S02 Back → S01, Save → S03 (`13:447`) với dữ liệu mẫu, không persist lựa chọn.
- Home: CTA → S04 (`13:465`); các tab chưa chọn mở S08 (`13:507`), S10 (`13:534`), S11 (`13:563`). Link “Xem tiến trình tuần” (`13:458`) đã nối tới S10.
- Meal: S04 Back mở overlay `13:579`; CTA → S05 (`13:476`); link mô phỏng lỗi → S07 (`13:497`). S05 timer có giá trị MCP `1.3`, chạy thực khoảng 1,3 giây → S06 (`13:485`); nút “Xem kết quả” (`67:403`) cũng mở S06. Giá trị `1300` trong audit cũ không chạy đúng runtime và đã được sửa. AppBar Back/CTA chỉnh sửa vẫn về S04; không có nhánh S05 → S07.
- Result: S06 AppBar Back và Edit đều → S04; Save → S08.
- Error: S07 Back và “Quay lại món ăn” → S04; Retry → S05. S07 không mở overlay.
- Journal: S08 và S09 có CTA ghi bữa → S04. Link “Xem ngày chưa ghi bữa” (`63:365`) trên S08 mở S09; đây là ngày trống trong bộ dữ liệu mẫu, không phải toàn bộ nhật ký không có dữ liệu.
- Progress/Learn: S10 link đọc → S11. S11 AppBar dùng `BACK` theo nguồn vào (Home hoặc Weekly); CTA cuối bài luôn tới S10. Trên Home/Journal/Empty/Weekly/Article, mọi tab chưa chọn đã nối đúng destination, tab đang chọn là no-op có ✓.
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
- **Component + variant:** AppBar/Back, progress indicator, Card/Default|Selected|Pressed, Button/Default|Pressed.
- **States:** Ba biến thể lựa chọn: mục tiêu 1 (`13:434`), mục tiêu 2 (`63:267`), mục tiêu 3 (`63:291`). Thẻ chọn có ✓ và “Đã chọn”; save-error chưa có frame.
- **Interaction / validation:** Chọn card chuyển tới biến thể tương ứng. Save → S03 dữ liệu mẫu; Flutter cần lưu một lựa chọn thật và đồng bộ Home, không suy từ chuyển frame rằng persistence đã có.
- **Navigation / Back:** Back về S01; Save tới S03.
- **Constraints:** Keyboard không dùng; mỗi card/button có hit target ≥48 dp; không chỉ tô nền để báo selected; từ 600 dp dùng cột giới hạn.

### S03 — Trang chủ · Final UI 6:42 / Prototype 13:447

- **Layout:** AppBar root, greeting/date, goal card, progress line, tip card, CTA ghi bữa, link tiến trình, bottom nav.
- **Component + variant:** AppBar/Root, Card/Goal|Tip, Progress, Button/Primary, TextButton, Navigation/Selected Home.
- **States:** Prototype hiển thị goal và log count mẫu; empty/error/load chưa có frame riêng.
- **Interaction / validation:** CTA → S04; ba tab chưa chọn → S08/S10/S11; link tuần cũng → S10. S09 mở từ link xem ngày chưa ghi trên S08. Flutter chọn dữ liệu/empty state theo ngày thật.
- **Navigation / Back:** Root tab; tab state giữ khi chuyển trang; Back theo hệ điều hành.
- **Constraints:** Có bản 360/412 dp; nav 84 dp, vùng bấm ≥48 dp; chart/progress có mô tả text. ≥600 dp có thể chia card hai cột; không có keyboard.

### S04 — Ghi bữa ăn · Final UI 6:76 / Prototype 13:465

- **Layout:** AppBar Back, heading, tên món input, thời điểm input, ghi chú trợ giúp, CTA Phân tích, offline demo link, disclaimer.
- **Component + variant:** AppBar/Back; Text Field/Filled; library có Default|Focused|Filled|Error|Disabled; Card/Tip; Button/Default|Pressed; TextButton.
- **States:** Fields dùng Filled cho dữ liệu mẫu; chưa có nhập liệu/validation ứng dụng thật.
- **Interaction / validation:** Link demo tới S07; CTA tới S05. Flutter trim và yêu cầu tên món, cho sửa time, không bắt calorie/portion; giữ input khi Back/lỗi.
- **Navigation / Back:** AppBar Back mở overlay 13:579; CTA → S05; offline demo → S07. Trong overlay, Continue đóng về S04 và Confirm → S03.
- **Constraints:** Keyboard văn bản; scroll/resize để field và CTA không bị che. Back hit frame 48 dp với visual circle 40 dp; 600+ form một cột max-width.

### S05 — Đang phân tích · Final UI 6:101 / Prototype 13:476

- **Layout:** AppBar Back, loading title/subtitle, processing card, spinner arc 40 dp, note, action chỉnh sửa và “Xem kết quả”.
- **Component + variant:** AppBar/Back; Loading/Processing; spinner arc; Text/Heading; Button/Default|Pressed.
- **States:** Frame Processing; component set còn Complete. Timer chạy khoảng 1,3 giây tới S06; không có timer/error branch tới S07.
- **Interaction / validation:** Timer MCP `1.3` → S06; fallback “Xem kết quả” → S06. Flutter gắn loading với service thật, bổ sung timeout/error handling và giữ draft.
- **Navigation / Back:** AppBar Back và CTA chỉnh sửa → S04; timer và “Xem kết quả” → S06.
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
- **Interaction / validation:** Retry → S05; AppBar Back và secondary “Quay lại món ăn” → S04. Copy “Quay lại biểu mẫu để kiểm tra thông tin bữa ăn.” không hứa dữ liệu được lưu. Không có overlay từ S07; Flutter retry không tạo duplicate và chỉ nói đã lưu sau local write thành công.
- **Navigation / Back:** Back và secondary → S04; Retry → S05; overlay không thuộc route của S07.
- **Constraints:** Error có text, icon và hành động; không phụ thuộc màu đỏ. Back hit target ≥48 dp; keyboard không dùng; error card không bị tách xa CTA ở màn rộng.

### S08 — Nhật ký bữa ăn · Final UI 6:155 / Prototype 13:507

- **Layout:** AppBar root, ngày, hai card (meal và note), daily summary, nút Ghi thêm, link “Xem ngày chưa ghi bữa”, bottom nav.
- **Component + variant:** AppBar/Root; Card/Meal|Note; Button/Primary; Navigation/Selected Journal.
- **States:** Frame có dữ liệu mẫu; pending sync/error chưa được thể hiện.
- **Interaction / validation:** Home Journal nav và Save result mở S08; Ghi thêm → S04; “Xem ngày chưa ghi bữa” → S09. Chưa có edit/delete trên card. Flutter chỉ hiển thị log tồn tại và cần xác nhận nếu thêm xóa.
- **Navigation / Back:** AppBar root; Home → S03, Progress → S10, Learn → S11; Journal đang chọn có ✓ và không điều hướng.
- **Constraints:** Semantics ngày/giờ và text; không keyboard; list cuộn; ở ≥600 dp có thể đặt summary bên cạnh journal nhưng giữ focus order.

### S09 — Ngày chưa ghi bữa · Final UI 6:186 / Prototype 13:522

- **Layout:** AppBar root, heading “Ngày chưa ghi bữa”, Empty State illustration/message, nút Ghi bữa ăn, bottom nav.
- **Component + variant:** AppBar/Root; Empty State/No meals; Button/Primary; Navigation/Selected Journal.
- **States:** Empty theo ngày trong nhật ký mẫu; không có nghĩa toàn bộ nhật ký chưa từng có bản ghi. Loading/error cần phân biệt riêng trong Flutter.
- **Interaction / validation:** Mở từ link `63:365` trên S08; CTA → S04. Flutter tự chọn trạng thái theo ngày/dữ liệu, không dùng link demo làm logic ứng dụng.
- **Navigation / Back:** AppBar root; Home → S03, Progress → S10, Learn → S11; Journal selected no-op có ✓. Sau local commit thật, Flutter route tới nhật ký dữ liệu tương ứng.
- **Constraints:** Empty copy và CTA có semantics; illustration không phải nội dung duy nhất; không keyboard; vùng rỗng co giãn, không làm CTA mất tầm với.

### S10 — Tiến trình tuần · Final UI 6:213 / Prototype 13:534

- **Layout:** AppBar root, Week heading, goal card, caption, 7-day bar chart, highlight card, learn link, bottom nav.
- **Component + variant:** AppBar/Root; Card/Goal|Highlight; Accessible weekly chart; TextButton; Navigation/Selected Progress.
- **States:** Figma có mẫu 5/7 và cột theo ngày; no-data/error chưa có frame.
- **Interaction / validation:** Prototype link mở S11. Flutter tính từ log thực; ưu tiên “đã ghi nhận 5 ngày tuần này” thay streak nếu cần ngôn ngữ trung tính; không cho tuần tương lai nếu thêm selector.
- **Navigation / Back:** Vào từ Home tab Progress hoặc link tuần; link đọc → S11; Home → S03, Journal → S08, Learn → S11; Progress selected no-op có ✓.
- **Constraints:** Chart có viền, label và text “Đã ghi: T2–T6 · Chưa ghi: T7, CN”; không chỉ dùng màu/cao thấp; không keyboard; giữ đọc được ở 360/412 dp, hai cột tại ≥600 nếu phù hợp.

### S11 — Bài học nhỏ · Final UI 6:257 / Prototype 13:563

- **Layout:** AppBar Back, thời lượng 3 phút, title, hai đoạn, action prompt card, source/disclaimer, Mark as read button, bottom nav.
- **Component + variant:** AppBar/Back; Text/Article; Card/Action prompt; source/disclaimer; Button/Primary; Navigation/Selected Learn.
- **States:** Figma bài chưa đọc; đã đọc/loading/error chưa có frame.
- **Interaction / validation:** Prototype Mark as read minh họa hoàn tất; Flutter chỉ đánh dấu local sau khi lưu state. Nội dung diễn giải và trích dẫn nguồn, không sao chép dài từ sách hay đưa khuyến nghị điều trị.
- **Navigation / Back:** AppBar dùng `BACK` theo nguồn vào: vào từ Home thì về Home, từ Weekly thì về Weekly. CTA cuối bài vẫn → S10. Home/Journal/Progress tabs → S03/S08/S10; Learn selected no-op có ✓.
- **Constraints:** Cuộn, Roboto text scale, line height thoáng, link nguồn gạch chân; keyboard không dùng; cột đọc tối đa khoảng 720 dp ở màn rộng; Back target ≥48 dp.

### Overlay hủy ghi bữa · Final UI 10:126 / Prototype 13:579

- **Layout:** Scrim và dialog 320×252 dp ở giữa, title/body, “Tiếp tục chỉnh sửa” và “Hủy bữa ăn”.
- **Component + variant:** Dialog/Open|Confirmed|Destructive; variant Destructive `61:93`; Button/Secondary và destructive TextButton.
- **States:** Closed, Open, dismissed, confirmed.
- **Interaction / validation:** Figma Continue đóng overlay để trở lại form mẫu; confirm → S03. Flutter phải giữ draft khi dismiss và chỉ xóa sau xác nhận; chuyển frame mẫu không chứng minh đã có lưu/xóa draft thật.
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

- Đặc tả cập nhật theo thao tác MCP và kết quả audit sau sửa; phạm vi Present/quyền công khai và bằng chứng cuối nằm trong [review lượt sửa](../docs/reviews/current-fix-review.md). Không đồng nhất audit cấu trúc với walkthrough.
- QA đã đạt ba flow, ba lựa chọn mục tiêu, 15 tab chưa chọn, retry, overlay, empty và Back theo nguồn vào. Present mở được khi không đăng nhập; editor trả CloudFront 403 nên chưa xác minh quyền truy cập editor. Audit cuối có 95 reactions, 92 destinations, không có đích thiếu hoặc vùng bấm thiếu kích thước trong phạm vi audit.
- Tài liệu không tuyên bố đã có Flutter app hoặc đã chạy test Flutter.
- Thiết kế đã audit 360/412 dp, cỡ chữ, contrast, vùng chạm và thứ tự đọc top-level. Khi triển khai Flutter vẫn cần kiểm tra ≥600 dp, keyboard, text scale 200%, screen reader, focus, reduced motion, local database recovery và retry idempotent trên thiết bị.
