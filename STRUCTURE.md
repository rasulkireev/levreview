# Project Structure

## Root

- `manage.py`: Django command entrypoint.
- `pyproject.toml`: Poetry dependencies and Python formatting configuration.
- `requirements.txt`: exported deployment requirements.
- `package.json`: Webpack, Tailwind, Stimulus, and frontend scripts.
- `tailwind.config.js`: Tailwind content scanning.
- `postcss.config.js`: PostCSS pipeline.
- `Dockerfile`: production image build.
- `.github/workflows/deploy-prod.yml`: GHCR and CapRover deployment.
- `deployment/`: runtime entrypoint and server configuration files.

## Django Project

- `levreview/settings/__init__.py`: base settings and environment-driven configuration.
- `levreview/settings/prod.py`: production overrides for hosts, HTTPS, HSTS, and file logging.
- `levreview/urls.py`: root URL includes for pages, admin, auth, users, core, Stripe, robots, and sitemap.
- `levreview/middleware.py`: canonical host redirect middleware.
- `levreview/sitemaps.py`: static-page sitemap definitions.
- `levreview/utils.py`: shared form error rendering.

Keep project-level files limited to cross-app configuration, routing, middleware, and shared utilities.

## Django Apps

### `pages/`

Marketing/static pages and the authenticated dashboard view.

- `views.py`: `TemplateView` pages and dashboard context assembly.
- `urls.py`: home, dashboard, privacy, terms, contact.
- `tests.py`: SEO routes and canonical host behavior.
- Templates live under `templates/pages/` and `templates/pages/components/`.

### `core/`

Location and review intake domain.

- `models.py`: `Location` and `Review`.
- `forms.py`: creation forms for locations and reviews.
- `views.py`: create/detail views for locations and reviews.
- `urls.py`: location creation, location detail, review creation, review detail.
- Templates live under `templates/core/`.

`Location.google_place_id` is unique and drives public review links. `Location.min_rating` controls whether a rating goes to Google or private feedback. `Review` stores private feedback for ratings below that threshold.

### `users/`

Account, settings, email confirmation, Stripe customer, and subscription behavior.

- `models.py`: `CustomUser`.
- `forms.py`: allauth login/signup overrides and minimum-rating form.
- `views.py`: settings, rating threshold updates, checkout, customer portal, Stripe webhook handler.
- `signals.py`: creates a dj-stripe customer after email confirmation.
- `utils.py`: adds user/customer/subscription/location context to dashboard templates.
- Templates live under `templates/account/`.

Be careful with the `CustomUser` table name, allauth assumptions, and dj-stripe customer/subscription relationships.

## Templates

- `templates/base.html`: public/marketing base with SEO metadata, Plausible, and frontend packs.
- `templates/dbase.html`: authenticated dashboard shell with sidebar and account state.
- `templates/components/`: shared footer, messages, and email confirmation components.
- `templates/pages/components/`: marketing page sections and dashboard subcomponents.
- `templates/account/components/`: settings, customer, and app preference sections.

Prefer extracting repeated UI into focused includes. Keep template names descriptive and colocated by product area.

## Frontend Assets

- `frontend/src/application/hotwire.js`: imports Tailwind CSS, starts Stimulus, registers third-party controllers, and exposes the Google Maps callback.
- `frontend/src/controllers/*_controller.js`: one Stimulus controller per browser behavior.
- `frontend/src/styles/tailwind.css`: Tailwind imports and project component layer.
- `frontend/src/styles/google-maps.css`: Google Maps-specific styles.
- `frontend/vendors/`: copied static vendor assets such as logos and images.
- `frontend/webpack/`: shared, development, production, and watch Webpack configs.
- `frontend/build/`: generated assets, ignored by git and produced by Webpack.

New Stimulus controller filenames should use snake case with `_controller.js`; data-controller names become kebab-case in templates. Existing `frontend/src/controllers/minRating_controller.js` and `data-controller="minRating"` are legacy exceptions. Do not rename them casually because templates may depend on the current identifier.

## URL And Naming Patterns

- Route names use lower-kebab style, for example `create-location`, `detail-location`, `create-review`, and `update-min-rating`.
- Prefer `reverse` and `reverse_lazy` in Python.
- Keep public URLs stable. Some existing routes intentionally lack trailing slashes, such as `dashboard` and location review URLs.
- Template block names are standard Django blocks: `meta`, `extra_head`, `extra_top_js`, `content`, `footer`, and `extra_bottom_js`.

## Data Model Boundaries

- Users own locations through `Location.owner`.
- Locations own private reviews through `Review.location`.
- A user's default `min_rating` is copied into new locations and can update existing locations through settings.
- Google Place ID is the external identifier for location review links.
- Stripe customer/subscription state comes from dj-stripe, not custom billing tables.

Do not rename related names or route kwargs casually; templates and views depend on them.

## Migrations

- New model or field changes need a new migration in the owning app.
- Do not edit historical migrations unless explicitly asked.
- Keep data migrations small and reversible when possible.
- Any production data shape change should be reflected in tests or a documented migration note.

## Tests

- Tests are colocated in each app's `tests.py`.
- Add tests near the app whose behavior changes.
- Use Django's test client for routes, redirects, template responses, and sitemap/robots assertions.
- Mock external services for Stripe, Mailgun, Sentry, and Google Maps.

## Documentation Files

- `AGENTS.md`: root operating instructions for coding agents.
- `PRODUCT.md`: product purpose, users, features, and business goals.
- `VISION.md`: long-term direction and non-goals.
- `TECH.md`: frameworks, dependencies, configuration, and deployment.
- `STRUCTURE.md`: file organization and architectural boundaries.
- `DESIGN.md`: visual identity, tokens, and UI guidance.

Update these files when the actual product, architecture, stack, or design direction changes.
