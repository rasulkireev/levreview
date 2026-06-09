# Technology Stack

## Runtime

- Python 3.10
- Django 4.x
- Node.js via `.nvmrc` (`lts/gallium`, Node 16 era)
- npm with `package-lock.json`
- Poetry with `poetry.lock`
- PostgreSQL-style database configuration through `DATABASE_URL`

## Backend

- Django is the application framework.
- `django-environ` loads runtime configuration from environment variables and `.env`.
- `django-allauth` owns signup, login, email confirmation, and account routes.
- `users.CustomUser` is the active user model and keeps the database table name `auth_user`.
- `django-model-utils` provides `TimeStampedModel` for `Location` and `Review`.
- `dj-stripe` and `stripe` support subscription checkout, customer portal, and subscription sync.
- `django-anymail` is configured for Mailgun, although email is currently forced to console backend in settings.
- `sentry-sdk` is initialized outside debug mode.
- `whitenoise` serves static assets in production.
- `django-widget-tweaks` is used to render Django form fields with Tailwind classes in templates.

## Frontend

- Server-rendered Django templates are the primary UI layer.
- Tailwind CSS is the main styling system.
- Bootstrap is present as a dependency but new UI should prefer Tailwind unless touching existing Bootstrap-dependent code.
- Stimulus powers small interactive behavior.
- Turbo/Hotwire assets are bundled through `frontend/src/application/hotwire.js`.
- Webpack builds assets into `frontend/build/` and emits `manifest.json` for `python-webpack-boilerplate`.
- PostCSS uses Tailwind, nesting, autoprefixer, `postcss-preset-env`, and cssnano in production.
- Marketing typography loads Google Fonts for Sora and Public Sans in `templates/pages/home.html`.

## Important Integrations

- Google Maps Places autocomplete is used for location creation.
- Google review redirect uses `search.google.com/local/writereview?placeid=...`.
- Stripe checkout and billing portal are used for subscriptions.
- Mailgun is configured through Anymail.
- Plausible analytics is included in base templates.
- Sentry is configured for production error tracking.
- CapRover receives Docker image deployments from GitHub Actions.

## Configuration

Required settings are read from environment variables. Commonly needed values include:

- `ENVIRONMENT`
- `SECRET_KEY`
- `DEBUG`
- `ALLOWED_HOSTS`
- `DATABASE_URL`
- `MAILGUN_API_KEY`
- `STRIPE_LIVE_SECRET_KEY`
- `STRIPE_TEST_SECRET_KEY`
- `STRIPE_LIVE_MODE`
- `dsn` for Sentry outside debug mode

Do not commit real values for any of these. When adding new configuration, prefer typed environment access in Django settings and document the variable.

## Source Of Truth

- Python dependency intent: `pyproject.toml`
- Python lockfile: `poetry.lock`
- Deployment Python requirements: `requirements.txt`, generated from Poetry
- JavaScript dependency intent and lockfile: `package.json`, `package-lock.json`
- Frontend entrypoints: `frontend/src/application/*.js`
- Tailwind scan paths: `tailwind.config.js`
- Production settings overlay: `levreview/settings/prod.py`

## Formatting And Linting

- Black line length is 120.
- isort uses the Django profile.
- djLint uses the Django profile with project-specific ignored rules.
- ESLint is configured for browser/node JavaScript and requires semicolons.
- Stylelint uses `stylelint-config-standard-scss`.
- Pre-commit runs YAML checks, EOF/trailing whitespace fixes, Black, isort, djLint, and requirements export.

## Testing

- Django tests use `django.test.TestCase`.
- `pages/tests.py` currently covers robots, sitemap, and canonical host behavior.
- `core/tests.py` and `users/tests.py` are placeholders and should receive focused tests when those apps change.
- There is no configured JavaScript test runner. For frontend behavior changes, prefer small Stimulus code and verify through asset build plus browser interaction.

## Deployment

- GitHub Actions deploys pushes to `main`.
- The workflow builds and pushes a Docker image to GHCR, then deploys to CapRover.
- Docker builds frontend assets in a Node image and runs Django in Python 3.10.
- `deployment/entrypoint.sh` collects static files, runs migrations, and starts Gunicorn.

## Technical Constraints

- Keep server-rendered templates as the default. Do not introduce a SPA layer without explicit approval.
- Preserve existing URL names and route shapes unless a migration/redirect plan is part of the task.
- Treat billing, auth, email confirmation, and external webhooks as high-risk surfaces.
- Move hardcoded service values to environment-backed settings when touching the relevant integration.
- Keep dependency upgrades deliberate and tested; this app has older framework and tooling versions.
