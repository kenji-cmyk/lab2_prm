# Tóm tắt tài liệu PRM323 Lab 2

## Tổng quan

Lab yêu cầu thiết kế UI/UX cho một ứng dụng di động giải quyết vấn đề thực tế của một nhóm người dùng cụ thể, theo quy trình **Analyze → Generate → Critique → Refine → Prototype → Handoff**. Trọng tâm chấm điểm nằm ở cả quá trình ra quyết định lẫn sản phẩm cuối. Bài làm mặc định là cá nhân; chỉ làm nhóm nếu giảng viên thông báo. **Không cần viết mã Flutter** trong lab này.

Chủ đề cần cụ thể và được giảng viên duyệt. Có thể chọn planner môn học, study planner, ứng dụng sự kiện trong trường, quản lý chi tiêu, đặt đồ ăn, theo dõi thói quen, thư viện hoặc tìm thực tập; chủ đề/persona trùng với sinh viên khác có thể không được duyệt. Thời hạn và trọng số môn học còn để giảng viên điền.

## Yêu cầu sản phẩm

- Có ít nhất **8 màn hình khác nhau**; dialog và biến thể trạng thái không được tính là màn hình riêng.
- Có ít nhất **3 user flow hoàn chỉnh**, mỗi flow nêu điểm bắt đầu, mục tiêu, điểm kết thúc, đường đi chính và nhánh thay thế. Ít nhất một flow phải có lỗi hoặc cách phục hồi.
- File Figma phải có đúng 6 trang, theo thứ tự: `01 User Flow`, `02 Wireframe`, `03 Final UI`, `04 Design System`, `05 Components`, `06 Prototype`.
- Final UI ở kích thước 360 × 800 dp. Wireframe bao phủ mọi màn hình; prototype phải chạy được cả ba flow từ điểm bắt đầu đến kết thúc, không có ngõ cụt, có Back hợp lý, ít nhất một dialog dạng overlay và một chuyển cảnh loading → result.
- Design system định nghĩa và thực sự sử dụng token cho màu sắc, typography, spacing, bo góc và elevation. Bắt buộc có light theme; dark theme tùy chọn. Component cần dùng Auto Layout, variants và token, tránh gán cứng màu/kích thước.
- Tối thiểu 9 nhóm component: Button, Text field, Card, Navigation, App bar, Dialog, Loading, Empty và Error. Cần có các trạng thái phù hợp như disabled, focused, loading, error, selected, xác nhận/hủy và retry.

States bắt buộc theo bảng đề gốc trang 5–6: Button **Default/Pressed/Disabled/Loading**; Text field **Default/Focused/Filled/Error/Disabled**; Card Default/Pressed nếu tappable; Navigation mỗi destination có selected; App bar Default/with actions; Dialog confirmation và một destructive/error variant. Loading cần spinner/skeleton mức màn; Empty có icon/message/action; Error có message/cause/retry. Focused không thay thế Pressed.

## AI, UX và accessibility

Ghi lại nguyên văn prompt đầu tiên gửi Google Stitch và lưu ảnh kết quả. Thực hiện ít nhất **3 vòng lặp có mục tiêu khác nhau**, mỗi vòng xử lý một vấn đề UX cụ thể và có ảnh trước/sau; yêu cầu chung chung như “làm đẹp hơn” không được tính. Dùng AI để phản biện UI theo 10 heuristic của Nielsen, accessibility và persona; lưu prompt cùng toàn bộ phản hồi, với ít nhất **5 phát hiện gắn với màn hình cụ thể**. Với mỗi khuyến nghị quan trọng, ghi rõ chấp nhận, chỉnh sửa hay từ chối và lý do dựa trên persona, heuristic hoặc ràng buộc thực tế. Khai báo mọi công cụ AI đã dùng.

Accessibility/responsive cần có bằng chứng: contrast tối thiểu 4.5:1 cho chữ thường và 3:1 cho chữ lớn/điều khiển; vùng chạm ít nhất 48 × 48 dp; chữ nội dung ít nhất 14 sp; không truyền đạt ý nghĩa chỉ bằng màu. Kiểm tra layout ở rộng 360 dp và 412 dp; handoff mô tả hành vi từ 600 dp trở lên.

## Tài liệu và bàn giao

Repository GitHub theo cấu trúc chính:

Đề trang 7 yêu cầu tên repo **prm323-lab2-<student-id>**; nếu làm nhóm cần dùng quy ước giảng viên cho phép.

