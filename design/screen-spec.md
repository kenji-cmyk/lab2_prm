# Nếp Lành — đặc tả 11 frame Final UI

Đặc tả này theo trang **03 Final UI** của file [Nhóm 6 — Ăn gì không chết trên Figma](https://www.figma.com/design/Cc2O3xSmxgjfvDI2hrsY3Q), cùng các frame Prototype riêng ở trang 06. Bộ Final UI có **8 màn hình chức năng** (S01–S04, S06, S08, S10–S11) và **3 frame trạng thái** (S05 đang tải, S07 lỗi, S09 nhật ký trống). Mỗi frame là 360 × 800 dp; có thêm biến thể Home rộng 412 dp ở node 16:164. Overlay xác nhận hủy là trạng thái phủ, không tính vào số màn hình. ID Final UI và Prototype là hai node khác nhau; cột tham chiếu dưới đây ghi riêng từng trang.

Tài liệu phản ánh audit API Figma ngày 2026-10-22: 32 reactions, 31 đích điều hướng hợp lệ, 0 đích thiếu. Đây là audit tĩnh, không phải walkthrough trực tiếp trong Figma Present.

Nếp Lành hỗ trợ ghi nhận thói quen ăn uống và đọc nội dung phổ thông về thực phẩm có nguồn gốc thực vật. Nội dung không chẩn đoán, điều trị, dự đoán nguy cơ hay bảo đảm phòng bệnh. “Phân tích” và “gợi ý” trong prototype là nội dung minh họa, không chứng minh đã có dịch vụ phân tích dinh dưỡng.

## Danh sách và liên kết frame

| Mã | Frame Figma | Node Final UI (trang 03) | Node Prototype (trang 06) | Phân loại | Mục đích |
|---|---|---:|---:|---|---|
| S01 | Chào mừng | 6:2 | 13:418 | Màn hình chức năng | Giới thiệu ứng dụng |
| S02 | Thiết lập mục tiêu | 6:19 | 13:434 | Màn hình chức năng | Chọn ý định thói quen ban đầu |
| S03 | Trang chủ | 6:42 | 13:447 | Màn hình chức năng | Tóm tắt hôm nay và lối vào các khu vực |
| S04 | Ghi bữa ăn | 6:76 | 13:465 | Màn hình chức năng | Nhập tên món, thời điểm và ghi chú |
| S05 | Đang phân tích | 6:101 | 13:476 | Frame trạng thái | Minh họa trạng thái chờ |
| S06 | Kết quả | 6:118 | 13:485 | Màn hình chức năng | Hiển thị gợi ý tham khảo và hành động lưu |
| S07 | Lỗi kết nối | 6:138 | 13:497 | Frame trạng thái | Cho thử lại hoặc quay về món ăn |
| S08 | Nhật ký bữa ăn | 6:155 | 13:507 | Màn hình chức năng | Nhật ký có dữ liệu mẫu |
| S09 | Nhật ký trống | 6:186 | 13:522 | Frame trạng thái | Trạng thái chưa có bản ghi |
| S10 | Tiến trình tuần | 6:213 | 13:534 | Màn hình chức năng | Tóm tắt mục tiêu và hoạt động trong tuần |
| S11 | Bài học nhỏ | 6:257 | 13:563 | Màn hình chức năng | Bài đọc ngắn có hành động tự chọn |
| — | Overlay xác nhận hủy bữa ăn | 10:126 | 13:579 | Overlay, không tính là màn hình | Gọi từ AppBar Back của S04 |

## Hệ thống giao diện và ranh giới

Figma có theme sáng, Roboto, spacing 4/8/12/16/24/32 dp; snapshot variables ghi radius 8/12/20 và pill 999 dp. Typography: Display 30/38, Headline 24/32, Title 20/28, Body 16/24, Body Small 14/20, Label 14/20. Nút chính cao 52 dp, chữ Roboto Medium 16/24, căn giữa. Item điều hướng là 82 × 68 dp; icon 24 dp trong vùng bố trí 32 dp; thanh điều hướng cao 84 dp.

| Token | Giá trị Figma | Ánh xạ ngữ nghĩa |
|---|---|---|
| Brand primary / on primary | #2F6B4F / #FFFFFF | CTA, liên kết và nội dung trên CTA |
| Primary container / on container | #E1F1E6 / #183D2D | lựa chọn và bề mặt nhấn nhẹ |
| Canvas / surface | #F7F8F4 / #FFFFFF | nền màn hình / thẻ |
| Text primary / secondary | #1F2B24 / #526258 | nội dung / mô tả |
| Border | #D6DFD7 | đường phân cách và viền |
| Error / error container | #A4261D / #F9DEDC | lỗi kèm nhãn và hành động |
| Success | #196C46 | xác nhận thành công, luôn có nhãn |
| Accent peach / sky | #F4E4D2 / #E6EEF8 | nhấn phụ, không mã hóa trạng thái duy nhất |

Figma Design System ghi các cặp tương phản: trắng/primary 6.29:1; secondary/white 6.47:1; text-primary/canvas 13.77:1; error/error-container 5.75:1. Đây là số liệu của token trong trang Design System; cần kiểm tra lại chữ và điều khiển thực tế sau khi dựng Flutter. Không dùng màu đơn lẻ để biểu thị trạng thái.

**Vùng chạm Back:** Leading của AppBar Root/Back trong Figma đã được chỉnh thành wrapper 48 × 48 dp. Vòng tròn nhìn thấy là 40 × 40 dp, đặt lệch 4 dp trong wrapper; icon là 24 dp. Giữ nguyên quan hệ này trong Flutter. Nút chính cao 52 dp, các hành động chữ phụ và hủy cao 48 dp; item điều hướng 82 × 68 dp.

**Responsive:** frame gốc là 360 × 800 dp; Home có biến thể 412 dp tại node 16:164. Các frame còn lại không được xem là đã kiểm chứng ở 412 dp chỉ vì cùng trang. Từ 600 dp trở lên, bản Flutter nên giới hạn bề rộng đọc, dàn hai cột ở nơi có lợi và giữ đúng thứ tự đọc/focus. Đây là yêu cầu handoff, không phải tuyên bố Figma đã có đủ frame 600 dp.

## S01 — Chào mừng

1. **Layout:** Status bar; dấu hiệu thương hiệu NL và tên Nếp Lành; minh họa nền xanh nhạt với thông điệp “Ăn đa dạng, từng bước nhỏ”; tiêu đề “Ăn xanh hơn, khỏe từng ngày”; mô tả ứng dụng; CTA “Thiết lập mục tiêu”; dòng nhắc đây là thông tin tham khảo.
2. **Component + variant:** Brand mark; khung minh họa; Text/Display và Body; Button/Primary/Default cao 52 dp; Health disclaimer.
3. **States:** Figma thể hiện trạng thái mặc định. Loading, lỗi khởi tạo và đăng nhập không nằm trong frame, cũng không bắt buộc để vào ứng dụng.
4. **Tương tác / validation:** CTA điều hướng tới S02 trong prototype. Không có trường nhập nên không có validation. Không diễn giải tiêu đề quảng bá thành cam kết sức khỏe.
5. **Navigation / Back:** Điểm vào flow; Back hệ thống rời ứng dụng theo nền tảng. Không có nút Back trong frame. CTA tới S02.
6. **Constraints:** Không có bàn phím; giữ disclaimer đọc được, không nhỏ hơn 14 sp trong bản Flutter. VoiceOver/TalkBack đọc thương hiệu, heading, mô tả, CTA rồi disclaimer; hình minh họa là trang trí. CTA 52 dp. Ở 412 dp mở rộng khoảng trống, không kéo giãn dòng chữ; 600+ dùng cột nội dung giới hạn bề rộng và giữ hình trước tiêu đề trong thứ tự đọc.

## S02 — Thiết lập mục tiêu

1. **Layout:** App bar Back “Mục tiêu của bạn”; thanh tiến độ Bước 1/2; câu hỏi “Bạn muốn bắt đầu từ đâu?”; ba thẻ “Thêm rau vào bữa ăn”, “Ghi lại bữa ăn”, “Đọc 5 phút mỗi ngày”; nút “Lưu mục tiêu”; ghi chú có thể thay đổi sau.
2. **Component + variant:** AppBar/Back; progress indicator; Card/Default và Selected; Button/Primary; Body Small.
3. **States:** Frame tô nền thẻ đầu tiên để nhấn mạnh thị giác; audit Prototype không ghi reaction trên ba thẻ. Đây là trạng thái hình ảnh tĩnh, không xác nhận rằng chọn thẻ hoạt động. Trạng thái lưu lỗi không được thể hiện.
4. **Tương tác / validation:** Prototype chỉ có Back về S01 và nút “Lưu mục tiêu” tới S03; không có reaction chọn card. Flutter có thể triển khai lựa chọn đơn theo thiết kế, nhưng phải xem đó là hành vi cần xây/test riêng; nếu chưa có lựa chọn thì disable Save hoặc cung cấp Skip rõ ràng. Figma không chứng minh persistence.
5. **Navigation / Back:** App bar Back về S01; “Lưu mục tiêu” tới S03. Hành vi Back là đường prototype, chưa quy định lưu/khôi phục khi tiến trình ứng dụng bị đóng.
6. **Constraints:** Không có bàn phím. Đọc ba thẻ như một radio group có selected state và nhãn; Card và CTA rộng theo 320 dp nội dung, vùng thao tác tối thiểu 48 dp. Ở 412 dp giữ các thẻ thành một cột dễ quét; 600+ có thể đặt lựa chọn trong cột giới hạn, giữ indicator và thứ tự focus.

## S03 — Trang chủ

1. **Layout:** App bar thương hiệu; lời chào và ngày; Card “Mục tiêu hôm nay” với ví dụ “1/2 bữa có rau xanh”; dòng “1 trong 2 thói quen hoàn thành” và progress bar; Card “Gợi ý hôm nay”; CTA “Ghi bữa ăn”; link “Xem tiến trình tuần”; navigation bar bốn mục.
2. **Component + variant:** AppBar/Root; Card/Goal và Tip; Progress indicator; Button/Primary; TextButton/Secondary; Navigation Item/Selected cho Trang chủ và Unselected cho Nhật ký, Tiến trình, Học.
3. **States:** Figma hiển thị dữ liệu mẫu và tiến độ một phần. S09 là frame trạng thái rỗng riêng, không được chọn tự động theo dữ liệu từ tab Journal trong Prototype.
4. **Tương tác / validation:** CTA tới S04; trong Prototype, ba nav item chưa chọn mở Nhật ký S08, Tiến trình S10, Học S11. Link “Xem tiến trình tuần” không có reaction; dùng nav Tiến trình để tới S10 trong demo. Nav Nhật ký mở S08; S09 được mở thủ công để trình bày trạng thái rỗng. Flutter cần wiring link tuần nếu muốn dùng được và chọn S08/S09 theo dữ liệu thật. Con số Home phải lấy từ dữ liệu thật khi triển khai, không giữ giá trị mẫu như số thực.
5. **Navigation / Back:** Home là điểm gốc sau onboarding; chuyển tab giữ trạng thái tab/scroll theo thiết kế ứng dụng. Back ở tab gốc tuân hành vi nền tảng. Prototype links không chứng minh có lưu trạng thái.
6. **Constraints:** Home gốc 360 × 800; biến thể rộng 412 dp node 16:164. Thanh dưới 84 dp, item 82 × 68 dp, nhãn luôn đi cùng icon và selected tab có semantics. Không có bàn phím. Từ 600 dp có thể dàn Goal/Tip hai cột; progress phải có mô tả bằng chữ cho screen reader.

## S04 — Ghi bữa ăn

1. **Layout:** App bar Back “Ghi bữa ăn”; tiêu đề “Ghi nhanh bữa ăn”; trường Tên món với ví dụ nhập; trường Bữa ăn với giá trị mẫu “Bữa trưa · 12:30”; Card “Gợi ý ghi chép”; nút “Phân tích bữa ăn”; link mô phỏng lỗi kết nối; disclaimer giáo dục.
2. **Component + variant:** AppBar/Back; Text Field/Default, Focused và Error; Card/Tip; Button/Primary; TextButton/Offline demo; Body Small.
3. **States:** Frame dùng giá trị mẫu ở cả hai trường; trang Components mô tả field trống/focus/error. Không có bàn phím hay lỗi validation đang mở trong Final UI.
4. **Tương tác / validation:** Link mô phỏng mở S07; CTA phân tích mở S05 theo prototype. AppBar Back mở overlay 10:126. Figma chưa chứng minh kiểm tra input. Flutter nên trim và yêu cầu tên món không rỗng, cho phép sửa thời điểm, giữ mọi field khi Back/lỗi; không yêu cầu cân đo, calories hoặc phân loại thực phẩm bắt buộc.
5. **Navigation / Back:** Trong Prototype, AppBar Back mở overlay; CTA tới S05; link mô phỏng lỗi tới S07. Overlay “Tiếp tục chỉnh sửa” đóng về S04; xác nhận “Hủy bữa ăn” tới S03.
6. **Constraints:** Bàn phím văn bản xuất hiện khi focus tên món; nội dung cần cuộn và CTA không bị bàn phím che. Hit target Back 48 × 48 dp trong Flutter dù vòng tròn Figma hiển thị 40 × 40; field có label ngoài input và lỗi được thông báo bằng chữ/semantics, không chỉ viền. Ở 600+ form giữ một cột đọc, không kéo giãn input quá rộng.

## S05 — Frame trạng thái: Đang phân tích

1. **Layout:** App bar Back “Đang phân tích”; tiêu đề “Đang tổng hợp thông tin”; mô tả giữ nguyên bữa ăn; card Loading có icon lá, nhãn “Đang tổng hợp” và câu tiến trình; ghi chú có thể quay lại sửa; CTA “Quay lại chỉnh sửa”.
2. **Component + variant:** AppBar/Back; Loading/Processing; Text/Heading, Body; Button/Primary.
3. **States:** Frame thể hiện Processing. Component library còn biến thể Complete. Prototype chuyển tiếp bằng timer 1300 ms; không có reaction từ S05 sang S07.
4. **Tương tác / validation:** Sau 1300 ms, Prototype đi S06. Back/CTA sửa quay lại S04. Nếu app thật có lỗi request/timeout, Flutter có thể điều hướng S07 nhưng đó là hành vi tương lai, không phải route trong Figma hiện tại. Không hiển thị “đang phân tích dinh dưỡng” nếu không có dịch vụ thực và nguồn nội dung đã kiểm duyệt.
5. **Navigation / Back:** Back và “Quay lại chỉnh sửa” về S04; timer 1300 ms tới S06. Nhánh lỗi S07 chỉ được gọi từ link mô phỏng tại S04 trong Prototype.
6. **Constraints:** Không có bàn phím; loading có nhãn screen reader và chế độ giảm chuyển động; không khóa Back. Nút 52 dp. Trong layout rộng, giữ card loading trong cột giữa; không dùng khoảng trống lớn như tín hiệu ứng dụng bị treo.

## S06 — Kết quả

1. **Layout:** App bar Back “Gợi ý bữa ăn”; label “GỢI Ý THAM KHẢO”; tiêu đề “Một bữa ăn nhiều màu”; tóm tắt món; Card “Điểm nổi bật”; Card “Gợi ý tiếp theo”; CTA “Lưu vào nhật ký”; hành động “Chỉnh sửa thông tin”; disclaimer không thay thế chuyên môn.
2. **Component + variant:** AppBar/Back; Text/Label, Heading, Body; Card/Highlight và Suggestion; Button/Primary; TextButton/Edit; Disclaimer.
3. **States:** Figma hiển thị một kết quả mẫu. Loading và lỗi có frame riêng S05/S07; không có biến thể “chưa có gợi ý” tại màn này.
4. **Tương tác / validation:** “Lưu vào nhật ký” tới S08 theo prototype. “Chỉnh sửa thông tin” về S04. Gợi ý là ví dụ giáo dục, không phải phân tích sức khỏe cá nhân. Flutter chỉ đánh dấu đã lưu sau khi commit local thành công; xác thực nội dung/nguồn trước khi phát hành.
5. **Navigation / Back:** Back và edit đều tới S04; save tới S08. Figma route không khẳng định nhật ký đã ghi xuống thiết bị.
6. **Constraints:** Không có bàn phím; disclaimer tối thiểu 14 sp và theo thứ tự đọc sau CTA. Screen reader đọc title, meal summary, hai card, CTA và disclaimer theo thứ tự; hai card có text đầy đủ khi phóng to. Ở ≥600 dp giới hạn chiều rộng và có thể xếp hai card cạnh nhau; giữ CTA dễ tìm.

## S07 — Frame trạng thái: Lỗi kết nối

1. **Layout:** App bar Back “Kết nối”; tiêu đề “Chưa thể tải gợi ý”; câu nói bữa ăn vẫn được giữ lại trên thiết bị; error card “Chưa có kết nối / Kết nối mạng rồi thử lại”; nút “Thử lại”; link “Quay lại món ăn”; privacy note.
2. **Component + variant:** AppBar/Back; Error & Recovery/Offline; Button/Primary Retry; TextButton/Back to meal; error container; Body Small.
3. **States:** Frame mô tả lỗi kết nối; trang Components có Error & Recovery/Retrying. Thành công retry quay về S05 trong prototype. “Giữ lại trên thiết bị” là nội dung UI mẫu, chưa xác minh persistence thật.
4. **Tương tác / validation:** “Thử lại” đi S05; “Quay lại món ăn” và AppBar Back đều đi S04. Overlay không được mở từ S07. Flutter phải giữ draft khi mất mạng, retry không tạo bản ghi trùng, và nói rõ liệu dữ liệu đã ghi local hay chỉ còn trong form.
5. **Navigation / Back:** Back và action phụ về S04; Retry tới S05; không có overlay hủy tại S07. Overlay chỉ được gọi từ AppBar Back ở S04.
6. **Constraints:** Error có icon/heading/body/Retry, semantics announce lỗi và không phụ thuộc đỏ; thông báo privacy đọc được. Back hit target Flutter 48 × 48 dp; bàn phím không áp dụng. Trên màn rộng giữ error panel gần nội dung chính, không đặt CTA xa.

## S08 — Nhật ký bữa ăn

1. **Layout:** App bar thương hiệu “Nhật ký bữa ăn”; tiêu đề Hôm nay và ngày; Card bản ghi “Bữa trưa · 12:30” với tên món; Card “Ghi chú của bạn”; tổng số bữa đã ghi hôm nay; CTA “Ghi thêm bữa ăn”; nav bar với Nhật ký được chọn.
2. **Component + variant:** AppBar/Root; Card/Meal entry và Note; Text/Date, Summary; Button/Primary; Navigation Item/Selected Journal.
3. **States:** Figma dùng dữ liệu mẫu có một bản ghi và ghi chú; S09 là frame empty state được trình bày riêng. Main Journal reaction trên Home mở S08; prototype không tự chọn S09 theo số bản ghi. Chờ đồng bộ/lỗi tải không được thể hiện.
4. **Tương tác / validation:** CTA tới S04; Prototype chỉ có reaction của nav Home → S03. Nav Journal từ Home mở S08; các tab Tiến trình/Học khi đang ở S08 không có reaction được audit. Flutter cần wiring các tab này nếu hỗ trợ chuyển tab trực tiếp. Frame không gắn rõ hành động sửa/xóa cho từng card; Flutter cần thêm menu/hành động có nhãn nếu hỗ trợ sửa/xóa, và xác nhận trước khi xóa.
5. **Navigation / Back:** Mở từ tab Nhật ký; Back/tab behavior giữ đúng tab. Nếu mở S08 sau khi lưu ở S06, chỉ báo “đã lưu” khi bản ghi thực sự tồn tại.
6. **Constraints:** Card đọc tuần tự, ngày/giờ có label, không dùng màu làm trạng thái sync duy nhất. Không có bàn phím; CTA dễ tìm khi text scale tăng. Ở ≥600 dp có thể đưa tóm tắt và list vào hai cột, nhưng giữ thứ tự đọc nhất quán.

## S09 — Frame trạng thái: Nhật ký trống

1. **Layout:** App bar thương hiệu “Nhật ký bữa ăn”; tiêu đề Hôm nay; Empty State minh họa và nội dung “Chưa có bữa ăn nào / Ghi lại bữa ăn đầu tiên để bắt đầu nhìn thấy thói quen của mình”; CTA “Ghi bữa ăn”; nav bar với Nhật ký được chọn.
2. **Component + variant:** AppBar/Root; Empty State/No meals; Button/Primary; Navigation Item/Selected Journal.
3. **States:** Figma thể hiện nhật ký trống. Empty component có variant riêng; loading/error của dữ liệu cần thiết kế khi triển khai, không được giả là đã có trong frame.
4. **Tương tác / validation:** CTA tới S04. Prototype không có reaction từ tab Nhật ký ở Home tới S09; frame này được mở thủ công để trình bày empty state. Không yêu cầu người dùng nhập một số bữa tối thiểu.
5. **Navigation / Back:** Prototype CTA khởi đầu flow ghi bữa; navigation item Home về S03. Khi lần tải dữ liệu gặp lỗi, Flutter phân biệt rõ lỗi với trạng thái không có dữ liệu.
6. **Constraints:** Empty illustration trang trí, nội dung và CTA là nguồn thông tin chính; screen reader đọc heading trước mô tả. Không có bàn phím. Tại 600+ giữ empty state gọn trong vùng nội dung, không giãn thành một trang rỗng.

## S10 — Tiến trình tuần

1. **Layout:** App bar thương hiệu “Tiến trình tuần”; tiêu đề Tuần này; Card mục tiêu “Mục tiêu rau xanh / 5 trong 7 ngày”; chú thích ngày có ít nhất một bữa ăn ghi lại; biểu đồ 7 cột T2–CN; Card “Điểm sáng”; link “Đọc gợi ý dinh dưỡng”; nav bar với Tiến trình được chọn.
2. **Component + variant:** AppBar/Root; Card/Goal và Highlight; chart 7 ngày; TextButton/Learning link; Navigation Item/Selected Progress.
3. **States:** Figma có dữ liệu mẫu trong tuần, gồm các cột theo ngày và một mục tiêu. Chưa có frame tuần trống hoặc lỗi tải.
4. **Tương tác / validation:** Link đọc mở S11; Prototype chỉ có reaction nav Home → S03. Nav Journal/Học khi đang ở S10 không có reaction được audit. Flutter cần wiring các tab này nếu hỗ trợ chuyển tab trực tiếp. Dữ liệu tuần và mục tiêu phải tính từ log thật trong Flutter; câu “5 ngày liên tiếp” chỉ dùng nếu được tính đúng, và nên ưu tiên câu trung tính “đã ghi nhận trong 5 ngày tuần này” để giảm áp lực.
5. **Navigation / Back:** Tab gốc Tiến trình; link tới S11; Back từ S11 cố định về S10. Không cho chọn tuần tương lai nếu sau này thêm bộ chọn tuần.
6. **Constraints:** Biểu đồ cần nhãn ngày/giá trị hoặc summary thay thế cho screen reader; màu cột không phải khác biệt duy nhất. Không có bàn phím. Chart 7 cột phải còn nhãn đọc được ở 360 dp; tại 600+ có thể bố trí chart và summary hai cột.

## S11 — Bài học nhỏ

1. **Layout:** App bar Back “Bài học nhỏ”; nhãn “ĐỌC 3 PHÚT”; tiêu đề “Đa dạng thực vật, từng bước một”; đoạn giới thiệu về chủ đề sách; Card “Thử trong bữa tối”; đoạn khuyến khích thay đổi nhỏ; ghi nguồn; disclaimer; CTA “Đánh dấu đã đọc”; nav bar với Học được chọn.
2. **Component + variant:** AppBar/Back; Text/Label, Heading, Body; Card/Action prompt; Source/Disclaimer; Button/Primary; Navigation Item/Selected Learn.
3. **States:** Figma hiển thị bài đọc chưa đánh dấu. Trạng thái đã đọc/loading/mất nội dung không có trong frame.
4. **Tương tác / validation:** CTA đánh dấu đã đọc trong prototype; Flutter lưu trạng thái đọc local khi commit thành công. Nội dung cần được biên tập, ghi thông tin nguồn/ấn bản/trang phù hợp và diễn giải bằng lời nhóm; không sao chép nguyên văn dài hoặc biến cảm hứng từ sách thành lời hứa điều trị.
5. **Navigation / Back:** Prototype Back và CTA “Đánh dấu đã đọc” đều tới S10. Tab Học từ Home cũng mở S11. Đây là route cố định trong prototype, không quay về nguồn gọi tùy biến. Bài liên quan chưa được nêu trên frame này.
6. **Constraints:** Bài dài phải cuộn, hỗ trợ phóng to chữ, line height đủ thoáng, link nguồn gạch chân và đọc được; thứ tự đọc tuần tự từ tiêu đề đến nguồn. Không có bàn phím. Ở ≥600 dp dùng cột đọc tối đa khoảng 720 dp; không kéo dòng chữ hết chiều rộng màn.

## Overlay — Xác nhận hủy bữa ăn (không tính là màn hình riêng)

1. **Layout:** Overlay phủ nền; dialog trắng 320 × 252 dp, đặt giữa frame; tiêu đề “Hủy ghi bữa ăn?”; mô tả dữ liệu nháp sẽ bị xóa và người dùng có thể quay lại sửa; nút “Tiếp tục chỉnh sửa”; hành động chữ “Hủy bữa ăn”.
2. **Component + variant:** Dialog/Open và Confirmed; Button/Secondary; TextButton/Destructive; scrim.
3. **States:** Đóng; mở; đóng để tiếp tục; xác nhận hủy. Figma có cả minh họa xác nhận đã hủy trên trang Components.
4. **Tương tác / validation:** “Tiếp tục chỉnh sửa” chỉ đóng overlay, không đổi dữ liệu; “Hủy bữa ăn” yêu cầu thao tác rõ ràng, xóa draft theo chính sách và trở về S03. Tap ngoài/Back chỉ đóng nếu không gây mất dữ liệu ngoài dự kiến.
5. **Navigation / Back:** Final UI node là 10:126, Prototype overlay node là 13:579. Overlay chỉ được gọi từ AppBar Back của S04; “Tiếp tục chỉnh sửa” dùng CLOSE để lộ lại S04; “Hủy bữa ăn” điều hướng tới S03.
6. **Constraints:** Flutter cần modal semantics, focus trap, focus trả lại nút mở, Escape/Back theo nền tảng; hai nút có hit target tối thiểu 48 dp. Mô tả lỗi/mất dữ liệu phải đọc được; ở màn hình rộng giữ dialog 320–400 dp, không full-width.

## Quy tắc diễn giải

- Danh sách này mô tả UI Figma và đường prototype; nó không chứng minh backend, dữ liệu bền vững, đồng bộ, phân tích dinh dưỡng, thông báo hay validation đã được triển khai.
- Những phần ghi “Flutter cần/nên” là yêu cầu khi thực hiện app thật, không phải trạng thái đã kiểm thử.
- Lưu bản ghi chỉ được xác nhận sau khi ghi local thành công. Nội dung thư viện cần nguồn và kiểm duyệt, không thay thế tư vấn y tế.
