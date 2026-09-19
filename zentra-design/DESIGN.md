---
version: alpha
name: Zentra
description: Modern, futuristic, luxury asset-management identity — deep navy ground, metallic gold as the single accent, glassy depth, thin gold hairlines.
colors:
  primary: "#0B1B2E"
  navy-deep: "#071120"
  navy-panel: "#12283F"
  navy-elevated: "#16304A"
  gold-core: "#C9A227"
  gold-light: "#E8CE86"
  gold-deep: "#9A7A2E"
  text-primary: "#FFFFFF"
  text-body: "#C7D1DC"
  text-muted: "#8C9FB4"
  on-gold: "#0B1B2E"
  success: "#43B02A"
  warning: "#D98A1F"
  danger: "#E8776A"
  info: "#00A3B5"
  success-deep: "#2E7D1F"
  warning-deep: "#8A5A00"
  danger-deep: "#C0392B"
  info-deep: "#00707E"
  surface-light: "#F5F7F9"
  ink-light: "#16222F"
  muted-light: "#5F6B7A"
  line-light: "#E2E8F0"
typography:
  display:
    fontFamily: Plus Jakarta Sans
    fontSize: 68px
    fontWeight: 800
    lineHeight: 1.02
    letterSpacing: "-0.02em"
  h1:
    fontFamily: Plus Jakarta Sans
    fontSize: 44px
    fontWeight: 800
    lineHeight: 1.08
    letterSpacing: "-0.02em"
  h2:
    fontFamily: Plus Jakarta Sans
    fontSize: 30px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: "-0.01em"
  h3:
    fontFamily: Plus Jakarta Sans
    fontSize: 19px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "0em"
  eyebrow:
    fontFamily: Plus Jakarta Sans
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: "0.3em"
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: "0em"
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "0em"
  label:
    fontFamily: Plus Jakarta Sans
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "0.08em"
  micro:
    fontFamily: Plus Jakarta Sans
    fontSize: 11.5px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: "0.16em"
  button:
    fontFamily: Plus Jakarta Sans
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "0.12em"
  numeric:
    fontFamily: Plus Jakarta Sans
    fontSize: 30px
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: "-0.01em"
rounded:
  none: 0px
  xs: 6px
  sm: 10px
  md: 14px
  lg: 20px
  xl: 28px
  pill: 999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  2xl: 64px
  3xl: 96px
components:
  app-shell:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.text-body}"
  panel-navy:
    backgroundColor: "{colors.navy-panel}"
    textColor: "{colors.text-body}"
    rounded: "{rounded.md}"
    padding: 24px
  panel-glass:
    backgroundColor: "{colors.navy-elevated}"
    textColor: "{colors.text-primary}"
    rounded: "{rounded.lg}"
    padding: 24px
  card-light:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.ink-light}"
    rounded: "{rounded.md}"
    padding: 20px
  button-primary:
    backgroundColor: "{colors.gold-core}"
    textColor: "{colors.on-gold}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 16px
  button-primary-hover:
    backgroundColor: "{colors.gold-light}"
    textColor: "{colors.on-gold}"
    rounded: "{rounded.pill}"
  button-ghost:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.gold-core}"
    rounded: "{rounded.pill}"
    padding: 16px
  button-ghost-hover:
    backgroundColor: "{colors.navy-panel}"
    textColor: "{colors.gold-light}"
    rounded: "{rounded.pill}"
  nav-link:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.text-body}"
    typography: "{typography.body-md}"
    padding: 10px
  nav-link-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.gold-core}"
    padding: 10px
  icon-tile:
    backgroundColor: "{colors.navy-panel}"
    textColor: "{colors.gold-core}"
    rounded: "{rounded.md}"
    size: 44px
  icon-circle:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.gold-core}"
    rounded: "{rounded.pill}"
    size: 64px
  stat-card:
    backgroundColor: "{colors.navy-panel}"
    textColor: "{colors.text-primary}"
    typography: "{typography.numeric}"
    rounded: "{rounded.md}"
    padding: 20px
  badge-status:
    backgroundColor: "{colors.navy-panel}"
    textColor: "{colors.gold-light}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 8px
  badge-success:
    backgroundColor: "{colors.navy-panel}"
    textColor: "{colors.success}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 8px
  badge-warning:
    backgroundColor: "{colors.navy-panel}"
    textColor: "{colors.warning}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 8px
  badge-danger:
    backgroundColor: "{colors.navy-panel}"
    textColor: "{colors.danger}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 8px
  badge-info:
    backgroundColor: "{colors.navy-panel}"
    textColor: "{colors.info}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 8px
  input-field:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.text-primary}"
    rounded: "{rounded.sm}"
    padding: 12px
  input-placeholder:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.text-muted}"
    rounded: "{rounded.sm}"
    padding: 12px
  stat-label:
    backgroundColor: "{colors.navy-panel}"
    textColor: "{colors.text-muted}"
    typography: "{typography.label}"
    padding: 4px
  card-light-bordered:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.ink-light}"
    rounded: "{rounded.md}"
    padding: 20px
  table-rule:
    backgroundColor: "{colors.line-light}"
    height: 1px
  label-on-light:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.muted-light}"
    typography: "{typography.label}"
    padding: 4px
  badge-success-light:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.success-deep}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 8px
  badge-warning-light:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.warning-deep}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 8px
  badge-danger-light:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.danger-deep}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 8px
  badge-info-light:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.info-deep}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 8px
  divider-gold:
    backgroundColor: "{colors.gold-deep}"
    height: 1px
  hero-panel:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.text-primary}"
    padding: 40px
