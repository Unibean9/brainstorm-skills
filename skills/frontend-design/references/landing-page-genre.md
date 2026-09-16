# Landing page — best practices

Read alongside `frontend-design/SKILL.md`. This is guidance, not a spine to fill in — the number,
order, and names of sections are entirely yours. `landing-page.html` is self-contained (no
`@font-face`, no CDN) — pick a font pairing from `references/fonts.md`, don't reach for a webfont.

## The reader

One person, alone, probably on a phone, arriving with nobody standing beside them to explain.
Their default posture is scepticism, they are mid-way through something else, and the cost of
leaving is zero. They scan — the hero, then a chain of headlines — and stop to read body copy only
where a headline hits a doubt they actually hold. Two consequences:

- **The hero and headline chain carry most of the message.** If a reader saw nothing but the hero
  and every section's headline, the argument should still roughly hold together.
- **The page must stand entirely alone** — every sentence has to survive without a presenter's
  voice, unlike a deck where the language lives in the presenter's mouth.

## Above-the-fold checklist

Everything visible before scrolling is where the reader decides whether to keep reading at all.
Three things have to land before they scroll:

- **Headline** — states the outcome, not the category. Short enough to read in one breath.
  `"Nền tảng quản lý bán hàng"` says nothing; `"Chốt đơn trong một cuộc gọi, không cần demo"` says
  something.
- **One supporting line** — expands the headline by one notch (the how, or the who-it's-for), not
  a second headline restating the same claim.
- **Primary CTA** — the single action the reader should take, worded as that action.

That trio is the floor, not the whole page. Beyond it, add whatever the idea calls for: a
problem/pain moment told as a scene, a differentiator, an objection actually worth answering, a
concrete "how it works" sequence, a proof moment, or a block that doesn't fit any of these labels
at all. Splitting the same claim across many thin sections is not the kind of addition worth
making — that's padding, not a new idea.

## Headline and CTA copy

Weak copy is the single most common reason a section reads as filler. A headline that names the
*category* instead of the *outcome* is the default failure mode — it could sit on any competitor's
page unchanged. A few formulas, translated to the idea's own claim — prompts to think from, not
templates to fill in verbatim:

| Formula | Example |
| --- | --- |
| `[Kết quả]` mà không cần `[nỗi đau]` | "Báo cáo chuẩn không cần biết Excel" |
| `[Kết quả]` trong `[khung thời gian]` | "Ra bản nháp trong 5 phút" |
| Cách `[tốt hơn]` để `[việc quen thuộc]` | "Cách nhanh hơn để duyệt chi" |
| Ngưng `[nỗi đau]`. Bắt đầu `[kết quả]`. | "Ngưng đoán. Bắt đầu biết chắc." |

Same test for the CTA: a verb without a stake ("Tìm hiểu thêm", "Gửi", "Đăng ký") asks for the
click without saying what it buys. Pair the verb with the payoff instead — "Dùng thử miễn phí",
"Xem demo 2 phút" — and reserve a lower-commitment link, if one is needed, underneath the primary
button rather than beside it. One primary action per screen; a second link is fine, a second
button carrying the same visual weight is not.

## Proof, without fabricating it

A claim lands harder with something behind it — a number, a named capability, a concrete scenario.
But this is a workshop artifact, not a live product with real customers: no logos, counts, or
quotes attributed to a real company or person who was never in the room. Where the material
genuinely wants a proof shape — a quote card, a comparison row, a before/after — build it and label
it as a sample rather than let it read as a real endorsement:

```html
<aside data-placeholder="testimonial">
  <p class="badge">MẪU MINH HOẠ</p>
  …
</aside>
```

## Interaction — this page is opened, not projected

A deck is presented; this page is used, by one person, with a thumb. A page with no response to
being touched reads unfinished. `:hover`/`:active` (wrapped in `@media (hover: hover)`),
`:focus-visible` with a real focus ring, short `transition`s on colour/transform/border,
`position: sticky`, `scroll-behavior: smooth`, `animation-timeline: view()` for a scroll-linked
reveal — all fair game, all achievable without `<script>`. One or two interactions done precisely
beat eight.

## Mobile and print

`<head>` needs `<meta name="viewport" content="width=device-width, initial-scale=1">` — without it
the page renders tiny on a phone. No horizontal overflow at 375px — relative units throughout. The CTA is tapped with a thumb, not
clicked with a cursor: minimum 44px tap height, enough padding that it doesn't sit flush against
neighbouring elements, full-width where the layout allows it. If you animate at all, carry both a
`@media print` and a `@media (prefers-reduced-motion: reduce)` block forcing
`opacity: 1; transform: none`.

## Common slip-ups

- **Headline names the category, not the outcome** — reads generic, could belong to any competitor.
- **CTA text is a low-commitment verb** ("Tìm hiểu thêm", "Xem thêm") instead of the action itself.
- **More than one CTA competing for attention** at the same visual weight.
- **A claim with nothing behind it** — a number or feature mentioned nowhere in `prd.md`.
- **Every section the same stacked, centred column** — the tell that a page was filled in from a
  template rather than composed. Break the rhythm on purpose in at least two blocks.
