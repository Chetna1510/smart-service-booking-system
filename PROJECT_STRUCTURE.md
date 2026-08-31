# Project Structure

Global static files and templates are shared across both apps, following Django best practices — one place to update styling, no duplication.

```
smart-service-booking-system/
├── manage.py
├── requirements.txt
├── booking_system/            # Project settings, root URLs
├── accounts/                   # Auth, dashboards, superadmin
│   ├── models.py              # UserProfile
│   ├── views.py                # register, login, dashboard, superadmin_*
│   └── urls.py
├── bookings/                    # Marketplace logic
│   ├── models.py               # ProviderProfile, Service, Availability,
│   │                            # Booking, Notification, SearchQuery
│   ├── views.py
│   ├── signals.py              # auto-creates notifications on booking events
│   └── urls.py
├── templates/
│   ├── base.html               # public pages (login, register, home)
│   ├── dashboard_base.html     # authenticated pages (sidebar layout)
│   ├── accounts/
│   ├── bookings/
│   └── superadmin/
└── static/
    ├── css/                    # base.css, dashboard.css, + per-page CSS
    └── js/main.js
```

## Templates

Two base templates, extended by everything else:

- **`base.html`** — public pages. Blocks: `title`, `extra_css`, `header_subtitle`, `content`, `extra_js`.
- **`dashboard_base.html`** — authenticated pages (sidebar nav). Blocks: `title`, `extra_css`, `page_title`, `page_subtitle`, `header_actions`, `dashboard_content`, `extra_js`.

```html
{% extends 'base.html' %}
{% block content %}...{% endblock %}
```

```html
{% extends 'dashboard_base.html' %}
{% block dashboard_content %}...{% endblock %}
```

## Static Files

- CSS → `static/css/`, JS → `static/js/`, images → `static/images/`
- Reference with `{% load static %}` and `{% static 'css/base.css' %}`
- Before deploying: `python manage.py collectstatic`

## Settings

```python
TEMPLATES = [{'DIRS': [BASE_DIR / 'templates'], 'APP_DIRS': True, ...}]
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

`SECRET_KEY` comes from the `DJANGO_SECRET_KEY` env var (falls back to a placeholder locally). `ALLOWED_HOSTS` / `CSRF_TRUSTED_ORIGINS` are set for the Render domain — update them if you deploy elsewhere.

## App Responsibilities

| App | Owns |
|---|---|
| `accounts` | Login/registration, `UserProfile` (role: user/provider/superadmin), dashboards, superadmin panel |
| `bookings` | Everything marketplace-related — services, availability, bookings, notifications, search logging |

## "I want to change X" — where to look

| Task | Edit |
|---|---|
| Add/change a page's HTML | `templates/accounts/` or `templates/bookings/` (extend a base template — see above) |
| Add a URL | app's `urls.py`, then wire it to a view in that app's `views.py` |
| Add/change a database field | app's `models.py`, then `python manage.py makemigrations && migrate` |
| Change global styling | `static/css/base.css` (public pages) or `static/css/dashboard.css` (authenticated pages) |
| Auto-fire something on a booking event | `bookings/signals.py` |
| Restrict a view to superadmins only | wrap it with `@superadmin_required` (defined in `accounts/views.py`) |

## Common Workflows

**Add a field to an existing model**
```bash
# 1. Add the field in models.py
# 2. Generate and apply the migration
python manage.py makemigrations
python manage.py migrate
```

**Add a new page**
1. Create the template, extending `base.html` (public) or `dashboard_base.html` (authenticated).
2. Add the view function in the app's `views.py`.
3. Register the path in the app's `urls.py`.
