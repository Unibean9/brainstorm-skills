# AI Brainstorm Room — Bộ skill sản phẩm

[English](README.md) · [Tiếng Việt](README.vi.md)

Bộ skill cho agent, giúp đưa một ý tưởng sản phẩm thô đi qua quy trình brainstorm có cấu trúc, PRD bám sát dữ kiện, rồi tạo artifact frontend sẵn sàng để trình bày.

```text
Ý tưởng thô
    ↓
brainstorming — mở rộng, đổi góc nhìn, phản biện và hội tụ, đồng thời giữ provenance
    ↓
prd           — chuyển các quyết định của nhóm thành PRD có thể review
    ↓
frontend-design — tạo landing page hoặc pitch deck từ PRD đã duyệt
```

## Các skill

| Skill | Vai trò | Đầu vào chính | Đầu ra chính |
| --- | --- | --- | --- |
| `brainstorming` | Điều phối phiên làm việc nhiều lượt bằng cách chẩn đoán nhóm cần kiểu tư duy nào tiếp theo | Ý tưởng ban đầu, vấn đề, mục tiêu và bối cảnh nhóm | `.memlog.md`, `brainstorm-intent.md`, insight và quyết định |
| `prd` | Chuyển intent và trace thành PRD có thể review, đồng thời tách dữ kiện, giả định và câu hỏi mở | `brainstorm-intent.md`, `.memlog.md` và input của người dùng | `prd.md`, tùy chọn `addendum.md` và các artifact review |
| `frontend-design` | Tạo landing page hoặc pitch deck self-contained với design system và định hướng hình ảnh rõ ràng | `prd.md` đã được duyệt | `landing-page.html` hoặc `deck.html` |

Ý tưởng thô là điểm bắt đầu của người dùng, không phải một skill riêng. `brainstorming` được kích hoạt khi người dùng muốn đào sâu ý tưởng qua nhiều lượt trao đổi.

Nếu cần đi nhanh, gọi brainstorming với flag `--sp` (short path). Skill chỉ hỏi một lượt các ý chính — ý tưởng/vấn đề, người dùng hoặc đối tượng, và kết quả mong muốn — rồi agent tự mở rộng phần còn thiếu bằng kiến thức của model. Các phần suy ra được đánh dấu là giả định để phân biệt với điều người dùng đã cung cấp.

## Cài đặt với skills.sh

Sau khi push các thư mục `skills/` lên [Unibean9/brainstorm-skills](https://github.com/Unibean9/brainstorm-skills), cài toàn bộ bộ skill:

```bash
npx skills add Unibean9/brainstorm-skills
```

Hoặc cài từng skill:

```bash
npx skills add Unibean9/brainstorm-skills --skill brainstorming
npx skills add Unibean9/brainstorm-skills --skill prd
npx skills add Unibean9/brainstorm-skills --skill frontend-design
```

Trên Windows, có thể chạy installer có sẵn từ thư mục gốc:

```powershell
.\install.ps1
```

Để chỉ cài một skill, ví dụ:

```powershell
.\install.ps1 -Skill brainstorming
```

Installer PowerShell dùng checkout local nên không cần quyền truy cập GitHub. Cách cài từ remote cần quyền đọc repository; nếu repository private, hãy đăng nhập GitHub trước hoặc clone repo rồi chạy `install.ps1` ở local.

Kiểm tra discovery từ thư mục gốc của repository:

```bash
npx skills add . --list
```

## Nguyên tắc của pipeline

1. `brainstorming` không viết PRD khi nhóm vẫn đang ở pha mở rộng ý tưởng.
2. Chuyển sang `prd` khi nhóm đã chọn một hướng hoặc người dùng yêu cầu chốt.
3. `prd` không được biến suy đoán thành sự thật; nội dung suy ra phải gắn nhãn `[ASSUMPTION]`.
4. `frontend-design` chỉ đọc PRD đã duyệt và các input được người dùng cho phép. Skill không được tự tạo testimonial, metric, feature, traction hoặc claim.
5. Có thể chạy một nhánh cuối hoặc cả hai nhánh, nhưng các artifact phải nhất quán với cùng một PRD.

## Bộ dữ liệu đánh giá

Thư mục [`evals/`](evals/) chứa golden dataset và các run đã lưu:

- [`golden-data.yaml`](evals/golden-data.yaml) — ba kịch bản end-to-end bao phủ brainstorming, tạo PRD và tạo landing page hoặc pitch deck.
- [`01-balcony-garden/transcript.md`](evals/runs/01-balcony-garden/transcript.md) — transcript của kịch bản Balcony Garden.
- [`01-balcony-garden/prd.md`](evals/runs/01-balcony-garden/prd.md) — PRD được tạo từ kịch bản đó.

Chạy evaluation bằng:

```bash
python evals/run_eval.py
```

Bộ evaluation được viết bằng tiếng Anh để có thể tái sử dụng với nhiều agent và runtime.

## Bối cảnh sản phẩm

AI Brainstorm Room là một facilitator bằng giọng nói dành cho nhóm học sinh hoặc nhóm làm việc. Nó không mặc định đưa đáp án thay nhóm. Thay vào đó, nó chẩn đoán nhóm đang cần framing, diverging, đổi góc nhìn, critiquing hay converging, rồi đặt một câu hỏi phù hợp. Những gì nhóm nói, lựa chọn và lý giải được lưu lại để PRD và các artifact phía sau phản ánh đúng quá trình suy nghĩ ban đầu.

## Showcase assets

Thêm ảnh chụp từ các live run vào [`assets/showcase/`](assets/showcase/). README gốc sẽ hiển thị các file này khi chúng có mặt:

![Live run 01 — brainstorming](assets/showcase/live-run-01-brainstorm.png)

![Live run 02 — PRD](assets/showcase/live-run-02-prd.png)

![Live run 03 — landing page hoặc deck](assets/showcase/live-run-03-output.png)

Xem [hướng dẫn showcase asset](assets/showcase/README.md) để biết tên file, kích thước và yêu cầu về quyền riêng tư.

## Cấu trúc repository

```text
.
├── README.md
├── README.vi.md
├── skills/
│   ├── brainstorming/
│   ├── prd/
│   └── frontend-design/
├── evals/
│   ├── golden-data.yaml
│   ├── run_eval.py
│   └── runs/
└── assets/showcase/
```
