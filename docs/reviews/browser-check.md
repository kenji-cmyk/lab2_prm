# Kiểm tra Figma Present và truy cập công khai

Ngày kiểm tra: **22/10/2026**. Phạm vi: file `Cc2O3xSmxgjfvDI2hrsY3Q`, trang **06 Prototype**. Báo cáo này phân biệt kiểm tra trực tiếp trong trình xem với audit cấu trúc bằng MCP.

## Truy cập và môi trường

| Kiểm tra | Kết quả thực tế |
| --- | --- |
| Kết nối Browser trong ứng dụng | **Bị chặn bởi môi trường**: khởi tạo thất bại trước khi chạy mã, báo `missing field sandboxPolicy`. Đã đọc hướng dẫn troubleshooting; không có bước khắc phục lỗi này. |
| Mở URL thiết kế `/design/Cc2O3xSmxgjfvDI2hrsY3Q` qua Playwright dự phòng | **Bị chặn bởi hạ tầng**: HTTP 403, trang CloudFront ghi “Request blocked”. Đây không phải màn Figma yêu cầu cấp quyền; không dùng kết quả này để kết luận file riêng tư. |
| Mở Present trong browser context mới, không cookies hay đăng nhập | **Đạt**: HTTP 200, tiêu đề đúng `Nhóm 6 — Ăn gì không chết - 06 Prototype`, render được launch card Flow 1 và nút **Bắt đầu**. Thanh trình xem hiện **Log in or create account**. Không thay đổi thiết lập chia sẻ. |
| Xác nhận cài đặt “Anyone with the link can view” của file thiết kế | **Chưa xác minh**: truy cập Present công khai đã chạy được, nhưng chưa đọc được hộp thoại Share của editor. Không suy diễn quyền editor từ quyền prototype. |

**Cập nhật ở lượt chỉnh Wireframe tiếp theo:** Playwright mở Chrome có giao diện trong profile mới chưa đăng nhập, URL design nhận HTTP 200 và render trang **02 Wireframe**. UI khách hiện “Sign up to comment, edit, inspect and more.” Kết quả này xác nhận mở được trang design ở chế độ khách; lỗi 403 ở bảng trên là kết quả headless trước đó. Chưa kiểm tra lần lượt đủ sáu trang hoặc giá trị Share. Sau lời nhắc đăng nhập để có quyền Edit, người dùng chọn **“dùng figma mcp”**; toàn bộ thao tác sửa Wireframe được thực hiện qua MCP.