```text
README.md
ux/persona.md
ux/user-flow.md
design/DESIGN.md
design/screen-spec.md
design/design-decisions.md
ai/ai-design-log.md
assets/stitch/       # ảnh các phiên bản Stitch
assets/figma/        # PNG các màn hình cuối
handoff/flutter-handoff.md
```

`persona.md` cần có bối cảnh, mục tiêu, pain points, thói quen thiết bị, nhu cầu accessibility, phát biểu vấn đề và tiêu chí thành công đo được. `user-flow.md` cần có danh sách màn hình, cấu trúc điều hướng, ba sơ đồ flow và bảng ánh xạ flow–màn hình. `DESIGN.md` là bản mô tả thiết kế dùng trước prompt đầu tiên. `design-decisions.md` ghi tối đa 10 quyết định quan trọng cùng kết quả checklist accessibility. README nêu chủ đề, persona, link Figma, công cụ AI và vị trí các sản phẩm.

Handoff phải mô tả **6 mục cho từng màn hình**: layout, components/variants, states, tương tác/validation, navigation/Back và các ràng buộc UI. Thêm hai bảng ánh xạ token sang Flutter (`ColorScheme`, `TextTheme` hoặc constants) và component sang widget (ví dụ Button → `FilledButton`). Một bạn cùng lớp cần dựng được một màn hình chỉ từ handoff và dùng Figma để xem hình ảnh tham khảo.

## Rubric 100 điểm

| Tiêu chí | Điểm |
|---|---:|
| Phân tích UX và user flow | 15 |
| Tạo UI bằng AI | 10 |
| Vòng lặp AI và phản biện UX | 15 |
| Thiết kế UI/UX cuối | 20 |
| Design system và components | 15 |
| Prototype tương tác | 10 |
| Flutter handoff | 10 |
| Tài liệu và AI log | 5 |
| **Tổng** | **100** |

Quy trình (UX, AI, lặp/phản biện, tài liệu) chiếm **45 điểm**; sản phẩm (UI, design system, prototype, handoff) chiếm **55 điểm**. Slide và demo là cách trình bày bằng chứng, không tạo thêm hạng mục điểm riêng.

## Gợi ý thuyết trình trong hai file Word

Hai hướng dẫn đề xuất 10 phút trình bày (10–12 slide), 5 phút demo và 5 phút hỏi đáp; giảng viên có thể điều chỉnh. Nội dung slide đi từ vấn đề/persona, kiến trúc thông tin và flows, quá trình AI, quyết định thiết kế, wireframe/UI, design system, accessibility, prototype đến Flutter handoff. Demo nên cho thấy đủ 6 trang Figma, ít nhất 8 màn hình thật, ba flow, một nhánh lỗi/phục hồi, overlay/loading, việc dùng token/component và một ví dụ truy vết prompt → phản biện → quyết định → thay đổi.

Đây là **đề xuất tổ chức buổi đánh giá**, không phải yêu cầu gốc phải nộp slide. Đề gốc yêu cầu một repository GitHub và một link Figma có quyền xem; nếu giảng viên yêu cầu nộp slide thì sẽ thông báo riêng. Hướng dẫn cũng mặc định cá nhân, trừ khi giảng viên cho phép làm nhóm.

## Khác biệt giữa các tài liệu

- Hai PDF có cùng các yêu cầu cốt lõi và rubric. PDF tiếng Anh có thêm mục về liêm chính học thuật/xác minh: lịch sử Git theo thời gian, xem lịch sử phiên bản Figma, có thể yêu cầu walkthrough khoảng 5 phút và xử lý việc khai báo AI/sao chép. Số commit và số ngày trong PDF tiếng Anh vẫn là chỗ trống `[N]`. Trang cuối PDF tiếng Việt chỉ thể hiện quy tắc link Figma không truy cập được sẽ ảnh hưởng điểm và chính sách nộp trễ; phần liêm chính/xác minh không xuất hiện ở đó. Nên xác nhận với giảng viên nếu cần biết bản nào có hiệu lực cho mục này.
- Hai file Word là hướng dẫn thuyết trình bằng tiếng Việt và tiếng Anh, cùng nội dung chính. Chúng trích rubric từ đề lab và đánh dấu rõ thời lượng, số slide, phân vai là khuyến nghị, không phải tiêu chí chấm bổ sung.

## Nguồn đã đọc

- `PRM323 - Lab 2 Thiết kế UI UX có hỗ trợ AI (bản tiếng Việt).pdf`
- `PRM323 - Lab 2 AI-Assisted UI UX Design (Google Stitch → Figma).pdf`
- `PRM323_Lab2_HuongDan_Slide_Presentation_Demo.docx`
- `PRM323_Lab2_Presentation_Assessment_Guidelines_EN.docx`
