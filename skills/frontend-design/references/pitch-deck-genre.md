# Pitch deck — best practices

Read alongside `frontend-design/SKILL.md`. This is guidance, not a spine to fill in — slide count
and order are entirely yours; the only render constraints that are actually machine-checked are a
`@page` rule sized for 16:9, at least one `[data-slide]` element, and the credit line text (see
below). `deck.html` is self-contained (no `@font-face`, no CDN) — pick a font pairing from
`references/fonts.md`, don't reach for a webfont.

## The deck is a visual artifact, not a document

`deck.html` is only ever archived as a PDF and shown on a screen — there is no accompanying script
for a presenter to read from. Prioritise image, numeral, and motion over long text: a slide dense
with sentences reads as a document page mistakenly sized 16:9, not a deck. Say the essential thing
in as few words as the slide can carry, and let scale/composition/motif do the rest of the work.

## Every slide prints, none of them hide

`scripts/deck/render_deck.js` produces the PDF by printing the whole document at once, in print
media — every `[data-slide]` becomes its own `@page`. There is no runtime toggling one slide
"active" while the rest sit at `opacity: 0` or `visibility: hidden`; a slide-show pattern built that
way prints as one page of content followed by blank pages. Do not build slide navigation, a
"current slide" JS state machine, or CSS that hides all but one `[data-slide]` by default — every
slide must be visible and laid out in its own right from the first paint. A small hand-written
`<script>` for a scroll-linked reveal *within* a slide is fine (see Motion below); a script that
controls which slide is shown is not.

## Poster typography

You are setting a poster, not a web page. Give each slide `container-type: size` and key the type
scale to slide **height** in `cqh` units (never `ch`, never `em` inherited from a root font size) —
`cqh` resolves against the slide's own box, so the same rules hold on screen and in print. Empty
space is a decision: if half a slide is bare it should hold something deliberate (an oversized
numeral, the motif, a field of accent), not leftover margin.

**Double-constrain a big number, don't single-axis it.** A hero numeral sized purely off width
overflows a short/wide slide; sized purely off height it overflows a narrow one. Cap both:
`font-size: min(18cqw, 22cqh)` reads correctly regardless of which dimension is tighter.

**Weight runs opposite to size.** The bigger the type, the lighter it should sit — a huge numeral
at `font-weight: 700` looks clumsy where `200`–`300` looks confident:

| Size | Weight |
| --- | --- |
| Hero numeral / display title (≥ 8cqh) | 200–300 |
| Section heading (4–8cqh) | 300–400 |
| Body / card copy (1.5–3cqh) | 400–500 |
| Caption / meta / label (smallest on the slide) | 500–600 |

Within one slide, a smaller element should never carry a *lighter* weight than a larger one next to
it — that inversion is what makes the hierarchy read as broken rather than designed.

**A floor under the smallest text.** This prints and gets read from across a room, not zoomed into
on a laptop: keep body/card copy at 18px-equivalent or larger and captions/labels no smaller than
14px-equivalent. If something doesn't fit at that floor, cut the sentence, split the slide, or pick
a shape from the vocabulary below that carries less text — don't shrink past the floor.

## Sketching the arc (optional)

If there's no outline yet, one lens to start from — a lightweight arc, not a template to fill in:
a hook (one contrast, question, or hard number that makes someone stop), context (who's talking and
why), the core content, a turn (something that breaks the expectation set so far), and a takeaway
(one line or a question worth sitting with). Weight each beat by how much the deck actually needs
it, not evenly — a 6-slide deck might spend one slide on the hook and four on the core.

## Slide vocabulary

A menu to pick from, not a sequence to fill in order — combine, skip, or invent freely. Named here
so a slide's shape has a starting point, not so the deck follows a checklist:

