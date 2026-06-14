# Product

## Overview

Lev Review is Google review management software for local businesses. It gives each location a review link that routes satisfied customers to Google and routes unhappy customers to a private feedback form first.

The product promise is direct: collect more public reviews without ignoring unhappy customers.

## Target Users

Local business owners, managers, and operators who depend on Google reviews but do not have a dedicated reputation-management team. They are usually checking the site between customer interactions, after closing, or while setting up a new location, and they need the product to feel trustworthy, fast, and easy to understand.

Primary users include:

- Restaurant, cafe, salon, clinic, shop, and service-business operators.
- Multi-location owners who need separate links and thresholds per location.
- Managers who want a simple private channel for bad experiences before they become public reviews.
- Non-technical users who may not know Google Place IDs, webhooks, or SEO terminology.

## Product Purpose

Lev Review helps businesses collect more public Google reviews while routing unhappy customers to a private feedback path first. Success means a visitor quickly understands that the product protects reputation, works for one or many locations, and can be started without a sales process.

## Core Workflow

1. A user signs up and confirms email.
2. The user creates a location using Google Places data.
3. Lev Review creates a shareable review link for that location.
4. A customer chooses a star rating.
5. Ratings at or above the location's `min_rating` redirect to Google review writing.
6. Ratings below the threshold open a private feedback form.
7. The operator reviews submitted private feedback in the dashboard.

This workflow is the product center. New features should make it easier to set up, share, understand, or act on.

## Key Features

- Location creation from Google Places autocomplete.
- Unique Google Place ID tracking per location.
- Configurable minimum rating threshold.
- Public Google redirect for satisfied customers.
- Private feedback capture with optional name and email.
- Dashboard with locations and recent review activity.
- Email confirmation gate before location creation.
- Free and Pro pricing surfaces.
- Stripe checkout and customer portal for subscription management.
- SEO pages, sitemap, robots.txt, canonical host behavior, and structured data for the marketing site.

## Business Objectives

- Make the free plan useful enough that a local business can start immediately.
- Convert serious operators to Pro when private recovery details and customization matter.
- Build trust through clear pricing, low setup friction, SEO credibility, and reliable operational behavior.
- Keep the product narrow enough to maintain quickly while improving the review recovery loop.

## Brand Personality

Calm, precise, and future-facing. The brand should feel like a quiet operations console for customer reputation: measured, confident, and technically current without becoming cold or abstract.

## Design Principles

- Show the review-routing mechanism before explaining it in detail.
- Keep the operator's job in focus: collect reviews, catch issues, protect the location.
- Use futuristic cues as signal and precision, not sci-fi decoration.
- Make pricing and setup feel direct, legible, and low-friction.
- Keep orange as the Lev Review accent while building a richer world around deep green, emerald, and off-white.
- Prefer real workflow states over fake dashboard decoration.

See `DESIGN.md` for tokens and concrete UI guidance.

## Anti-references

Avoid generic SaaS card grids, purple gradients, startup hype copy, fake dashboard noise, corporate blandness, and gray-heavy pages. The site should not look like a template with interchangeable icons and soft shadows.

## Accessibility & Inclusion

Target WCAG AA contrast, clear focus states, keyboard-accessible navigation, readable text at small screen sizes, and reduced-motion alternatives for decorative transitions.

The product serves busy operators and their customers. Keep language plain, controls obvious, forms forgiving, and mobile layouts reliable.

## Product Guardrails

- Do not build review manipulation, fake-review, review-buying, or public suppression features.
- Do not make unhappy customers feel punished for honest feedback.
- Do not expand into a general CRM, ticketing, or survey suite unless the feature directly strengthens the review recovery workflow.
- Do not add integrations that require ongoing maintenance before the core location/review/subscription flow is strong.
- Do not bury setup behind a sales process.