---

## Overview

Zentra is the umbrella brand for a family of property, legal, finance, and workspace
systems. Every Zentra surface must read as **modern, futuristic, and luxurious** — one
recognisable identity, whether the visitor lands on Asset, Law, Finance, or Hub.

The identity is built on three decisions:

1. **Deep navy is the ground, not a colour choice.** Almost the entire surface is navy.
   Content is lit *out of* the darkness rather than placed on white. Light surfaces are
   the exception reserved for dense operational screens (dashboards, tables, forms).
2. **Gold is the only accent and it is never flat.** Gold appears as a linear metallic
   gradient (light → core → deep), never a solid fill, because metallic gradient is what
   separates "luxury" from "mustard". Gold is reserved for: the primary action, the brand
   mark, hairline rules, and active nav state. It is never used for body text.
3. **Depth comes from light and hairlines, not from drop shadows.** Elevation is expressed
   with a lighter navy panel, a 1px gold hairline at 40–60% opacity, and a soft gold outer
   glow on the primary action. Heavy box-shadows are off-brand.

The posture is **confident and quiet**: generous space, wide letter-spacing on small caps,
few type weights, and no decoration that does not carry meaning.

## Colors

- **Primary — navy `#0B1B2E`:** the default page ground for every Zentra surface. Also the
  text colour that sits *on* gold.
- **Navy deep `#071120`:** vignette corners, page top/bottom bands, inset fields. Navy
  panel `#12283F` and navy elevated `#16304A` are the two stacking levels for cards —
  use them instead of shadows to create depth.
- **Gold core `#C9A227`:** the accent. Carried over from the existing live Zahir MJ
  sites so Zentra inherits established brand equity rather than introducing a third gold.
  `gold-light #E8CE86` is the top gradient stop and hover state; `gold-deep #9A7A2E` is
  the bottom stop and the hairline colour.
  Rule: **gold is a gradient, never a flat fill.**
- **Text:** `text-primary #FFFFFF` for headlines and emphasised numbers; `text-body
  #C7D1DC` for paragraphs on navy; `text-muted #8C9FB4` for captions and metadata.
- **Semantic — two sets, surface-matched (see the contrast table):** for **navy** surfaces
  use success `#43B02A`, info `#00A3B5`, warning `#D98A1F`, danger `#E8776A`. For **light**
  surfaces use the deeper set: success `#2E7D1F`, info `#00707E`, warning `#8A5A00`, danger
  `#C0392B`. Bright-on-light and deep-on-navy both fail AA. Status only, never decorative.
- **Light mode (operational screens only):** `surface-light #F5F7F9` ground, `ink-light
  #16222F` text, `line-light #E2E8F0` borders. Navy and gold remain the brand carriers;
  the accent does not change in light mode.

Contrast (all ratios measured, not assumed):

| Pair | Ratio | Verdict |
|---|---|---|
| `on-gold` on `gold-core` | 7.17:1 | AA + AAA |
| `on-gold` on `gold-light` | 11.24:1 | AAA |
| `text-primary` on `primary` | 15.9:1 | AAA |
| `text-body` on `primary` | 11.22:1 | AAA |
| `text-muted` on `primary` | 6.39:1 | AA |
| `gold-core` on `primary` | 7.17:1 | AA — safe as text |
| `gold-deep` on `primary` | 4.29:1 | AA for large text only; hairlines/decoration only |
| `success` on `navy-panel` | 5.34:1 | AA |
| `warning` on `navy-panel` | 5.43:1 | AA |
| `info` on `navy-panel` | 4.93:1 | AA |
| `danger` on `navy-panel` | 5.19:1 | AA |
| `success-deep` on `surface-light` | 4.81:1 | AA |
| `warning-deep` on `surface-light` | 5.52:1 | AA |
| `info-deep` on `surface-light` | 5.40:1 | AA |
| `danger-deep` on `surface-light` | 5.06:1 | AA |
| `muted-light` on `surface-light` | 5.05:1 | AA |