| Shape | Reads well for | Structure sketch |
| --- | --- | --- |
| Big-number hero | one metric that carries the whole slide | oversized numeral (`cqh`-scaled), one line of context |
| Two-column split | contrast, before/after, us-vs-them | `grid-template-columns: 1fr 1fr` |
| Feature grid | 3–6 parallel capabilities | `grid-template-columns: repeat(3, 1fr)` |
| Metrics row | 3–4 KPIs side by side | `grid-template-columns: repeat(4, 1fr)` |
| Timeline flow | progression, roadmap, before→now→next | a horizontal or diagonal chain, not a bullet list |
| Quote / testimonial card | a proof moment | label illustrative quotes as a sample, don't imply a real endorsement |
| Full-bleed statement | one sentence that deserves the whole frame | set it large, don't pad it with more words |

```css
.slide-split { display: grid; grid-template-columns: 1fr 1fr; gap: 48px; align-items: center; }
.slide-features { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }
.slide-metrics { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; }
```

Mix shapes across the deck on purpose — a deck of identically-composed slides reads as filled from
a template.

Setting text over an image or a busy gradient? The image needs a genuinely quiet region first —
roughly a third of it low-detail enough to hold type without a fight. If nothing in the composition
gives you that, don't reach for a dark overlay to force it; recompose, crop tighter, or move the
text off the image instead.

## Slide copy formulas

A slide with weak copy gets padded with more words instead of set larger — the opposite of what it
needs. A few structures, translated to the idea's own claim, not filled in verbatim:

| Formula | Fits | Shape |
| --- | --- | --- |
| PAS (Problem–Agitate–Solution) | a problem slide | "`[Nỗi đau]`? Mỗi `[khoảng thời gian]`, `[hệ quả]`. `[Giải pháp]` giải quyết việc này." |
| FAB (Feature–Advantage–Benefit) | a feature/product slide | "`[Tính năng]` giúp `[lợi thế]`, nhờ đó `[lợi ích]`." |
| Before → After → Bridge | a transformation or case moment | trạng thái hiện tại → trạng thái mong muốn → sản phẩm là cầu nối |
| Cost of inaction | an urgency/agitation slide | "Không có `[giải pháp]`, `[hệ quả]` tiếp diễn mỗi `[khoảng thời gian]`." |

Headline test, same as the landing page: a headline that names the *category* ("Giải pháp cho
X") instead of a concrete claim is filler. "Nền tảng quản lý bán hàng" says nothing; "Chốt đơn
trong một cuộc gọi" says something.

## Motion, then reduced motion before print

Motion is welcome here the same way it is on the landing page — CSS `transition`,
`animation-timeline: view()`, staggered `@keyframes` reveals, or a small hand-written `<script>`
where it earns its place (see the pagination warning above for what a script must never control):

```css
@keyframes fadeUp { from { opacity: 0; transform: translateY(24px); } to { opacity: 1; transform: none; } }
.animate-fade-up { animation: fadeUp .6s ease-out forwards; }

.animate-stagger > * { opacity: 0; animation: fadeUp .5s ease-out forwards; }
.animate-stagger > *:nth-child(1) { animation-delay: .1s; }
.animate-stagger > *:nth-child(2) { animation-delay: .2s; }
.animate-stagger > *:nth-child(3) { animation-delay: .3s; }
```

Whatever you use, pair it with a `@media (prefers-reduced-motion: reduce)` block forcing
`opacity: 1; transform: none`: a scroll-linked or delayed reveal whose fill leaves elements at
`opacity: 0` never advances during print, and the deck comes out blank while looking perfect on
screen. `render_deck.js` renders with `prefers-reduced-motion: reduce` forced on — an animation
without this escape hatch is guaranteed to print empty, not just risk it.

## Render contract

`render_deck.js` rejects the file if either is missing: a `@page { size: 1600px 900px; margin: 0 }`
rule (without one the deck prints Letter portrait instead of 16:9), and at least one
`<section data-slide="…">` element.

## Credit line

The route prompt supplies the exact credit line text. Render it verbatim, in small type, low in the
frame — cosmetic placement and styling are yours; the wording is not.