Link Present đã kiểm tra trong context mới: [Flow 1 — Bắt đầu thói quen](https://www.figma.com/proto/Cc2O3xSmxgjfvDI2hrsY3Q?node-id=13-373&starting-point-node-id=13%3A373).

## Accessibility của trình xem

- Mặc định Figma thông báo screen reader support đang tắt. Đã bật **Options → Advanced settings → Accessibility settings → Adapt content for screen readers** trong tùy chọn cục bộ của trình xem.
- Sau khi bật, cây accessibility có tên màn, nội dung tiếng Việt và tên link. Đã focus link **Thiết lập mục tiêu**, nhấn **Enter**, xác nhận URL chuyển từ `13-418` sang `13-434` và article đổi từ **01 Chào mừng** sang **02 Thiết lập mục tiêu**.
- Đã phát hiện và sửa thứ tự đọc top-level vốn bắt đầu từ disclaimer/CTA ở cuối màn. Sau reload, S01/S02/S03 và các màn tiếp theo đọc header → nội dung → CTA/navigation; Card đọc Title → Body. Đã xác nhận riêng launch Flow 1 đọc tiêu đề → mô tả → Bắt đầu và overlay đọc tiêu đề → mô tả → Tiếp tục chỉnh sửa → Hủy bữa ăn.
- Click trực tiếp DOM accessibility có thể bị canvas Figma chặn; keyboard activation bằng **focus + Enter** hoạt động. Đây là đặc điểm thao tác của trình xem, không đủ để kết luận hotspot hỏng.
- Trạng thái chọn mục tiêu có cả dấu **✓** và chữ **Đã chọn**; tab hiện tại có dấu **✓**. Tiến trình có nội dung chữ **Đã ghi: T2–T6 · Chưa ghi: T7, CN** bên cạnh biểu đồ, nên các trạng thái đã quan sát không chỉ dựa vào màu.
- Giới hạn ngữ nghĩa của Figma: overlay xuất thành `article`, không phải `dialog`; Text Field là nội dung mẫu của thiết kế, không phải ô nhập HTML. Không đánh dấu toàn bộ WCAG/screen reader là đạt từ kiểm tra này.

Kiểm tra này không thay thế đo contrast, kích thước vùng chạm, font và clipping trên dữ liệu/ảnh Figma; xem báo cáo accessibility riêng của lần chỉnh sửa cuối.

## Walkthrough sau chỉnh sửa

Các bước dưới đây chạy trực tiếp trong Figma Present, sau khi người phụ trách báo hoàn tất reactions và sau reload. Dùng tên link/button trong accessibility tree, focus rồi nhấn Enter; chờ đúng article của màn đích, không dùng nút Next frame của Figma để bỏ qua flow.

| Kiểm tra | Kết quả |
| --- | --- |
| Native starting points | **Đạt**: sidebar Flows hiển thị ba entry; chọn được launch `13:373`, `13:378`, `13:383`. |
| Flow 1 | **Đạt**: launch → S01 → S02 → Lưu mục tiêu → S03. Chọn Goal 2 chuyển `63:267` với **✓ Ghi lại bữa ăn / Đã chọn**; chọn Goal 3 chuyển `63:291` với **✓ Đọc 5 phút mỗi ngày / Đã chọn**; chọn lại Goal 1 về S02 với **✓ Thêm rau vào bữa ăn / Đã chọn**. |
| Flow 2 và nhánh thành công | **Đạt sau sửa lỗi timer**: launch → S03 → Ghi bữa ăn → S04 → Phân tích → S05 → tự S06 → Lưu vào nhật ký → S08. |
| Phục hồi lỗi | **Đạt**: S04 → Mô phỏng lỗi kết nối → S07 → Thử lại → S05 → tự S06 → Lưu → S08. |
| Empty state có lối vào và lối ra | **Đạt**: S08 → Xem ngày chưa ghi bữa → S09 → Ghi bữa ăn → S04. |
| Overlay xác nhận | **Đạt**: App Bar S04 mở overlay; Tiếp tục chỉnh sửa đóng overlay về S04, vẫn hiển thị fixture Đậu hũ áp chảo; mở lại và Hủy bữa ăn về S03. Đây là kiểm tra dữ liệu mẫu, không phải chứng minh persistence của dữ liệu người dùng. |
| Flow 3 | **Đạt**: launch → S03 → Xem tiến trình tuần → S10 → Đọc gợi ý dinh dưỡng → S11 → Đánh dấu đã đọc → S10. |
| Back theo ngữ cảnh ở S11 | **Đạt**: vào từ S10, App Bar Back về S10; vào từ tab Học ở S03, App Bar Back về S03. |
| Bottom navigation | **Đạt**: chạy đủ 15 destination không được chọn của S03/S08/S09/S10/S11. Đã chờ đúng màn đích ở từng bước; chuỗi chạy gồm 22 bước cả liên kết vào empty state. |

Link bắt đầu: [Flow 1](https://www.figma.com/proto/Cc2O3xSmxgjfvDI2hrsY3Q?node-id=13-373&starting-point-node-id=13%3A373), [Flow 2](https://www.figma.com/proto/Cc2O3xSmxgjfvDI2hrsY3Q?node-id=13-378&starting-point-node-id=13%3A378), [Flow 3](https://www.figma.com/proto/Cc2O3xSmxgjfvDI2hrsY3Q?node-id=13-383&starting-point-node-id=13%3A383).

## Lỗi tìm thấy và kiểm tra lại

S05 trước sửa không tự chuyển sang S06: chờ 30 giây khi bật screen reader adaptation vẫn ở `13-476`; tắt adaptation, click đúng nút canvas rồi chờ thêm 5 giây cũng không chuyển. Báo người phụ trách kiểm tra trigger. Sau khi giá trị timeout trong dữ liệu MCP đổi từ `1300` thành `1.3`, reload rồi chạy lại S04 → S05 → S06 đã đạt: khoảng **2.072 ms** từ Enter ở Phân tích đến khi article S06 xuất hiện, bao gồm thời gian điều hướng/render. Nhánh Retry cũng tự qua S05 → S06. Không dùng phép quy đổi đơn vị để coi cấu hình cũ là đạt; kết luận dựa trên hành vi trình xem. S05 còn có nút **Xem kết quả** làm đường thay thế.

## Phạm vi chưa xác minh

- Giá trị trong hộp thoại Share và quyền xem lần lượt đủ sáu trang chưa kiểm tra. **Prototype và trang design/Wireframe đã mở được không đăng nhập**, theo hai lần kiểm tra trực tiếp mô tả ở trên.
- Không chạy kiểm thử với thiết bị trợ năng thực, font scaling hệ điều hành hay dữ liệu nhập thật. Phép focus + Enter chứng minh kích hoạt bằng bàn phím trong Present, chưa thay thế kiểm tra thứ tự Tab và focus trap của ứng dụng được triển khai.
- Không coi số lỗi console của chính Figma/telemetry là lỗi của thiết kế khi flow và render vẫn hoạt động; không thu thập token/cookies vào hồ sơ.
