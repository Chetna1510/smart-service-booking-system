# Superadmin Guide

## Access

```bash
python manage.py create_superadmin
```
Creates `superadmin` / `admin123` — **change the password after first login.**

Log in at `/login/`, then visit `/superadmin/` (or click "Superadmin Panel" in the sidebar). Every view is gated by the `superadmin_required` decorator; non-superadmins are redirected to the regular dashboard with an error message.

## Sections

| URL | Purpose |
|---|---|
| `/superadmin/` | Dashboard: user/service/booking counts, completed-booking revenue, total booked hours, last-6-months revenue by month, recent users & bookings, top services by booking count |
| `/superadmin/users/` | Search and filter users by type; **activate/deactivate** any account; **reset a password** to a chosen value |
| `/superadmin/services/` | Search and filter all services by category or active/inactive status |
| `/superadmin/notifications/` | Send a bulk notification (system, booking, message, or reminder) to all users, customers only, or providers only |

## Security

Superadmin status is the `user_type = 'superadmin'` field on `UserProfile` — not a separate permission system. Grant it by editing that field directly (e.g. via Django admin or shell) or by running `create_superadmin`.

## "I want to change X" — where to look

| Task | Edit |
|---|---|
| Add a new stat to the dashboard | `superadmin_dashboard` view in `accounts/views.py` (compute it, add to `context`) → `templates/superadmin/dashboard.html` (display it) |
| Add a new user filter/search field | `superadmin_users` view — extend the `Q()` filter chain, add the field to the form in `templates/superadmin/users.html` |
| Add a new bulk-action on a user (beyond activate/reset password) | Add a new `elif action == '...'` branch in `superadmin_users`, plus a button posting that `action` value from the template |
| Change who can receive bulk notifications | `recipient_type` branch in `superadmin_notifications` (`accounts/views.py`) |
| Restrict any new view to superadmins | Wrap it with `@superadmin_required` |

## Troubleshooting

- **"You do not have permission to access this page"** → the logged-in user's `UserProfile.user_type` isn't `'superadmin'`.
- **Redirected to login instead of the panel** → not authenticated at all; log in first.
- **A superadmin change (e.g. password reset) isn't reflected** → these views use plain POST + redirect (no AJAX), so a stale page or a missing form `action`/CSRF token is the usual cause.
