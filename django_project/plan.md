# Implementation Plan: MySQL Migration and Flexible Authentication System

## 1. Overview
This document outlines the complete process for migrating the project's database from SQLite to MySQL and implementing a flexible login system that allows authentication via email address, or a combination of email and username.

## 2. Goal 1: MySQL Database Migration

### 2.1 Dependency Updates
**File:** `requirements.txt`
- **Action:** Add `mysqlclient` to the dependencies list.
- **Reason:** `mysqlclient` is the recommended MySQL driver for Django, providing better performance and stability than PyMySQL as it is a C-extension.

### 2.2 Project Configuration
**File:** `django_project/settings.py`
- **Action:** Update the `DATABASES` configuration.
- **Implementation:**
  ```python
  import os

  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': os.environ.get('DB_NAME', 'django_db'),
          'USER': os.environ.get('DB_USER', 'db_user'),
          'PASSWORD': os.environ.get('DB_PASSWORD', 'db_password'),
          'HOST': os.environ.get('DB_HOST', 'localhost'),
          'PORT': os.environ.get('DB_PORT', '3306'),
          'OPTIONS': {
              'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
          },
      }
  }
  ```

### 2.3 Manual Database Setup (Required Action)
Before running the server, the following SQL commands must be executed in the MySQL shell:
```sql
-- 1. Create the database with utf8mb4 for full unicode support
CREATE DATABASE django_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 2. Create a dedicated database user
CREATE USER 'db_user'@'localhost' IDENTIFIED BY 'db_password';

-- 3. Grant all privileges on the specific database to the user
GRANT ALL PRIVILEGES ON django_db.* TO 'db_user'@'localhost';

-- 4. Apply changes
FLUSH PRIVILEGES;
```

### 2.4 Schema Migration
- **Action:** Run the following command in the terminal:
  ```bash
  python manage.py migrate
  ```
- **Result:** This creates all necessary Django and application tables within the MySQL database.

---

## 3. Goal 2: Flexible Login System Implementation

### 3.1 Custom Authentication Backend
**File to Create:** `users/backends.py`
- **Logic:** Implement a class `CustomAuthBackend` inheriting from `django.contrib.auth.backends.ModelBackend`.
- **Detailed Logic for `authenticate()` method:**
    1. **Scenario: Email + Username provided**
       - Attempt to find a user where `User.objects.get(email=email, username=username)`.
    2. **Scenario: Only one identifier provided**
       - If the input looks like an email, attempt to find a user where `User.objects.get(email=email)`.
       - Otherwise, attempt to find a user where `User.objects.get(username=username)`.
    3. **Password Verification:**
       - If a user is found, verify the password using `user.check_password(password)`.
       - Return the user object if successful, otherwise return `None`.

### 3.2 Backend Registration
**File:** `django_project/settings.py`
- **Action:** Register the custom backend.
- **Implementation:**
  ```python
  AUTHENTICATION_BACKENDS = [
      'users.backends.CustomAuthBackend',
      'django.contrib.auth.backends.ModelBackend', # Fallback
  ]
  ```

### 3.3 Custom Authentication Form
**File:** `users/forms.py`
- **Action:** Create `FlexibleAuthenticationForm` inheriting from `django.contrib.auth.forms.AuthenticationForm`.
- **Implementation:**
    - Add `email = forms.EmailField(required=False, label="Email Address")`.
    - Override `clean()`: Ensure that either `username` or `email` is provided. If both are empty, raise a `ValidationError`.

### 3.4 View Integration
**File:** `django_project/urls.py`
- **Action:** Update the login route to use the new form.
- **Implementation:**
  ```python
  from django.contrib.auth import views as auth_views
  from users.forms import FlexibleAuthenticationForm

  urlpatterns = [
      # ... other paths
      path('login/', auth_views.LoginView.as_view(
          template_name='users/login.html', 
          authentication_form=FlexibleAuthenticationForm
      ), name='login'),
  ]
  ```

### 3.5 Template Update
**File:** `users/templates/users/login.html`
- **Action:** Ensure the login form explicitly renders the `email` field.
- **Implementation:** Use `{{ form.email }}` or ensure `{{ form.as_p }}` is used to automatically include the new field.

---

## 4. Implementation Sequence
1. **MySQL Setup:** `requirements.txt` $\rightarrow$ `settings.py` $\rightarrow$ MySQL Shell $\rightarrow$ `python manage.py migrate`.
2. **Auth Backend:** Create `users/backends.py` $\rightarrow$ Update `settings.py` (AUTHENTICATION_BACKENDS).
3. **Auth Form/View:** Create `FlexibleAuthenticationForm` in `users/forms.py` $\rightarrow$ Update `urls.py` $\rightarrow$ Verify `login.html`.

## 5. Verification Plan
| Test Case | Input | Expected Result |
| :--- | :--- | :--- |
| **MySQL Connectivity** | Start server | Server starts without DB errors |
| **Login via Email** | Valid Email + Password | Successful Login |
| **Login via Email+User**| Valid Email + Valid User + Password | Successful Login |
| **Login via Username** | Valid Username + Password | Successful Login |
| **Invalid Auth** | Wrong Password / Missing Fields | Login Failure with Error Message |
