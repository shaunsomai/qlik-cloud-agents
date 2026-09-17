# sales-demo-theme — why these colours

Every palette below was checked with a runnable validator against **Qlik's white chart surface** (`#ffffff`), not chosen by eye. The checks are: lightness band, chroma floor, colour-vision-deficiency separation between pairs, normal-vision separation, and contrast against the surface.

## The data being coloured

| Field | Distinct values | Colour job |
|---|---|---|
| Region, Sales Channel | 3 | categorical |
| Segment, Brand | 4 | categorical |
| Category | 5 | categorical |
| Sales Rep | 8 | categorical |
| Sub Category | 14 | **too many** — fold to Other, or facet |
| Sales, Profit, Margin % | continuous | sequential |
| Margin vs target | signed | diverging |

Eight is the largest honest categorical need, which is exactly the palette size. Sub Category at 14 is past the point where hue can identify anything; Qlik's `othersColor` and the chart's "Others" limit handle that.

## Why not a built-in theme

The built-ins were measured the same way, and none of them pass:

| Palette | Result |
|---|---|
| **sales-demo-theme** (8 slots) | **ALL PASS** — one contrast WARN |
| Qlik default "12 Colors" (Paul Tol) | FAIL ×3 |
| Qlik `horizon` (first 8) | FAIL ×4 |

Qlik's default is the Paul Tol qualitative scheme, and it does pass colour-vision separation (worst adjacent ΔE 12.7). What it fails is everything else: three hues sit outside the lightness band, two read as grey against white (chroma below floor), and `#aa4499` ↔ `#cc6677` measures **ΔE 12.9 for normal vision** — below the 15 floor, so full-colour readers struggle to tell that pair apart.

`horizon` is worse for this purpose: seven of its eight hues fall below the chroma floor, and `#E1DAD5` ↔ `#99CFCD` separate by only 9.9. They are pleasant, low-saturation brand colours — not working data colours.

## The categorical palette

Fixed order, `type: "row"`, never re-assigned by series count:

| Slot | Hue | Hex |
|---|---|---|
| 1 | blue | `#2a78d6` |
| 2 | orange | `#eb6834` |
| 3 | aqua | `#1baf7a` |
| 4 | yellow | `#eda100` |
| 5 | magenta | `#e87ba4` |
| 6 | green | `#008300` |
| 7 | violet | `#4a3aa7` |
| 8 | red | `#e34948` |

```
Palette (light, surface #ffffff, categorical): 8 slots
  [PASS] Lightness band       all 8 inside L 0.43–0.77
  [PASS] Chroma floor         all 8 >= 0.1
  [PASS] CVD separation       worst adjacent #eda100↔#1baf7a ΔE 9.1 (protan)
  [PASS] Normal-vision floor  worst adjacent #e87ba4↔#eda100 ΔE 19.6
  [WARN] Contrast vs surface  below 3:1: #1baf7a 2.82, #eda100 2.17, #e87ba4 2.69
  → ALL CHECKS PASS
```

The contrast WARN is not dismissable: those three hues need visible labels or a table view so identity never rests on the fill alone. Qlik's value labels satisfy this.

## The three-slot cap — read this before colouring a treemap

Those results hold for the **adjacent** pairlist: bars, stacks and lines, where a series only needs to separate from its neighbours. Treemaps, scatter plots and choropleths put every pair side by side, and there the palette does not stretch to eight:

```
5 slots, --pairs all:  [FAIL] #e87ba4↔#eb6834 ΔE 12.9 (normal) — below the 15 floor
3 slots, --pairs all:  [PASS] worst pair ΔE 24.0 (normal), CVD 9.2
```

So the theme ships a second palette, **"Core 3 (all-pairs safe)"**, for those chart forms. Past three categories in a treemap, fold the tail into Other or facet into small multiples.

This applies to the Sales Demo treemap today: it colours by Category, which has five values. It is legible because Qlik draws a 2px gap and a direct label on every tile — the labels are doing work the colours cannot.

## Sequential and diverging

**Magnitude** is one blue hue, light → dark. Continuous gradients use the full `#cde2fb → #0d366b` range. Discrete bands use five spaced steps, because adjacent steps must differ in lightness by at least 0.06 and the light end must clear 2:1 against white:

```
ordinal 5 steps (#86b6ef,#5598e7,#2a78d6,#1c5cab,#104281)
  [PASS] Lightness monotone · [PASS] Adjacent ΔL · [PASS] Light-end contrast 2.11:1 · [PASS] Single hue
```

Two earlier attempts failed and are worth recording: starting at `#cde2fb` fails light-end contrast at **1.32:1** (the lightest step is allowed to recede only for continuous encoding, not for discrete bands), and using consecutive ramp steps fails adjacent ΔL at **0.049**.

**Variance** is red ↔ blue through a neutral grey midpoint, for signed values like margin against target. Two cool hues were rejected: with blue↔aqua the midpoint doesn't read as "nothing".

## Reproducing these results

```bash
node <dataviz-skill>/scripts/validate_palette.js \
  "#2a78d6,#eb6834,#1baf7a,#eda100,#e87ba4,#008300,#4a3aa7,#e34948" \
  --mode light --surface "#ffffff"
```

Qlik ships its own Node at `%LOCALAPPDATA%\Programs\Qlik\Sense\Node\node.exe`, so no separate install is needed. Add `--pairs all` for treemap and scatter forms, `--ordinal` for discrete ramps.

## Known gaps

- **Dark mode is not addressed.** Qlik Sense Desktop renders on white and the four built-ins are all light. A dark variant would need its own steps validated against a dark surface — not an automatic flip of these values.
- **Status colours are not themed.** Qlik has no theme slot for good/warning/critical; those live in per-chart colour expressions. If you add them, keep them distinct from the eight series hues so a status colour never impersonates a series.
