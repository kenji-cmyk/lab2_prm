# Nếp Lành — Design brief

**Nhóm 6 · cập nhật 22/10/2026.** [Figma](https://www.figma.com/design/Cc2O3xSmxgjfvDI2hrsY3Q). Quy trình hiện tại: Codex đọc đề/UX/brief, dùng Figma MCP thiết kế và sửa. Brief là đầu vào của lượt chỉnh hiện tại, không chứng minh thời điểm trước lần generation đầu tiên đã thất lạc log.

## Người dùng, mục tiêu và tone

Minh là sinh viên 20 tuổi, dùng điện thoại Android 360–412 dp trong những khoảng nghỉ ngắn. App giúp chọn thói quen nhỏ, ghi bữa ăn, nhìn lại tuần và đọc bài học ngắn. Persona là giả định thiết kế.

Dùng tiếng Việt dễ hiểu, thân thiện, ví dụ món ăn quen thuộc và ngôn ngữ trung tính. Nguồn cảm hứng là sách Ăn gì không chết; không sao chép nội dung dài, không chẩn đoán hoặc hứa phòng/chữa bệnh. Ghi rõ nội dung mang tính giáo dục.

## Màn hình và điều hướng

Có 8 màn chức năng: Welcome, Goal, Home, Meal form, Result, Journal, Weekly, Article. Loading, Offline error, Empty journal là 3 trạng thái; dialog hủy là overlay. Final UI 360 × 800; có đủ 11 khung 412 × 800 đối chiếu.

Ba flow: onboarding→Home; Home→Meal→Loading→Result→Journal; Home→Weekly→Article→Weekly. Flow ghi bữa có lỗi/retry và hủy/tiếp tục. Goal có ba lựa chọn với ✓/Đã chọn; Article Back theo nguồn vào. Các inactive tabs, Home link và lối vào empty date đã nối. Xem [user flow](../ux/user-flow.md).

## Màu sắc

| Token | Giá trị | Vai trò |
| --- | --- | --- |
| color/brand/primary | #2F6B4F | CTA, link, outline |
| color/brand/on-primary | #FFFFFF | Chữ/icon trên primary |
| color/brand/primary-container | #E1F1E6 | Selected/container |
| color/brand/on-primary-container | #183D2D | Chữ trên container, pressed CTA |
| color/surface/canvas | #F7F8F4 | Nền màn |
| color/surface/default | #FFFFFF | Card/dialog |
| color/text/primary | #1F2B24 | Chữ chính |
| color/text/secondary | #526258 | Chữ phụ |
| color/border/default | #D6DFD7 | Separator/trang trí |
| color/border/control | #526258 | Viền field active, tương phản ≥3:1 |
| color/state/error | #A4261D | Chữ/icon lỗi và thao tác hủy |
| color/state/error-container | #F9DEDC | Nền lỗi |
| color/state/success | #196C46 | Thành công, có nhãn/icon |
| color/accent/peach | #F4E4D2 | Bề mặt phụ |
| color/accent/sky | #E6EEF8 | Bề mặt phụ |

Không dùng border/default nhạt làm tín hiệu điều khiển duy nhất. Text contrast thấp nhất trong các frame được đo là 5,52:1; control border trên trắng khoảng 6,47:1. Xem [audit](../docs/reviews/accessibility-audit.json).

## Typography, spacing và radius

Dùng Roboto. Text Styles: Display 30/38, Headline 24/32, Title 20/28, Body 16/24, Body Small 14/20, Label 14/20 Medium, Label Bold 14/20 Bold. Button label 16/24 Medium. Các text layers hiển thị tối thiểu 14 px trong khung chuẩn; Flutter dùng sp.

Spacing: 4/8/12/16/24/32 dp. Radius: 8/12/20 và pill 999 dp. Elevation dùng Effect Style Elevation/Level 1. Audit có 25 variables, 7 Text Styles và 1 Effect Style; không tự suy rộng thành các cấp token chưa có.

## Components và states

| Nhóm | States/variants hiện có |
| --- | --- |
| Button | Default, Focused, Pressed, Loading, Disabled |
| Text Field | Default, Focused, Filled, Error, Disabled |
| Card | Default, Selected, Pressed |
| Navigation Item | Selected, Unselected; Home/Journal/Progress/Learn có icon và nhãn |
| App Bar | Root, Back; leading hit target 48 × 48 |
| Dialog | Open, Confirmed, Destructive |
| Loading | Processing, Complete; indicator vòng40dp |
| Empty State | No meals, No results |
| Error & Recovery | Offline, Retrying |

Giữ Auto Layout và token bindings; dùng instances thay các bản rời. [Ảnh states review](../assets/figma/15-component-states.png) dùng instances để đối chiếu phần bổ sung. Nút chính cao52dp, secondary48dp, nav82×68dp ở bản360.

## Accessibility và responsive

- Text ≥14 px; contrast chữ ≥4,5:1, control ≥3:1, click target ≥48×48dp trong phạm vi audit.
- Goal/nav selected có ✓, chart có text ngày đã/chưa ghi; không chỉ dùng màu.
- Đã sửa layer order cho Figma đọc màn/launch/overlay từ trên xuống; keyboard focus+Enter chạy được flow. Figma Present cần bật Adapt content for screen readers.
- Đã có 11 bản412 và đo bounds/contrast/type. Khi triển khai, giữ nội dung cuộn, CTA không bị bàn phím che, hỗ trợ font scaling và semantics; ≥600dp dùng cột đọc giới hạn hoặc hai cột theo handoff.
- Chưa kiểm tra thiết bị trợ năng, keyboard ảo hoặc toàn bộ Tab/focus trap của app Flutter.

## Nguồn và giới hạn

[Review sau sửa](../docs/reviews/current-fix-review.md), [QA Present](../docs/reviews/browser-check.md), [snapshot hiện tại](figma-audit.json). Wireframe bộ52:* được dựng hồi cứu; đã xóa bộ12:* trùng và giữ 11 frame rõ ràng. Prototype chỉ dùng fixture, không có backend, persistence hay phân tích dinh dưỡng thật.

Present công khai đã xác minh; quyền editor công khai chưa xác minh do CloudFront403 trong môi trường. Codex + Figma MCP là lựa chọn thay công cụ của người thực hiện bài; chưa có xác nhận giảng viên chấp thuận thay Stitch/đánh giá iteration lịch sử.
