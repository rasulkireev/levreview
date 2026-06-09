---
version: alpha
name: Lev Review
description: Reputation routing for local businesses. Calm, precise, operator-focused, and quietly futuristic.
colors:
  primary: "#07100D"
  primaryRaised: "#10231D"
  surface: "#F4F7F2"
  surfaceRaised: "#FFFFFF"
  surfaceDark: "#0B1714"
  text: "#07100D"
  textMuted: "#465B54"
  textSubtle: "#5D7169"
  border: "#C9D8CF"
  accent: "#F97316"
  accentHover: "#EA580C"
  success: "#22C55E"
  successSoft: "#6EE7B7"
  warning: "#FB923C"
  star: "#FBBF24"
  danger: "#EF4444"
  onPrimary: "#FFFFFF"
  onSurface: "#07100D"
typography:
  display:
    fontFamily: Sora
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: 0px
  h1:
    fontFamily: Sora
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: 0px
  h2:
    fontFamily: Sora
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.12
    letterSpacing: 0px
  h3:
    fontFamily: Public Sans
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0px
  body:
    fontFamily: Public Sans
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: 0px
  bodyLarge:
    fontFamily: Public Sans
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0px
  label:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0px
rounded:
  sm: 6px
  md: 8px
  lg: 12px
  full: 9999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  section: 80px
components:
  buttonPrimary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.onPrimary}"
    rounded: "{rounded.md}"
    padding: 12px
    height: 48px
  buttonPrimaryHover:
    backgroundColor: "{colors.primaryRaised}"
    textColor: "{colors.onPrimary}"
    rounded: "{rounded.md}"
    padding: 12px
    height: 48px
  buttonAccent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.onSurface}"
    rounded: "{rounded.md}"
    padding: 12px
    height: 48px
  buttonAccentHover:
    backgroundColor: "{colors.accentHover}"
    textColor: "{colors.onSurface}"
    rounded: "{rounded.md}"
    padding: 12px
    height: 48px
  buttonSecondary:
    backgroundColor: "{colors.surfaceRaised}"
    textColor: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: 12px
    height: 48px
  consolePanel:
    backgroundColor: "{colors.surfaceDark}"
    textColor: "{colors.onPrimary}"
    rounded: "{rounded.md}"
    padding: 24px
  pricingPanel:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.onSurface}"
    rounded: "{rounded.md}"
    padding: 32px
  feedbackInput:
    backgroundColor: "{colors.surfaceRaised}"
    textColor: "{colors.text}"
    rounded: "{rounded.md}"
    padding: 12px
    height: 44px
  bodyText:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.textMuted}"
    typography: "{typography.body}"
  subtleText:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.textSubtle}"
    typography: "{typography.label}"
  divider:
    backgroundColor: "{colors.border}"
    textColor: "{colors.primary}"
    height: 1px
  statusSuccess:
    backgroundColor: "{colors.success}"
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    padding: 8px
  statusSoft:
    backgroundColor: "{colors.successSoft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    padding: 8px
  statusWarning:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    padding: 8px
  starIndicator:
    backgroundColor: "{colors.star}"
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    padding: 4px
  errorPanel:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: 16px
---

# Lev Review Design System

## Overview

Lev Review should feel like a focused reputation operations console for local businesses. The visual direction is calm, precise, trustworthy, and slightly future-facing. The UI should help a busy operator understand the routing mechanism quickly: one customer link, two possible outcomes.

The current marketing page establishes the canonical direction: deep green-black hero surfaces, off-white operational sections, emerald proof/status accents, and orange as the active Lev Review signal. New UI should extend that world instead of falling back to generic SaaS layouts.

Dashboard screens still contain older Tailwind gray/orange patterns. When touching those screens, improve them toward this system without doing unrelated redesign work.

## Colors

Use deep green-black as the primary environment color. It should feel operational and grounded, not nightclub-dark or blue-slate SaaS. Off-white surfaces create room for explanation, pricing, and forms. Orange is the product accent and call-to-action color. Emerald and green communicate reputation health, routing success, and safe progress.

- `primary` is the main dark background and text color.
- `surface` is the default light page band.
- `surfaceDark` is for dashboard-like previews and compact console modules.
- `accent` is for primary product action, routing markers, and numbered steps.
- `successSoft` is for status pills, progress, and positive route signals.
- `warning` is for private recovery routing, not generic errors.
- `danger` is reserved for actual destructive or failed states.

Do not introduce purple gradients, gray-heavy SaaS palettes, beige branding, blue corporate dashboards, or decorative bokeh/orbs.

## Typography

Use Sora for display headings and important numeric values. Use Public Sans for body copy, controls, forms, navigation, and dashboard text. Keep headings confident but not oversized inside dashboard panels or forms.

Letter spacing should be `0px`. Do not add negative tracking to new components. Use weight, scale, and spacing for hierarchy.

## Layout

Prefer full-width page bands with constrained inner content (`max-w-7xl`, responsive padding). Marketing pages should show the product mechanism in the first viewport, then workflow, then pricing. Operational screens should be dense but calm, with clear scanning paths and obvious primary actions.

Use grids when comparing flows or pricing. Avoid nested cards. Cards are acceptable for repeated items, pricing tiers, modals, and genuinely framed tools. The 3D/futuristic feeling should come from precision, contrast, measured grids, and real workflow states rather than decoration.

## Elevation & Depth

Keep elevation restrained. The marketing hero can use subtle glass/console treatment with low-opacity borders and blur. Dashboard surfaces should rely on borders, spacing, and background contrast more than shadow stacks.

Use shadows only when a surface is floating over another surface, such as menus, popovers, and transient overlays.

## Shapes

Default radius is 8px. Use 6px for small inputs or badges, 12px only for larger panels that need a softer feel, and full radius for pills/status indicators. Do not make large, pill-shaped text buttons by default.

## Components

- Primary actions: dark green or orange depending on context. On orange backgrounds, prefer dark text when contrast allows; if using white text on orange, verify contrast or darken the orange.
- Secondary actions: transparent or white surfaces with clear borders and focus rings.
- Forms: visible labels or `sr-only` labels, strong focus rings, and clear error blocks.
- Status pills: short, specific labels such as `public`, `private`, `Pro`, `Free`, or `verified`.
- Console previews: show real product states like ratings, Google-ready percentage, private feedback, location count, or follow-up timing.
- Icons: use existing Heroicons-style SVGs unless the project adds an icon library deliberately.

## Do's and Don'ts

Do show the review routing mechanism before explaining surrounding features.

Do make the operator's next action obvious: create location, share link, review feedback, update rating threshold, or manage subscription.

Do keep pricing direct and legible. Avoid burying plan differences in decoration.

Do preserve keyboard focus, `sr-only` text for icon-only controls, and reduced-motion alternatives.

Don't create fake analytics noise, decorative abstract dashboards, or generic SaaS card grids.

Don't use purple, blue-slate, beige, or gray-dominant themes for new product surfaces.

Don't add animation that delays or obscures the review path.

Don't make low-rating feedback feel punitive. It is a recovery path, not a shame path.
