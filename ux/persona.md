# Persona — Nếp Lành

> **Minh là persona giả định** được dựng từ đề tài và bối cảnh sinh viên; nhóm chưa thực hiện nghiên cứu thực địa để xác nhận các chi tiết dưới đây.

## Bối cảnh

**Minh, 20 tuổi — sinh viên năm hai**

Minh có lịch học thay đổi theo ngày và ngân sách ăn uống hạn chế. Minh thường chọn món thuận tiện ở căn tin hoặc gần trường, nên lựa chọn thực phẩm phụ thuộc vào thời gian và những gì có sẵn. Minh muốn tìm hiểu thêm về các món có nguồn gốc thực vật theo chủ đề cuốn *Ăn gì không chết – Sức mạnh chữa lành của thực phẩm*, nhưng không muốn ứng dụng áp đặt một chế độ ăn hoặc biến từng bữa thành bài kiểm tra.

Minh chủ yếu dùng điện thoại để xem thông tin nhanh giữa các tiết học. Khi mở ứng dụng, Minh muốn nhận ra ngay cách ghi bữa ăn, xem lại tuần và tìm một bài học ngắn. Kết nối mạng có thể không ổn định; nếu thao tác gặp lỗi, Minh cần biết cách thử lại hoặc rời bước đó.

## Mục tiêu

- Tự chọn một mục tiêu nhỏ, phù hợp với lịch học và khả năng chi tiêu.
- Ghi bữa ăn và xem lại nhật ký mà không cần đếm calo, cân thực phẩm hay phân loại món thành “tốt/xấu”.
- Nhìn lại tiến trình theo tuần để nhận biết thói quen do mình ghi lại.
- Đọc nội dung dinh dưỡng phổ thông và hiểu đây không phải lời khuyên y tế cá nhân.
- Khi có lỗi kết nối, hiểu trạng thái hiện tại và chọn thử lại hoặc hủy thao tác.

## Khó khăn và nhu cầu thiết kế

| Khó khăn giả định | Nhu cầu thiết kế |
|---|---|
| Giờ học thay đổi khiến mục tiêu cứng và nhắc nhở dày đặc khó theo | Cho phép tự chọn, đổi hoặc bỏ qua mục tiêu; nhắc nhở không gây áp lực |
| Ngân sách hạn chế, lựa chọn ở căn tin không giống nhau mỗi ngày | Ngôn ngữ và ví dụ không giả định có thể mua thực phẩm đắt hoặc tự nấu |
| Không muốn dành nhiều thời gian ghi từng nguyên liệu | Luồng ghi bữa ăn ngắn, có thể xem lại kết quả trước khi mở nhật ký |
| Cảm thấy không thoải mái với điểm số, chuỗi ngày hoặc ngôn ngữ phán xét | Dùng mô tả trung tính; không trừng phạt ngày bỏ lỡ |
| Lỗi kết nối làm gián đoạn việc ghi nhận | Thông báo dễ hiểu, có lựa chọn thử lại và hủy; không khẳng định đã lưu khi chưa rõ |
| Nội dung dinh dưỡng có thể bị hiểu thành lời khuyên cá nhân | Ghi nguồn và phạm vi; không chẩn đoán, điều trị hoặc hứa hẹn phòng bệnh |

## Thiết bị và khả năng tiếp cận

- Thiết kế ưu tiên màn hình điện thoại, thao tác chạm và các bước ngắn.
- Giả định thiết bị chính là điện thoại Android, rộng 360–412 dp, dùng nhanh giữa tiết học; đây là giả định thiết kế, chưa được phỏng vấn xác nhận.
- Dùng chữ rõ, nhãn trực tiếp và nút có vùng chạm đủ lớn.
- Biểu thị trạng thái bằng chữ và biểu tượng, không dựa riêng vào màu sắc.
- Giữ nội dung dễ đọc khi người dùng tăng cỡ chữ hoặc bật trình đọc màn hình.
- Nút Back và thao tác hủy cần dễ đoán; hủy thao tác nhập liệu nên có bước xác nhận dạng dialog.

## Phát biểu vấn đề

Sinh viên như Minh cần cách nhẹ nhàng để đặt mục tiêu cá nhân, ghi lại bữa ăn, xem tiến trình tuần và học một điều nhỏ về thực phẩm có nguồn gốc thực vật. Ứng dụng cần tôn trọng lịch sống và ngân sách thay đổi, đồng thời tránh ép buộc, phán xét hoặc diễn giải thông tin dinh dưỡng thành kết luận sức khỏe.

## Tiêu chí thiết kế để kiểm thử sau này

Đây là **mục tiêu đề xuất cho kiểm thử prototype**, không phải kết quả nghiên cứu hoặc thử nghiệm đã thực hiện:

1. Người tham gia có thể đi từ Chào mừng qua Thiết lập mục tiêu đến Trang chủ trong tối đa 2 phút.
2. Người tham gia tìm được luồng ghi bữa ăn từ Trang chủ trong tối đa 30 giây.
3. Khi gặp màn hình Lỗi kết nối, người tham gia nhận biết được cách thử lại và cách hủy thao tác.
4. Người tham gia tìm được Tiến trình tuần, mở Bài học nhỏ và quay lại màn hình trước.
5. Người tham gia hiểu nội dung là kiến thức phổ thông, không phải chẩn đoán, điều trị hoặc bảo đảm phòng bệnh.

## Ranh giới nội dung

Nếp Lành là ý tưởng ứng dụng hướng dẫn tự quan sát và học kiến thức dinh dưỡng phổ thông. Thiết kế không chẩn đoán, điều trị, dự đoán nguy cơ bệnh, kê chế độ ăn cá nhân hoặc tuyên bố thực phẩm ngăn ngừa/chữa khỏi bệnh. Sách là nguồn cảm hứng chủ đề; nội dung của nhóm cần được tự diễn đạt, dẫn nguồn phù hợp và không sao chép đoạn văn hay bảng biểu. Người cần tư vấn về tình trạng sức khỏe riêng nên trao đổi với chuyên gia y tế có chuyên môn.
