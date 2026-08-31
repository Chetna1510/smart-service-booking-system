# Smart Service Booking System

A Django web app where service providers (salons, tutors, cleaners, therapists, etc.) list services and availability, and customers search, browse, and book appointments online.

## Project Structure

```
smart-service-booking-system/
├── manage.py
├── requirements.txt
├── booking_system/        # Project settings, root URLs
├── accounts/               # Auth, dashboards, superadmin
│   ├── models.py          # UserProfile
│   ├── views.py
│   └── urls.py
├── bookings/                # Services, availability, bookings
│   ├── models.py          # ProviderProfile, Service, Availability, Booking, Notification
│   ├── views.py
│   ├── signals.py
│   └── urls.py
├── templates/               # Global templates (base.html, dashboard_base.html, ...)
└── static/                  # Global CSS/JS
```

## Features

- **Accounts**: Registration and login for Customers and Service Providers, with a role-aware dashboard.
- **Services**: Providers create, edit, and manage the services they offer.
- **Availability & Booking**: Providers publish open time slots; customers browse, search, and book them.
- **Notifications**: In-app alerts for bookings, cancellations, and reminders.
- **Superadmin Panel**: Platform-wide analytics, user management, service management, and bulk notifications.

## How to Run the Project

1. **Navigate to the project directory:**
   ```bash
   cd smart-service-booking-system/
   ```

2. **Activate the virtual environment:**
   ```bash
   source venv/bin/activate
   ```

3. **Install dependencies and apply migrations:**
   ```bash
   pip install -r requirements.txt
   python manage.py migrate
   ```

4. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

5. **Open your browser:**
   ```
   http://127.0.0.1:8000/
   ```

## Key URLs

| Page | URL |
|---|---|
| Home | `/` |
| Register (User / Provider) | `/register/user/` · `/register/provider/` |
| Login / Logout | `/login/` · `/logout/` |
| Dashboard | `/dashboard/` |
| Browse Providers | `/browse-providers/` |
| My Bookings | `/my-bookings/` |
| My Services (Provider) | `/my-services/` |
| Superadmin Panel | `/superadmin/` |

## Technologies Used

- Django 6.0.2
- Bootstrap 5.3 + Bootstrap Icons
- SQLite (default Django database)
- WhiteNoise (static files) + Gunicorn (deployment, e.g. Render)

## File Locations for VS Code

Open the `smart-service-booking-system` folder directly in VS Code to edit the files.
