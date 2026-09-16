# Fonts for self-contained artifacts

`landing-page.html` and `deck.html` are single, self-contained files — no `@font-face`, no
webfont, no CDN, no `http(s)` URL anywhere (the lint that rejects the file catches this). That
rules out "pick anything from Google Fonts," but it doesn't mean settling for Arial: several
Windows ClearType faces are genuinely distinctive and hold up under Vietnamese tone marks.

Pick one pairing, commit to it for the whole artifact — don't mix faces from two different rows.

| Pairing        | Display (headings)  | Body       | Mono / meta | Reads as                    |
| -------------- | ------------------- | ---------- | ----------- | --------------------------- |
| Ink & paper    | `Constantia`        | `Calibri`  | `Consolas`  | editorial, quietly literary |
| Modern clarity | `Segoe UI Semibold` | `Segoe UI` | `Consolas`  | clean, product/tech         |
| Warm humanist  | `Cambria`           | `Corbel`   | `Consolas`  | approachable, warm-serious  |
| Quiet luxury   | `Palatino Linotype` | `Candara`  | `Consolas`  | refined, unhurried          |

```css
:root {
  --font-display: Constantia, Cambria, serif;
  --font-body: Calibri, "Segoe UI", sans-serif;
  --font-mono: Consolas, "Courier New", monospace;
}
```

Always chain a same-category fallback (`serif`/`sans-serif`/`monospace`) after the named face —
but pick that fallback from another row in this table, not a generic default: the diacritics still
need to survive on whatever actually gets used.
