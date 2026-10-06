# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Django Management
- **Run Server**: `python manage.py runserver`
- **Create Migrations**: `python manage.py makemigrations`
- **Apply Migrations**: `python manage.py migrate`
- **Create Superuser**: `python manage.py createsuperuser`

### Testing
- **Run All Tests**: `python manage.py test`
- **Run App Tests**: `python manage.py test <app_name>`
- **Run Single Test Class**: `python manage.py test <app_name>.tests.<TestClass>`

## Architecture & Structure

### High-Level Layout
The project is a standard Django application. The root directory contains `manage.py` and the core configuration folder `django_project/`.

### Key Applications
- **`users`**: Manages authentication and user identities.
    - **User Model**: Uses Django's default `User` model.
    - **Profiles**: Implements a custom `Profile` model with a `OneToOneField` to `User` to handle extended user data (e.g., profile images).
- **`blog`**: The primary application for blog content management.

### Core Patterns
- **Authentication**: Handled within the `users` app using custom forms and views for registration and profile updates.
- **Media Storage**: User-uploaded files are stored in the `media/` directory.
- **Database**: Configured for SQLite by default, with a migration path to MySQL defined in `plan.md`.
