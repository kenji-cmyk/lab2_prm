# Nếp Lành — Design decisions

Các quyết định này phản ánh frame Figma hiện tại và ghi chú rà soát ngày 22/10/2026. Những hạng mục đánh dấu mở vẫn cần bằng chứng trước khi xem là đạt.

| # | Quyết định | Lý do | Hệ quả / bằng chứng |
|---:|---|---|---|
| 1 | Định vị app là công cụ giáo dục và theo dõi thói quen, không phải công cụ y tế. | Chủ đề dinh dưỡng có thể bị hiểu thành chẩn đoán hoặc cam kết sức khỏe. | Không dự đoán bệnh, kê điều trị, hứa phòng bệnh hay chấm điểm sức khỏe; nội dung cần rà soát trước handoff. |
| 2 | Giữ 11 frame hiện tại, phân biệt màn hình chức năng với trạng thái và ghi rõ nguồn gốc wireframe. | Loading, Offline error và Empty journal là trạng thái/frame của luồng; rubric không tính chúng như màn hình độc lập. | Tám màn hình chức năng: Welcome, Goal, Home, Meal form, Result, Journal, Weekly, Article. Page 02 hiện có 11 frame grayscale dựng hồi cứu từ Final UI ngày 22/10/2026, không phải wireframe nguyên gốc trước UI. |
| 3 | Tách xử lý gợi ý bữa ăn khỏi việc lưu vào nhật ký. | S05 xử lý gợi ý và tự chuyển sau 1.3 giây; S06 hiển thị gợi ý kèm CTA lưu. | Luồng hiện tại: S04 → S05 → S06 → “Lưu vào nhật ký” → S08. Link mô phỏng offline tại S04 → S07; tại S07 Back/secondary → S04 và Retry → S05. Không gọi S06 là saved result; prototype xác nhận đường đi nhưng không xác nhận draft được giữ sau lỗi hay việc lưu thành công. |
| 4 | Giữ Goal cards tĩnh; phân biệt hành vi đã nối với ý tưởng refinement. | S02 chưa có chọn thẻ; prototype có Back → S01 và Save → S03. | Không mô tả reminders, skip hay edit là chức năng hiện có. Chúng chỉ là refinement tương lai nếu được bổ sung và kiểm tra. |
| 5 | Journal và Empty journal phải phân biệt dữ liệu có và chưa có. | Trạng thái rỗng cần giải thích, không khiến người dùng nghĩ app bị lỗi. | Empty journal không dùng số liệu mẫu giả; CTA S09 dẫn tới S04 để bắt đầu ghi bữa ăn. |
| 6 | Dùng palette Figma hiện tại với Roboto. | Giữ nhất quán với 24 variables được rà soát và các component đã căn chỉnh. | Primary #2F6B4F, onPrimary #FFFFFF, primaryContainer #E1F1E6, onContainer #183D2D, canvas #F7F8F4, surface #FFFFFF, textPrimary #1F2B24, textSecondary #526258, border #D6DFD7, error #A4261D, errorContainer #F9DEDC, success #196C46, peach #F4E4D2, sky #E6EEF8. Typography đã rà: button 16/24, card title 20/28, body 14/20, navigation 14/20. Audit ghi nhận 7 Text Styles và Effect Style Elevation/Level 1; 164 bound nodes, 174 bound paints. |
| 7 | Chuẩn hóa căn chỉnh theo component thay vì sửa từng instance rời. | Các lỗi lệch nhãn/icon lặp lại trên nhiều màn hình và variants. | Đã nhóm vector vào Navigation Item; căn lại 26 button, 44 nav item, brand mark, form, loading/empty và dialog trong lượt review được ghi nhận. |
| 8 | Mọi hit area phải đạt tối thiểu 48 × 48 dp. | 44 dp secondary actions và icon Back 40 dp không đáp ứng yêu cầu nếu đó là toàn bộ hit area. | Đã sửa 11 secondary actions thành 48 dp; Back 40 × 40 có wrapper 48 × 48; dialog source/cancel actions 48 dp. Cần rà các control còn lại và xem PNG export. |
| 9 | Nhật ký tuần mô tả hành vi tự ghi nhận, không suy ra kết quả sức khỏe. | Log bữa ăn không đủ cơ sở để đánh giá sức khỏe cá nhân. | Dùng câu trung tính như “Bạn đã ghi nhận…”; không calories, cân nặng, bệnh hay ngôn ngữ nhân quả. |
| 10 | Bài đọc phải ghi nguồn và dùng nội dung tự diễn đạt. | Đề tài lấy cảm hứng từ sách và nội dung dinh dưỡng cần được trình bày có trách nhiệm. | Dẫn WHO/AHA hoặc nguồn phù hợp; không sao chép sách, kê đơn hay hứa hẹn kết quả. |

## Accessibility checklist

| Tiêu chí | Mục tiêu | Trạng thái bằng chứng |
|---|---|---|
| Tương phản chữ thường | ≥4.5:1 | Đã tính các cặp palette trên canvas/surface; cần kiểm tra mọi lớp chữ trong frame cuối. |
| Tương phản chữ lớn/điều khiển | ≥3:1 | Cần đo các cặp dùng thực tế, nhất là viền/focus. |
| Vùng chạm | ≥48 × 48 dp | Đã xác nhận 11 secondary actions, Back wrapper và dialog source/cancel actions có hit area 48 dp; rà các control còn lại sau PNG export. |
| Cỡ chữ nội dung | ≥14 sp | Body 14/20 đã rà soát ở một số card/header; các text layer còn lại cần kiểm tra. |
| Trạng thái không chỉ bằng màu | Có nhãn/icon/hình dạng | Đã là quy tắc thiết kế; chưa có checklist từng trạng thái/frame. |
| Điều hướng/Figma alignment | Nhãn/icon căn giữa component; prototype link đúng đích | 26 button và 44 Navigation Item đã được kiểm tra; điều hướng chỉ một phần: ba tab chưa chọn ở S03 có link; S08/S09/S10 chỉ tab Home nối S03; tab S11 chưa nối. S11 Back/CTA về S10. |
| Responsive | 360, 412 và từ 600 dp | Ghi nhận áp dụng/xem trang chủ 412 px; chưa có bằng chứng đầy đủ cho mọi frame/breakpoint. |
| Focus/đọc màn hình | Focus rõ, tên icon, thứ tự hợp lý | Chưa xác minh bằng assistive technology. |
| Phục hồi offline | Giải thích lỗi, đường quay lại và Retry | Prototype nối S04 link mô phỏng offline → S07; S07 Back/secondary → S04, Retry → S05. Việc giữ dữ liệu chưa được xác minh. |

**Kết quả accessibility chưa hoàn tất:** Figma alignment review không đồng nghĩa với kiểm thử WCAG hoặc assistive technology. 11 secondary actions, AppBar Back wrapper và dialog source/cancel actions đã được xác nhận có hit area 48 dp. Cần kiểm tra những control còn lại và các tiêu chí khác.

**Bổ sung sau đối chiếu đề gốc:** metadata mới ghi 22 frame ở trang Wireframe (hai bộ đặt chồng), không phải chỉ 11 frame như snapshot cũ. Button thiếu Pressed; Text Field thiếu Filled/Disabled; Card Pressed và Dialog destructive/error cần bổ sung hoặc xác minh. Xem [bảng đối chiếu](../docs/submission-review.md). Các ghi nhận lịch sử phía trên không xác nhận đã đáp ứng đủ mọi states/accessibility.
