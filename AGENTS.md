# AGENTS.md

Root instructions for AI coding agents working in Lev Review.

## Start

- Read `PRODUCT.md`, `VISION.md`, `TECH.md`, `STRUCTURE.md`, and `DESIGN.md` before broad product, UI, architecture, or dependency work.
- Use `rg` and `rg --files` for discovery. Read the relevant models, forms, views, templates, controllers, tests, and settings before changing behavior.
- Keep changes focused. Do not bundle unrelated cleanup, redesign, dependency upgrades, and feature work into one patch.
- Prefer existing Django, template, Tailwind, and Stimulus patterns over introducing new frameworks.
- Do not add secrets, API keys, tokens, credentials, private customer data, or local `.env` values to the repo.

## Project Map

- Product surface: local-business Google review routing and private feedback capture.
- Django apps:
  - `pages/`: marketing, dashboard, static pages, sitemap/SEO route coverage.
  - `core/`: locations, review capture, Google Place ID flows.
  - `users/`: custom user model, account settings, email confirmation, Stripe customer/subscription actions.
  - `levreview/`: settings, root URLs, middleware, sitemap helpers, shared form utilities.
- UI surface:
  - Marketing pages extend `templates/base.html`.
  - Authenticated dashboard pages extend `templates/dbase.html`.
  - Frontend behavior lives in `frontend/src/controllers/*_controller.js` and is loaded by `frontend/src/application/hotwire.js`.

## Commands

- Install Python deps: `poetry install`
- Install JS deps: `npm install`
- Build frontend assets: `npm run build`
- Watch frontend assets during local development: `npm run watch`
- Start webpack dev server: `npm run start`
- Run Django checks: `poetry run python manage.py check`
- Run all Django tests: `poetry run python manage.py test`
- Run focused tests: `poetry run python manage.py test pages`
- Apply migrations locally: `poetry run python manage.py migrate`
- Start Django locally: `poetry run python manage.py runserver`
- Docs-only verification: `git diff --check`

The Django app expects environment variables loaded through `django-environ` and `.env`. If a command fails because local secrets or service configuration are missing, report the missing variable or service clearly instead of inventing dummy production values.

## Code Style

- Python is formatted with Black at line length 120 and import-sorted with the Django isort profile.
- Django code should stay boring: models in `models.py`, form customization in `forms.py`, route behavior in views, reusable template context in small helpers.
- Use named URLs and `reverse`/`reverse_lazy`; do not hardcode internal paths in Python when a route name exists.
- Keep database changes migration-backed. Do not edit existing migrations unless the user explicitly asks for migration surgery.
- JavaScript should remain Stimulus-first. Add a controller only when behavior belongs in the browser; keep server-rendered pages server-rendered.
- Existing JavaScript uses semicolons and ES modules. Match that style.
- Templates use Django templates, `widget_tweaks`, Tailwind utilities, and small includes. Keep includes cohesive and named by their UI role.

## Testing

- Add or update Django tests for behavior changes, especially routing, middleware, forms, review routing, dashboard context, billing actions, auth, and sitemap/SEO output.
- `pages/tests.py` has real route and canonical host coverage. `core/tests.py` and `users/tests.py` are currently placeholders, so do not assume coverage exists there.
- For Stripe, Mailgun, Sentry, and Google Maps work, mock external services unless the user explicitly asks for a live integration test.
- For template/UI changes, run `npm run build` when asset classes, controllers, or CSS are touched. Use a browser check when interaction or responsive layout changes.
- For documentation-only changes, `git diff --check` is sufficient unless a referenced command or generated artifact was changed.

## Product And Design Guardrails

- The product promise is simple: happy customers go to Google, unhappy customers go to a private feedback path first.
- Keep the operator's workflow visible. Avoid abstract SaaS decoration, fake dashboards, generic card grids, and hype copy.
- Follow `DESIGN.md` for new marketing UI. The current dashboard has older gray/orange Tailwind patterns; improve it gradually when touching those screens.
- Preserve accessibility: real labels or `sr-only` labels, keyboard focus states, WCAG AA contrast where feasible, and reduced-motion alternatives for decorative motion.
- Do not build features that manipulate, suppress, or fake public reviews. The product routes feedback and helps operators recover issues.

## Security And Privacy

- Customer feedback can contain personal information. Treat review names, emails, and feedback as private operational data.
- Do not log secrets, raw payment payloads, or customer feedback unless the log is intentionally scoped and safe.
- Keep CSRF protections on unsafe requests. Be careful with `csrf_exempt`; Stripe webhook behavior should be deliberate and tested.
- New public endpoints need an explicit access decision: anonymous, authenticated, owner-only, or external webhook.
- Hardcoded service configuration should be moved toward environment-backed settings when touched.

## Dependencies

- Python dependency source of truth is `pyproject.toml` plus `poetry.lock`; `requirements.txt` is exported for deployment.
- If Python dependencies change, update `pyproject.toml`, `poetry.lock`, and regenerated `requirements.txt`.
- JavaScript dependency source of truth is `package.json` plus `package-lock.json`; use npm, not pnpm or yarn.
- Do not swap Django, Tailwind, Bootstrap, Stimulus, Webpack, allauth, dj-stripe, or deployment tooling without explicit approval.

## Deployment Notes

- Production deploy builds a Docker image through `.github/workflows/deploy-prod.yml`, pushes to GHCR, then deploys to CapRover.
- `Dockerfile` builds frontend assets in a Node stage and serves Django from Python 3.10.
- `deployment/entrypoint.sh` runs `collectstatic`, `migrate`, and Gunicorn on port 80.
- Static assets depend on `frontend/build/manifest.json` generated by Webpack and consumed by `python-webpack-boilerplate`.

## Pull Requests

- Keep PRs small and single-purpose.
- Use conventional commit language when committing, for example `docs: add AI project guidance`.
- In handoff notes, include what changed, what was verified, and any test or environment gaps.
