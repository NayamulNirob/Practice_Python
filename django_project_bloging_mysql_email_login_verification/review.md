# Code Review

Reviewed the Django blog project with a focus on authentication, account verification, deployment settings, and basic maintainability. Findings are ordered by severity.

## Findings

### Critical: Production settings expose the app and use a committed secret

[`settings.py`](django_project_bloging_mysql_email_login_verification/settings.py#L25) hard-codes a `django-insecure-` secret key, enables `DEBUG`, and accepts every host (`ALLOWED_HOSTS = ['*']`, lines 28–30). If this configuration is deployed, debug pages can disclose sensitive configuration and request data, the known key can undermine signed values and sessions, and the unrestricted host list removes host-header protection.

**Recommendation:** Load `SECRET_KEY` from the environment, fail startup if it is missing in production, set `DEBUG` from an explicit environment setting, and configure the actual allowed hostnames. Rotate the key if this value has ever been used in a deployed environment.

### High: Unverified passwords are stored as plaintext

[`register`](users/views.py#L18) saves `password1` directly to `PendingUser.password` at line 33. The password remains recoverable from the database until verification, and could persist indefinitely because pending records have no expiration or cleanup. A database leak therefore exposes credentials users may reuse elsewhere.

**Recommendation:** Never store the raw password. Hash it before saving and use a flow that can safely set the account password after verification, or create an inactive user with Django's password-hashing APIs and activate it after verification. Add expiry and cleanup for abandoned registrations.

### High: The custom authentication backend can authenticate inactive users

[`PendingUserBackend.authenticate`](users/backends.py#L9) checks a user's password and returns the user directly at line 19. This overrides Django's normal `ModelBackend` authentication path without calling `user_can_authenticate`, so users marked inactive can still log in through this backend.

**Recommendation:** Call `self.user_can_authenticate(user)` before returning the user, and add a regression test for inactive accounts.

### Medium: Verification is a state-changing GET with no expiry

[`verify_account`](users/views.py#L60) creates an account and deletes its pending record on a GET request. Email security scanners commonly open links automatically, which can activate an account before its owner does. The UUID token has no expiration check, so pending credentials and links remain valid indefinitely.

**Recommendation:** Use a confirmation flow that requires a deliberate POST after opening the link, and reject tokens past a defined expiration time. Keep verification tokens single use.

### Medium: Registration can fail on duplicate pending emails

[`UserRegistrationForm.clean_email`](users/forms.py#L14) checks for an existing `User`, but not an existing `PendingUser`. Since [`PendingUser.email`](users/models.py) is unique, submitting another registration for the same not-yet-verified email can raise an uncaught database `IntegrityError` instead of returning a form error or resending verification.

**Recommendation:** Check pending registrations during form validation and provide a deliberate resend or duplicate-registration response.

### Medium: Container starts Django's development server

[`Dockerfile`](Dockerfile#L19) runs `manage.py runserver` on `0.0.0.0`. Django's development server is not intended for production traffic and lacks production server behavior such as robust worker handling.

**Recommendation:** Run a production WSGI/ASGI server in deployed containers and keep `runserver` for local development.

## Additional notes

- [`verify_account`](users/views.py#L84) sends `str(e)` to the user on unexpected exceptions. This can expose internal error details; log the exception server-side and show a generic message.
- [`logout_view`](users/views.py#L92) logs users out via GET. Make logout a POST action to avoid link previews or cross-site navigation triggering a state change.
- [`README.md`](README.md) describes SQLite as the default, but [`settings.py`](django_project_bloging_mysql_email_login_verification/settings.py#L81) requires MySQL environment variables. Align the documented setup with the actual database configuration.
- Both app test modules contain only empty `TestCase` scaffolding. Add coverage for registration, verification expiry/replay, inactive-user login, and post ownership before relying on these flows.

## Review scope and verification

This was a static review of the repository's application code, templates, settings, deployment file, and test scaffolding. Tests were not run; the findings above should be confirmed with focused tests as fixes are made.