The semantic colours exist in **two sets on purpose — they are not interchangeable.**
The bright set (`success`, `warning`, `danger`, `info`) is for navy surfaces; the `-deep`
set is for light surfaces. Substituting one for the other fails WCAG AA: `success #43B02A`
is 5.34:1 on navy but only 2.61:1 on light. Use the matching set for the surface.

Never set `gold-deep` as text — it is a hairline and gradient-stop colour only.

## Typography

**Two faces, strictly separated by role.**

**Plus Jakarta Sans** is the *interface* voice — body copy, labels, buttons, nav, tables
and every number. It is a geometric grotesque that reads as engineered and modern without
the ubiquity of Inter, and it is already bundled, so there is no new dependency.

**Zentra Display** is the *brand* voice — the wordmark, the hero headline, and section
eyebrows ONLY. It is our own derived build: Marcellus (SIL Open Font License 1.1) renamed,
subset to the display charset, hand-kerned for the wordmark pairs and re-exported to
woff2 — see `tools/build_display_font.py`, which rebuilds it from the OFL source and
verifies the result. The OFL permits modification and self-hosting; the Reserved Font
Name rule is honoured by the rename. It is a *lapidary Roman* — flared serifs, high
stroke contrast, inscriptional capitals — which is the register the reference banner sits
in, and which a geometric sans cannot reach.

Because it is single-weight, **never set `font-weight` above 400 on `Zentra Display`** —
the browser will synthesise a faux-bold and smear the thin strokes. Hierarchy in the
display face comes from size and tracking, not weight.

- **Display face** — wordmark, hero h1, `.zeyebrow`. Tracking +0.02em to +0.28em
  (the wider the smaller). Uppercase only; it has no lowercase voice.
- **Interface face** — everything else. Never mix the two inside one sentence.

Weight discipline — this applies to **Plus Jakarta Sans** only; `Zentra Display` is
single-weight at 400. Only three weights exist in the interface family:

- **800** — display, h1, and numeric stats. The "engineered" voice.
- **700** — h2, h3, labels, buttons, nav. The working voice.
- **400/500** — body, eyebrows, micro labels.

Size and tracking carry hierarchy, not colour or boxes:

- **Display 72px / 400 / +0.02em (Zentra Display)** — the hero headline and one-per-page
  statements only. Gold foil applies to the accent word only, never the whole line.
- **Eyebrow 13px / 600 / 0.3em uppercase** — the "WELCOME TO" register. Wide tracking is
  what makes it feel luxury rather than shouty.
- **Micro 11.5px / 500 / 0.16em uppercase** — nav sub-labels, footer meta, the
  `SMARTER MANAGEMENT | GREATER VALUE` treatment.
- **Body 17px / 400 / 1.65** — paragraphs on navy. Never narrower than 15px.
- **Numeric 30px / 800** — dashboard figures. Pair with a 13px muted label underneath;
  never let a number sit without a label.

Two-gradient treatment is part of the type system, not an effect: the brand wordmark is
set twice — "ZENTRA" in a silver-white gradient, "ASSET" (the system name) in the gold
gradient. Applied to any other heading this becomes decoration; keep it to the lockup.

## Layout

- **Navy surfaces:** 8px base unit; section rhythm at 40 / 64 / 96px.
- **Content max width 1120px** for marketing and public pages; operational dashboards may
  run to 1440px with a 260px fixed nav rail.
- **Hero composition is asymmetric and fixed:** text panel left at ~40%, visual field
  right at ~60% bleeding to the viewport edge. Do **not** centre the hero — the off-centre
  split is a load-bearing part of the identity.
- **Four-column feature/benefit rows** with 1px gold hairline dividers between cells
  (fading at the ends). Use this once per page, immediately above the footer band, not as
  a general-purpose grid.
- **Two-column pairing rule:** any navy marketing section alternates copy-left / visual-right,
  then flips. One idea per section.
- Public pages are fully responsive; collapse the hero to a single column under 900px and
  drop the feature row to 2×2 under 720px.

## Elevation & Depth

Four levels, defined by surface *and* light, with shadows as the smallest component:

1. **Ground** — `primary #0B1B2E`. The page itself.
2. **Panel** — `navy-panel #12283F` + `divider-gold` hairline. Cards, nav rail sections.
3. **Elevated** — `navy-elevated #16304A` + 1px gold hairline at 50% + soft inner top
   highlight. Floating panels, dropdowns, device frames.
4. **Focus** — the primary action only: gold gradient plus a soft outer glow
   (`0 0 28px rgba(201,162,39,0.35)`). If more than one element on screen glows, remove
   the glow from all but the primary action.

Deliberately excluded: large soft black drop shadows, frosted blur over busy photography
without a real elevation system behind it.

## Shapes

