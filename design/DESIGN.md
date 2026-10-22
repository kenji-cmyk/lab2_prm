# Nếp Lành — Design spec

**Nhóm:** 6<br>
**Figma hiện tại:** [Nếp Lành — Cc2O3xSmxgjfvDI2hrsY3Q](https://www.figma.com/design/Cc2O3xSmxgjfvDI2hrsY3Q)<br>
**Bản cập nhật:** 22/10/2026<br>
**Trạng thái:** Đã ghi nhận một lượt căn chỉnh Figma và 11 frame hiện tại. Google Stitch chưa chạy. Kiểm tra accessibility còn hạng mục mở; đây không phải tuyên bố hoàn tất.

## Mục tiêu và giới hạn sản phẩm

Nếp Lành là ứng dụng tiếng Việt giúp ghi nhận bữa ăn, tìm hiểu lựa chọn thực phẩm có nguồn gốc thực vật và chọn thói quen nhỏ phù hợp với đời sống. Đề tài lấy cảm hứng từ cuốn *Ăn gì không chết – Sức mạnh chữa lành của thực phẩm* (tên tiếng Anh nhóm đăng ký: “How eat to die”).

Ứng dụng mang tính giáo dục và theo dõi thói quen, không chẩn đoán, điều trị hay tuyên bố phòng ngừa bệnh; không hứa hẹn kết quả sức khỏe, kê thực đơn hay chấm điểm đạo đức bữa ăn. Nhóm cần tự diễn đạt nội dung học tập, ghi nguồn phù hợp và không sao chép đoạn văn hoặc hình ảnh từ sách.

## Goal: hiện tại và dự kiến

S02 Goal hiện có các thẻ mục tiêu tĩnh; các thẻ chưa có tương tác chọn. Prototype đã nối Back từ S02 về S01 Welcome và Save từ S02 tới S03 Home. Không có nhắc nhở tùy chọn, bỏ qua hay chỉnh sửa trong frame hiện tại. Nếu thiết kế các hành vi ấy sau này, cần ghi riêng là phần dự kiến cho lần refinement, không mô tả như chức năng đã có.

## Các frame hiện có

File Figma hiện có **11 frame** theo chức năng dưới đây. Trong tiêu chí đếm màn hình của Lab, Loading, Offline error và Empty journal là các trạng thái/biến thể của luồng, không nên tính là màn hình chức năng độc lập. Tám màn hình chức năng là Welcome, Goal, Home, Meal form, Result, Journal, Weekly và Article.

| # | Tên frame | Vai trò và trạng thái |
|---:|---|---|
| 1 (S01) | Welcome | Giới thiệu Nếp Lành và điểm vào sử dụng. |
| 2 (S02) | Goal | Thẻ mục tiêu tĩnh; Back → S01, Save → S03. Chọn thẻ chưa được nối. |
| 3 (S03) | Home | Điểm vào ghi bữa ăn, nhật ký, tiến độ tuần và nội dung học; ba tab chưa chọn có prototype link. |
| 4 (S04) | Meal form | Form bữa ăn. Back mở overlay xác nhận; Continue đóng overlay và giữ S04 bên dưới; xác nhận hủy → S03. Link mô phỏng offline → S07. |
| 5 (S05) | Loading | Màn xử lý gợi ý bữa ăn; timer 1.3 giây tự chuyển tới S06, không phải trạng thái lưu nhật ký. |
| 6 (S06) | Result | Hiển thị gợi ý; CTA “Lưu vào nhật ký” dẫn tới Journal S08. Đây chưa phải xác nhận lưu thành công. |
| 7 (S07) | Offline error | Trạng thái offline của luồng xử lý gợi ý; Back và secondary action → S04, Retry → S05. Prototype xác nhận đường đi, chưa xác nhận việc giữ lại dữ liệu đã nhập. |
| 8 (S08) | Journal | Nhật ký khi đã có bản ghi; tab Home được nối về S03. |
| 9 (S09) | Empty journal | Nhật ký rỗng; CTA bắt đầu ghi bữa ăn → S04; tab Home → S03. |
| 10 (S10) | Weekly | Tóm tắt ghi nhận trong tuần; liên kết học tập → S11, tab Home → S03. |
| 11 (S11) | Article | Nội dung đọc và nguồn tham khảo; Back và CTA → S10. Các tab điều hướng ở đây chưa được nối. |

Các đường đi đã xác nhận gồm S02 Back → S01 và Save → S03; S04 mở overlay bằng Back, Continue đóng overlay để trở lại S04, xác nhận hủy → S03 và link mô phỏng offline → S07; S05 tự chuyển sau 1.3 giây → S06; CTA lưu ở S06 → S08; S07 Back/secondary → S04 và Retry → S05; S09 CTA → S04; S11 Back/CTA → S10. Đây là mô tả prototype, không khẳng định lưu bữa ăn thành công hay giữ draft sau lỗi.

Điều hướng hiện ở trạng thái **một phần**: ba tab chưa chọn trên S03 có link; ở S08, S09 và S10 chỉ tab Home nối về S03; các tab khác tại những frame đó và các tab trên S11 chưa được nối. Không nên mô tả toàn bộ tab là dùng được.

## Design tokens

Trang Design System trong Figma hiện có 24 variables: 14 màu cùng các token spacing/radius. Bảng dưới ghi lại palette được rà soát; contrast là phép tính trên các cặp màu nêu rõ, chưa thay thế kiểm tra từng lớp chữ/điều khiển trong screenshot.

### Màu sắc

| Token | Giá trị | Vai trò |
|---|---|---|
| color.primary | #2F6B4F | CTA và trạng thái chính. |
| color.onPrimary | #FFFFFF | Chữ/icon trên primary. |
| color.primaryContainer | #E1F1E6 | Nền chọn/nhấn nhẹ. |
| color.onContainer | #183D2D | Chữ/icon trên primaryContainer. |
| color.canvas | #F7F8F4 | Nền ứng dụng. |
| color.surface | #FFFFFF | Card và dialog. |
| color.textPrimary | #1F2B24 | Tiêu đề và nội dung chính. |
| color.textSecondary | #526258 | Mô tả và nhãn phụ. |
| color.border | #D6DFD7 | Phân tách nhẹ; không dùng riêng làm dấu hiệu điều khiển. |
| color.error | #A4261D | Lỗi; luôn đi kèm thông báo chữ. |
| color.errorContainer | #F9DEDC | Nền thông báo lỗi. |
| color.success | #196C46 | Thành công; luôn đi kèm nhãn/biểu tượng. |
| color.peach | #F4E4D2 | Bề mặt nhấn ấm. |
| color.sky | #E6EEF8 | Bề mặt nhấn lạnh. |

Tương phản tính theo relative luminance: primary trên canvas **5.90:1**; chữ trắng trên primary **6.29:1**; onContainer trên primaryContainer **10.28:1**; textSecondary trên canvas **6.06:1**; textPrimary trên canvas **13.77:1**; error trên errorContainer **5.75:1**; success trên surface **6.41:1**; textPrimary trên peach **11.81:1** và trên sky **12.56:1**. Các cặp này đạt 4.5:1 cho chữ thường; vẫn phải kiểm tra màu thực tế và cỡ chữ trong từng frame.

### Typography

Dùng **Roboto**. Audit ghi nhận 7 Text Styles và không phát hiện font thiếu; các cỡ dưới đây thuộc những lớp đã rà soát.

| Token | Cỡ / line-height | Độ đậm | Bằng chứng / phạm vi |
|---|---:|---|---|
| type.card-title | 20 / 28 px | Theo style Figma | Tiêu đề card/header đã rà soát; khung chữ được căn theo line-height. |
| type.body | 14 / 20 px | Theo style Figma | Nội dung card/header đã rà soát. |
| type.button | 16 / 24 px | Roboto Medium | Nhãn 26 button đã được căn giữa ngang/dọc. |
| type.navigation | 14 / 20 px | Theo style Figma | Nhãn trong 44 Navigation Item đã được căn giữa với icon. |

Các text style ngoài phạm vi rà soát cần đối chiếu trực tiếp với trang Design System. Nội dung chính nhắm tối thiểu 14 sp; mọi lớp chữ nhỏ hơn cần được rà soát thay vì mặc định là đạt.

### Spacing, radius và elevation

| Nhóm | Tokens và trạng thái |
|---|---|
| Spacing | 4, 8, 12, 16, 24, 32 dp theo bộ token nền hiện có; lần căn chỉnh form dùng padding ngang 16 px. |
| Radius | 12, 20 và pill theo bộ token nền hiện có; đối chiếu component trong trang Design System. |
| Elevation | Có 1 Effect Style `Elevation/Level 1`; không phải variable. Không tự suy rộng thành các mức 0–3 chưa có trong file. |

Audit Figma ghi nhận 24 variables (14 màu), 7 Text Styles, 1 Effect Style, 164 bound nodes và 174 bound paints. Đây là thống kê tĩnh từ API/plugin audit, không thay thế lượt Present walkthrough.

### Component và trạng thái

Các component dùng Auto Layout và variants. Ghi chú căn chỉnh đã xác nhận các hạng mục sau trong file hiện tại; không đồng nghĩa với việc mọi trạng thái accessibility đã được kiểm thử.

| Nhóm component | Variants và trạng thái cần thể hiện |
|---|---|
| Button | Default / Focused / Loading / Disabled; nhãn Roboto Medium 16/24 căn giữa. |
| Text field | Default / Focused / Error. |
| Card | Default / Selected. |
| Navigation | Selected / Unselected; icon và nhãn nằm cùng component, căn giữa. |
| App bar | Root / Back; hit area Back 48 × 48 dp bao quanh icon 40 × 40. |
| Dialog | Open / Confirmed. |
| Loading | Processing / Complete; S05 Processing là xử lý gợi ý, không phải lưu nhật ký. |
| Empty | No meals / No results. |
| Error | Offline / Retrying; semantics giữ bản nháp cần xác minh trong prototype. |

## Accessibility và responsive

### Đã ghi nhận từ lượt rà soát Figma ngày 22/10

- 26 button được kiểm tra; nhãn đã căn giữa ngang/dọc và đồng bộ bốn trạng thái; không còn button lệch tâm trong lần rà soát này.
- 44 Navigation Item được kiểm tra; vector được đặt trong component, icon/nhãn căn cùng trục; không còn lỗi căn nhãn tab.
- Prototype navigation chỉ nối một phần: ba tab chưa chọn trên S03 có link; S08/S09/S10 chỉ có tab Home về S03; các tab ở S11 chưa được nối.
- Card/header đã đồng bộ chiều cao khung chữ với line-height: tiêu đề 20/28 px, body 14/20 px; không còn chữ vượt cạnh dưới hoặc frame thấp hơn một dòng trong phần đã kiểm tra.
- Đã căn giữa brand mark, form, nội dung loading/empty, nhãn ngày biểu đồ và thao tác hủy dialog; đã nhóm icon trạng thái với vòng nền.
- Các chỉnh sửa được áp dụng cho Final UI, Prototype và trang chủ rộng 412 px; render trang chủ 412 px đã được xem. 11 secondary actions, AppBar Root/Back Leading và dialog source/cancel actions hiện có hit area 48 dp.

### Checklist cần hoàn tất

- [x] Các vùng đã sửa và đo: 11 secondary actions cao 48 dp; AppBar Root/Back Leading có hit area 48 × 48 dp bao quanh vòng icon 40 × 40; dialog source/cancel actions 48 dp. PNG cuối đã xuất trong assets/figma; các control còn lại vẫn cần rà toàn bộ.
- [ ] Tương phản ≥4.5:1 cho chữ thường, ≥3:1 cho chữ lớn/điều khiển trên từng frame; phép tính token phía trên chưa phải kiểm tra toàn bộ screenshot.
- [ ] Mọi nội dung/nhãn/help text giữ ít nhất 14 sp hoặc có lý do rõ ràng; body 14/20 đã được rà soát ở một số card/header.
- [ ] Không dùng màu làm dấu hiệu duy nhất cho selected, lỗi, loading, tiến độ hoặc trạng thái đồng bộ.
- [ ] Focus nhìn thấy, thứ tự đọc hợp lý, tên accessible cho icon và thông báo trạng thái đọc được.
- [ ] Rà đủ các frame ở 360 dp, 412 dp; kiểm tra hành vi từ 600 dp. Bằng chứng hiện tại mới ghi nhận thay đổi trang chủ 412 px.
- [ ] Kiểm tra text scaling, bàn phím và nội dung dài để bảo đảm CTA không bị che/cắt.

**Giới hạn của kiểm tra:** đã xem render của màn chính, dialog hủy, component điều hướng và màn responsive qua renderer/cấu trúc Figma. Trình xem Figma qua Playwright trả HTTP 403; đây không phải kiểm thử tương tác trực tiếp trong browser.

## Ghi chú nội dung

Nguồn nền được tham khảo gồm WHO, [Healthy diet](https://www.who.int/en/news-room/fact-sheets/detail/healthy-diet), và AHA, [2021 Dietary Guidance — Top Things to Know](https://professional.heart.org/en/science-news/2021-dietary-guidance-to-improve-cardiovascular-health/top-things-to-know). Nội dung trong app cần dẫn nguồn, diễn đạt lại bằng lời của nhóm và giữ tính giáo dục; không chuyển thành kê đơn hoặc lời hứa sức khỏe.
