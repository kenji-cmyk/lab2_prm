# Nếp Lành — AI design log

Ngày cập nhật: **22/10/2026**. File thiết kế: [Nếp Lành — Figma](https://www.figma.com/design/Cc2O3xSmxgjfvDI2hrsY3Q).

## Công cụ và cách khai báo

Theo yêu cầu mới của người thực hiện bài, quy trình được ghi nhận là **Codex đọc tài liệu → thiết kế/chỉnh sửa bằng Figma MCP → phản biện → tinh chỉnh → prototype → handoff**. Google Stitch không được sử dụng. Không có output, ảnh hay lịch sử ba vòng lặp Stitch; các prompt chuẩn bị trước đây chưa được gửi và đã được bỏ khỏi log để tránh nhầm với lịch sử thực tế.

Đề gốc yêu cầu Google Stitch và ít nhất ba vòng lặp có bằng chứng trước/sau; **việc dùng Codex kết nối Figma MCP để thay thế cần được giảng viên chấp thuận**, hiện repository chưa có xác nhận đó. Thay cách mô tả công cụ không tự chứng minh đã đáp ứng tiêu chí công cụ hoặc số vòng lặp.

| Công cụ | Vai trò và giới hạn |
| --- | --- |
| Codex | Đọc yêu cầu, persona và thiết kế hiện có; phân tích vấn đề UX; soạn tài liệu, đề xuất và thực hiện sửa theo yêu cầu. |
| Figma MCP | Kết nối file Figma để đọc metadata/cấu trúc, thao tác thiết kế và lấy bằng chứng từ file. Kết quả cụ thể của lượt sửa này được ghi trong review hiện tại. |
| Figma | Lưu wireframe, Final UI, design system, components và prototype. Ảnh export nằm trong `assets/figma`, không được gắn nhãn Stitch. |
| Công cụ kiểm tra repository | Kiểm tra cấu trúc, đường dẫn và manifest ảnh; không thay thế kiểm thử tương tác hoặc accessibility thực tế. |

## Tài liệu được đọc trước khi chỉnh thiết kế

Các tài liệu sau là đầu vào đã đọc cho việc phân tích và sửa hiện tại:

| Tài liệu | Nội dung dùng để thiết kế/kiểm tra |
| --- | --- |
| [Tóm tắt đề và hướng dẫn](../docs/requirements/summary.md) | Quy trình, 6 trang Figma, 8 màn chức năng, 3 flow, states bắt buộc, contrast/hit area/type size và handoff. Tóm tắt dẫn nguồn hai đề PDF và hai hướng dẫn DOCX trong thư mục requirements. |
| [Persona](../ux/persona.md) | Minh là persona giả định; cần thao tác ngắn, ngôn ngữ trung tính, lỗi có đường phục hồi và nội dung giáo dục. Chưa có nghiên cứu thực địa xác nhận persona. |
| [User flows](../ux/user-flow.md) | Inventory S01–S11, ánh xạ Final UI/Prototype, ba flow và các hạn chế trong snapshot trước sửa. |
| [Design brief](../design/DESIGN.md) | Palette, typography, spacing, radius, phạm vi sản phẩm và giới hạn nội dung. |
| [Đối chiếu yêu cầu](../docs/submission-review.md) | States còn thiếu, wireframe chồng, tương tác chưa nối và các kiểm tra còn mở ở thời điểm audit. |
| [Review căn chỉnh trước](../docs/reviews/figma-alignment.md) | Các chỉnh sửa được ghi nhận trước đây và giới hạn của renderer/audit tĩnh. |
| [Bằng chứng Figma đã xuất](../assets/figma/README.md) | Phân biệt ảnh UI, trạng thái, overlay, responsive và snapshot wireframe. |

Không suy ra rằng toàn bộ tài liệu được viết trước bản thiết kế đầu tiên; nguồn gốc và giới hạn lịch sử được ghi riêng bên dưới.

## Prompt thực tế của lượt sửa hiện tại

Nguyên văn yêu cầu người dùng đã gửi:

~~~text
- Một số component states, liên kết prototype; Wireframe có hai bộ chồng nhau.
- Kiểm tra accessibility, Figma Present và quyền xem công khai.


sửa cho tôi 2 lỗi này, còn bằng chứng stitch, 3 vòng lặp sẽ thay bằng viết sử dụng codex liên kết với mcp của figma, đọc tài liệu rồi sau đó bắt đầu design
~~~

Đây là prompt sửa thực tế trong phiên hiện tại, không phải prompt tạo giao diện đầu tiên. Không có bản ghi nguyên văn prompt tạo thiết kế đầu tiên hoặc toàn bộ phản hồi AI lịch sử đủ để khôi phục chuỗi generate/refine ban đầu; log không dựng lại chúng bằng nội dung suy đoán.

## Quy trình của lượt hiện tại

Lượt này tập trung sửa thiết kế và xác minh những vấn đề đã được audit. Kết quả, node, số liệu và bằng chứng mới được tập hợp tại [review lượt sửa hiện tại](../docs/reviews/current-fix-review.md). Chỉ những thao tác và phép kiểm tra được review đó xác nhận mới được xem là đã hoàn thành.

| Bước | Cách thực hiện và tiêu chí | Trạng thái ghi nhận |
| --- | --- | --- |
| Analyze | Đọc đầu vào; đối chiếu states và ba flow với file Figma, phân biệt lỗi quan sát được với giới hạn chưa kiểm thử. | Đã đọc tài liệu và xác định phạm vi; baseline nằm trong review đối chiếu. |
| Design qua MCP | Bổ sung variants; sửa lựa chọn mục tiêu, điều hướng, empty state, loading/lỗi và wireframe. | Đã thực hiện các sửa thiết kế nêu bên dưới; giữ 11 wireframe chính, xóa đúng 11 frame trùng và xếp grid không chồng. |
| Critique | Đối chiếu UI thật với persona, Nielsen và accessibility: phản hồi trạng thái, consistency, Back, error recovery, contrast, kích thước chạm, cỡ chữ và ý nghĩa ngoài màu sắc. | Đã rà baseline và audit sau sửa; 25 frame 360/412 có contrast chữ thấp nhất 5.52:1, body ≥14 px và vùng bấm được audit ≥48 dp. |
| Refine | Chấp nhận sửa các vấn đề baseline, điều chỉnh nội dung theo giới hạn prototype, truy vết tới node và tài liệu. | Đã bổ sung states và sửa hành vi theo bảng kết quả bên dưới; không gán lượt này thành ba vòng lặp lịch sử. |
| Prototype | Kiểm tra đích, starting points, Back, overlay, loading → result và retry; chạy Present và kiểm tra truy cập công khai. | QA đạt ba flow, ba lựa chọn mục tiêu, 15 tab chưa chọn, retry, overlay, empty và Back theo ngữ cảnh. Present không đăng nhập truy cập được; trang editor trả CloudFront 403 nên quyền editor chưa xác minh. |
| Handoff | Đồng bộ tài liệu với variants, hành vi và kết quả thật; giữ rõ giới hạn prototype, dữ liệu mẫu và lưu trữ. | Đã cập nhật flow, handoff và kịch bản demo; chưa có Flutter app hoặc kiểm thử ứng dụng trên thiết bị. |

## Phản biện baseline và quyết định sửa

Nguồn quan sát là [đối chiếu trước sửa](../docs/submission-review.md) và [metadata ngày 22/10](../docs/reviews/figma-metadata-2026-10-22.json). Đây là bản tổng hợp phát hiện audit thực tế, không phải toàn bộ phản hồi của một prompt critique lịch sử đã thất lạc.

| Phát hiện cụ thể trước sửa | Căn cứ UX / accessibility | Quyết định cho lượt hiện tại và lý do | Cách xác minh sau sửa |
| --- | --- | --- | --- |
| S02 Goal: thẻ mục tiêu tĩnh, trong khi CTA ghi lưu mục tiêu. | Visibility of system status; persona cần tự chọn và nhận phản hồi rõ. | Chấp nhận sửa tương tác và biểu thị lựa chọn để hành động lưu có nghĩa trong prototype. | Chọn thẻ, kiểm tra dấu hiệu selected ngoài màu sắc và đường tiếp tục/Back. |
| S03 Home: “Xem tiến trình tuần” chưa có reaction. | Consistency and standards; control trông có thể bấm cần có hành vi phù hợp. | Chấp nhận nối tới S10 để đường link hiển thị hoạt động. | Kiểm tra reaction và mở S10 từ control đó. |
| S08/S09/S10/S11: tab chỉ nối một phần; S09 chưa có lối vào từ flow chính. | User control and freedom; navigation cần tránh ngõ cụt. | Chấp nhận hoàn thiện destination và bổ sung lối demo empty state dễ tìm. | Rà từng tab, đường trở lại và điểm khởi chạy S09. |
| S11 Article: Back cố định về S10 cả khi mở từ tab Học trên S03. | Match between system and real world; kỳ vọng trở lại theo ngữ cảnh. | Chấp nhận sửa Back theo đường vào, giữ đường về Tiến trình rõ ràng. | Mở từ Home và Weekly, thử Back ở cả hai đường. |
| S04 Meal form và S07 Offline error: retry/back có link nhưng chưa xác minh giữ dữ liệu nhập. | Error prevention và help users recover; persona có kết nối không ổn định. | Chỉnh sửa mô tả theo điều prototype thực sự chứng minh, tránh nói đã lưu bền vững trên thiết bị. | Kiểm tra đường lỗi → sửa/thử lại; ghi rõ dữ liệu mẫu hay tương tác thực tế. |
| Trang 05 Components: thiếu Button Pressed, Text field Filled/Disabled và Dialog destructive/error rõ ràng; Card tappable cần Pressed. | Consistency; phân biệt đang nhấn, nhập, vô hiệu hóa và hành động hủy. | Chấp nhận bổ sung states đúng bảng đề, giữ Focused riêng với Pressed. | Kiểm kê variants/Auto Layout, xem render và kiểm tra instance. |
| Trang 02 Wireframe: hai bộ `12:*` và `52:*` chồng nhau. | Aesthetic and minimalist design; cần nhận ra bộ chính và đối chiếu UI. | Chấp nhận dọn trang, giữ một bộ chính rõ ràng; khai báo nguồn hồi cứu khi áp dụng. | Kiểm kê frame và xem render tổng quan sau sắp xếp. |

Đây là baseline trước sửa. Kết quả thực hiện trong lượt hiện tại:

| Hạng mục | Thay đổi đã thực hiện qua Figma MCP |
| --- | --- |
| Component states | Button có Pressed `61:78`; Text Field có Filled `61:80` và Disabled `61:85`; Card có Pressed `61:90`; Dialog có Destructive `61:93`. Focused vẫn riêng với Pressed. |
| Chọn mục tiêu | S02 chuyển giữa ba frame `13:434` / `63:267` / `63:291`; thẻ chọn có ✓ và “Đã chọn”. Save vẫn mở Home với dữ liệu mẫu, không persist. |
| Điều hướng và empty | Mọi tab chưa chọn trên Home/Journal/Empty/Weekly/Article có destination; tab đang chọn no-op với ✓. Home link `13:458` → Weekly; S08 link `63:365` → S09 “Ngày chưa ghi bữa”. |
| Back và nội dung lỗi | S11 AppBar `BACK` theo nguồn vào, CTA cuối bài vẫn Weekly. S04 dùng fields Filled. S07 hướng dẫn quay lại kiểm tra biểu mẫu, bỏ lời hứa lưu trên thiết bị. |
| Loading và starting points | Spinner arc 40 dp; timer MCP `1.3` chạy khoảng 1,3 giây, thay giá trị cũ `1300` không chạy đúng runtime; fallback “Xem kết quả” `67:403`. Ba native starting points tại `13:373` / `13:378` / `13:383`. |
| Accessibility và responsive | Có 11 bản 412 dp; audit 25 frame 360/412 ghi contrast chữ thấp nhất 5.52:1, body ≥14 px, vùng bấm được audit ≥48 dp. Đã sửa thứ tự đọc top-level, bổ sung dấu chọn, text ngày chart và biên control/chart. |
| Wireframe | Xóa đúng 11 frame trùng `12:*`; giữ 11 frame `52:*` kích thước 360 × 800, grid ba cột với bước 420 × 900, không chồng nhau. Giữ khai báo bộ này dựng hồi cứu từ Final UI. Danh sách ID và thao tác nằm trong [script dọn wireframe](../tools/figma/fix-wireframes.js). |
| Kiểm tra cuối và ảnh | Audit cuối ghi 95 reactions, 92 destinations, không có đích thiếu hoặc vùng bấm thiếu kích thước trong phạm vi audit; 25 variables. Có 25 PNG cuối: 14 ảnh cũ được xuất lại, một preview states và 10 ảnh 412 dp bổ sung; tính cả Home 412 có 11 màn responsive. |

Kết quả và bằng chứng kiểm tra cuối nằm trong [review hiện tại](../docs/reviews/current-fix-review.md). Present không đăng nhập đã đạt kiểm tra truy cập và walkthrough; không suy từ lỗi CloudFront 403 của editor rằng Present cũng bị chặn. Các kiểm tra thiết kế không tự chứng minh semantics, text scale 200%, bàn phím hoặc khả năng truy cập của ứng dụng Flutter trên thiết bị.

## Lịch sử có bằng chứng và giới hạn

| Lượt ghi nhận | Bằng chứng có sẵn | Giới hạn |
| --- | --- | --- |
| Căn chỉnh Figma trước lượt hiện tại | [Review căn chỉnh](../docs/reviews/figma-alignment.md) ghi sửa căn chữ/button/form/navigation, đồng bộ Final UI/Prototype/Home 412; có [manifest ảnh](../assets/figma/manifest.json). | Chỉ có review, audit và ảnh; không có chuỗi prompt/response nguyên văn để gọi đây là ba vòng lặp AI. |
| Rà soát yêu cầu và sắp xếp hồ sơ | [Báo cáo đối chiếu](../docs/submission-review.md) và metadata trực tiếp phát hiện 22 wireframe, thiếu states và reactions; ghi kiểm tra repository. | Lượt này không sửa Figma; browser trước đó lỗi khởi tạo/HTTP 403, nên chưa xác minh Present hoặc quyền công khai. |
| Sửa theo yêu cầu hiện tại | Prompt nguyên văn ở trên; states, liên kết, wireframe, audit và walkthrough sau sửa ghi trong bảng kết quả; [review hiện tại](../docs/reviews/current-fix-review.md) tập hợp bằng chứng cuối. | Đây là một lượt sửa thực tế, không phải ba vòng lặp đã xảy ra trước đây. Present đã mở được không đăng nhập; trang editor chưa xác minh do CloudFront 403. |

Bộ wireframe `52:*` được dựng hồi cứu từ Final UI trong lượt trước, không chứng minh wireframe có trước khi tạo giao diện. Số liệu audit cũ (32 reactions, 31 đích hợp lệ, 24 variables, 7 Text Styles, 1 Effect Style) chỉ thuộc snapshot trước sửa; kết quả cuối dùng review hiện tại và dữ liệu mới.

Ảnh render/export chứng minh hình ảnh tại thời điểm xuất; cấu trúc chứng minh node/variant/reaction có trong file. Present walkthrough mới chứng minh đường đi được thao tác trong trình xem; kiểm tra không đăng nhập mới hỗ trợ xác nhận quyền công khai. Prototype không tự chứng minh backend, lưu bền vững, phân tích dinh dưỡng thật hoặc hỗ trợ trình đọc màn hình trên thiết bị.