- **Pill `999px`** — primary and ghost buttons, status badges, nav chips.
- **md `14px`** — the default card radius. This is the brand's signature radius.
- **lg `20px` / xl `28px`** — device frames, large glass panels, image masks.
- **sm `10px`** — inputs and small controls.
- **Circles** — the hero feature row and icon buttons. Circle for single glyphs, rounded
  square for anything with a label.
- **Icon language:** thin-stroke line icons at 1.5–2px, gold, always inside a geometric
  container (circle on navy, rounded square on light). Never place a bare stroke icon on
  navy without a container.
- **Hairlines** are a shape primitive: 1px gold at 40–60% opacity. Diagonal hairlines in
  panel corners are the system's only ornamental element — allow at most two on a page.

## Components

- **`button-primary`** — gold gradient pill, navy text, always uppercased with 0.12em
  tracking. It may carry a two-line lockup (bold action + small supporting line) and a
  trailing arrow. Exactly one per viewport. It always carries the `orbit` motion (see
  Motion) — the travelling light is what marks it as the primary action.
- **`button-ghost`** — gold outline/text on navy, fills to `navy-panel` on hover. All
  secondary actions. Two maximum per section.
- **`panel-navy` / `panel-glass`** — the two stacking levels. Every card on navy is one of
  these; no other card treatment exists.
- **`stat-card`** — numeric 800 + muted 13px label. The number never appears without its
  label, and never more than four per row.
- **`icon-tile` / `icon-circle`** — 44px rounded square in dense UI, 64px circle in hero.
  Icon stroke and container border both gold.
- **`nav-link` / `nav-link-active`** — body-md muted by default; active becomes gold and
  is marked by the gold hairline underline, not a filled pill.
- **`badge-status`** — pill, `label` typography, used for state only.
- **`divider-gold`** — the 1px rule. Structural sections use the full-width variant; cells
  inside a row use the fading variant.
- **`card-light`** — the light-mode exception, for dense operational screens only. Never
  used on a public marketing page.

## Motion

Motion is a material, not decoration: it imitates light on metal. Two motions exist in the
system, and nothing else animates on its own.

- **`orbit` — the primary action.** A single bright arc of gold travels once around the
  button border every **3.6s**, linear, forever. The ring itself never moves; only the
  gradient *angle* is animated, so the ring stays locked to the border radius at every
  frame. Reserved for `button-primary`: exactly one travelling light per viewport.
- **`shimmer` — icon discs.** A soft white-gold band crosses an `icon-circle` on a **5.2s**
  ease-in-out cycle, holding still for the first ~60% so it reads as a passing reflection
  rather than a repeating flash.

**Rules**

- Never animate `transform: rotate()` on an element to fake a travelling border: a rotating
  rectangle cannot follow a rounded border and the light breaks at the corners. Animate the
  gradient angle instead, using a registered `@property` of `syntax: "<angle>"`.
- Never store the gradient in a custom property and consume it via `var()` in another rule —
  the inner `var()` is resolved at declaration time, which silently kills the animation.
  Write the gradient inside the rule that paints it.
- A registered property with `inherits: false` must be *set on* the element that paints it.
  Setting it on an ancestor has no effect.
- Motion is never the only carrier of meaning, and any element that animates is decorative
  (`aria-hidden`) or already carries a static affordance.

**Reduced motion.** Under `prefers-reduced-motion: reduce` all animation stops and the
gradient is pinned to a static angle, so the button still reads as gold. Verified: the ring
keeps **1,807** gold pixels in reduced-motion vs **1,471** while animating, and screenshot
pairs differ — i.e. the animation genuinely stops rather than merely appearing to.

## Do's and Don'ts

**Do**
- Reach for navy + gold as the default for any new Zentra surface; only the Assets and
  Zentra Legal mock-ups are currently off-system and should be migrated to these tokens.
- Express metallic gold as a gradient and carry the same gradient across favicon,
  watermark, and device chrome so the mark is recognisable at 16px.
- Use one gold element per viewport as the focal point (usually the primary action).
- Keep the feature row to exactly four items and the benefit band to exactly four items.
- Reuse Plus Jakarta Sans; do not introduce a serif or a second family.

**Don't**
- Don't use flat gold, or gold as body text. `gold-core` is AA-safe as a short label on
  navy (7.17:1) but never for paragraphs, and never on light surfaces.
- Don't add drop shadows or default glassmorphism to create depth — use the navy panel
  levels and hairlines.
- Don't centre-page the hero, and don't replace "ZENTRA" silver / "ASSET" gold with a
  single-colour wordmark.
- Don't let dashboard figures appear without labels, or exceed four stat cards in a row.
- Don't invent new accents per system (no per-product teal or mint); the existing
  `#00A3B5` teal and `#7EDCC8` mint in the Zentra ID mock-up are **not** part of this
  system and should be retired during migration.
- Don't use stock photography of people, or emoji.
