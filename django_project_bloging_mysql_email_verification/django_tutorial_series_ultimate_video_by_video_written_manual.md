# Python Django Tutorial: Full-Featured Web App — Complete Video-by-Video Manual

This document is a complete, exhaustive written companion to all 17 videos in Corey Schafer's **Python Django Tutorial: Full-Featured Web App** series. It details every command, code file, migration step, shell experiment, and deployment configuration across the entire playlist.

---

## Table of Contents
1. [Video 1: Getting Started](#video-1-getting-started)
2. [Video 2: Applications and Routes](#video-2-applications-and-routes)
3. [Video 3: Templates](#video-3-templates)
4. [Video 4: Admin Page](#video-4-admin-page)
5. [Video 5: Database and Migrations](#video-5-database-and-migrations)
6. [Video 6: User Registration](#video-6-user-registration)
7. [Video 7: Login and Logout System](#video-7-login-and-logout-system)
8. [Video 8: User Profile and Picture](#video-8-user-profile-and-picture)
9. [Video 9: Update User Profile](#video-9-update-user-profile)
10. [Video 10: Create, Update, and Delete Posts (Class-Based Views)](#video-10-create-update-and-delete-posts-class-based-views)
11. [Video 11: Pagination](#video-11-pagination)
12. [Video 12: Email and Password Reset](#video-12-email-and-password-reset)
13. [Video 13: AWS S3 File Uploads](#video-13-aws-s3-file-uploads)
14. [Video 14: Environment Variables and Secret Keys](#video-14-environment-variables-and-secret-keys)
15. [Video 15: Deploying to an Ubuntu Linux Server](#video-15-deploying-to-an-ubuntu-linux-server)
16. [Video 16: Custom Domain & SSL Setup](#video-16-custom-domain--ssl-setup)
17. [Video 17: Common Deployment Errors & Troubleshooting](#video-17-common-deployment-errors--troubleshooting)

---

## Video 1: Getting Started

### 1. Conceptual Overview
Django is a high-level Python web framework that follows the **MVT (Model-View-Template)** architecture. It promotes rapid development, clean design, and comes with built-in tools for security, database routing, and user management.

### 2. Step-by-Step Environment Setup
#### Terminal Setup (Windows PowerShell / Command Prompt)
```powershell
# Navigate to working directory
cd C:\Users\SEBPO\Documents\GitHub\Practice_Python_to_Al

# Create project folder
mkdir django_project
cd django_project

# Create a virtual environment named .venv
py -m venv .venv

# Activate the virtual environment
# On Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# On Windows CMD:
.\.venv\Scripts\activate.bat
# On macOS / Linux:
source .venv/bin/activate
```

#### Installing Django
```powershell
# Upgrade pip to latest version
py -m pip install --upgrade pip

# Install Django
pip install django
```

#### Creating the Initial Django Project
Run `django-admin startproject` with a trailing dot (`.`). The trailing dot instructs Django to initialize the project inside the current folder rather than creating a nested directory structure (`django_project/django_project/manage.py`).

```powershell
django-admin startproject django_project .
```

### 3. File Structure & Explanation
```text
django_project/
│── .venv/                   # Virtual environment dependencies
│── manage.py                # Command-line utility for project management
└── django_project/          # Inner project package
    ├── __init__.py          # Indicates this directory is a Python package
    ├── asgi.py              # Asynchronous Server Gateway Interface entry point
    ├── settings.py          # Master configuration file for Django
    ├── urls.py              # Master URL routing declarations
    └── wsgi.py              # Web Server Gateway Interface entry point for deployment
```

* **`manage.py`**: Interacts with your project to run local servers, execute migrations, launch shells, and create apps.
* **`settings.py`**: Controls database engines, installed apps, middleware, template configurations, static asset paths, and security settings.
* **`urls.py`**: Routes incoming HTTP requests to specific views or app URL sub-routings.

### 4. Running the Development Server
```powershell
py manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser. You will see Django's default rocket launch success page. To stop the server press `Ctrl + C`.

---

## Video 2: Applications and Routes

### 1. Project vs. Application Concept
* **Project:** The complete web infrastructure (settings, database connection, master URL routes, global middleware).
* **App:** A self-contained web module designed to perform a dedicated function (e.g., `blog`, `users`, `store`). A project can contain multiple apps.

### 2. Creating the `blog` App
```powershell
py manage.py startapp blog
```

Generated `blog/` structure:
```text
blog/
│── migrations/          # Database migration files tracking schema changes
│── __init__.py
│── admin.py             # Registers models to Django Admin UI
│── apps.py              # Configuration settings for the blog app
│── models.py            # Database models / ORM schema
│── tests.py             # Automated unit test definitions
└── views.py             # Python functions/classes handling request/response logic
```

### 3. Writing Views (`blog/views.py`)
Views accept web request objects (`HttpRequest`) and return responses (`HttpResponse` or rendered HTML).

```python
# blog/views.py
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Blog Home</h1>')

def about(request):
    return HttpResponse('<h1>Blog About</h1>')
```

### 4. App URL Routing (`blog/urls.py`)
Create a new file `urls.py` inside the `blog` directory:

```python
# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
```

### 5. Wiring App URLs into Master URL Router (`django_project/urls.py`)
Include the `blog.urls` inside the root project URL dispatcher using `include()`:

```python
# django_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')), # Routes root domain requests to blog app
]
```

### 6. Registering the App (`django_project/settings.py`)
Add `'blog.apps.BlogConfig'` to `INSTALLED_APPS`:

```python
# django_project/settings.py
INSTALLED_APPS = [
    'blog.apps.BlogConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

---

## Video 3: Templates

### 1. The Django Template Engine & Directory Namespacing
Returning raw HTML strings from views is unmaintainable. Django looks for templates in an app's subfolder structured as `templates/<app_name>/`. This namespacing (`blog/templates/blog/`) prevents collision with identically named templates in other installed apps.

### 2. Creating Dummy Context Data & Updating Views (`blog/views.py`)
```python
# blog/views.py
from django.shortcuts import render

# Dummy data dictionary list representing blog posts before database integration
posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
```

### 3. Template Inheritance — Master Skeleton (`blog/templates/blog/base.html`)
Template inheritance allows shared HTML layout elements (headers, navigation bars, footers, CSS links) to be written once.

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS CDN -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    
    <!-- Custom CSS -->
    <link rel="stylesheet" type="text/css" href="{% static 'blog/main.css' %}">

    {% if title %}
        <title>Django Blog - {{ title }}</title>
    {% else %}
        <title>Django Blog</title>
    {% endif %}
</head>
<body>
    <header class="site-header">
      <nav class="navbar navbar-expand-md navbar-dark bg-steel fixed-top">
        <div class="container">
          <a class="navbar-brand mr-4" href="{% url 'blog-home' %}">Django Blog</a>
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggle">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarToggle">
            <div class="navbar-nav mr-auto">
              <a class="nav-item nav-link" href="{% url 'blog-home' %}">Home</a>
              <a class="nav-item nav-link" href="{% url 'blog-about' %}">About</a>
            </div>
          </div>
        </div>
      </nav>
    </header>

    <main role="main" class="container">
      <div class="row">
        <div class="col-md-8">
          {% block content %}{% endblock %}
        </div>
      </div>
    </main>

    <!-- Bootstrap JS dependencies -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
</body>
</html>
```

### 4. Child Templates (`home.html` & `about.html`)
`blog/templates/blog/home.html`:
```html
{% extends "blog/base.html" %}
{% block content %}
    {% for post in posts %}
        <article class="media content-section">
          <div class="media-body">
            <div class="article-metadata">
              <a class="mr-2" href="#">{{ post.author }}</a>
              <small class="text-muted">{{ post.date_posted }}</small>
            </div>
            <h2><a class="article-title" href="#">{{ post.title }}</a></h2>
            <p class="article-content">{{ post.content }}</p>
          </div>
        </article>
    {% endfor %}
{% endblock content %}
```

`blog/templates/blog/about.html`:
```html
{% extends "blog/base.html" %}
{% block content %}
    <h1>About Page</h1>
{% endblock content %}
```

### 5. Adding Static Files (`blog/static/blog/main.css`)
Place static files inside `blog/static/blog/main.css`:

```css
body {
  background: #fafafa;
  color: #333333;
  margin-top: 5rem;
}

.bg-steel {
  background-color: #5f788a;
}

.content-section {
  background: #ffffff;
  padding: 10px 20px;
  border: 1px solid #dddddd;
  border-radius: 3px;
  margin-bottom: 20px;
}

.article-title {
  color: #444444;
}

.article-title:hover {
  color: #428bca;
  text-decoration: none;
}
```

---

## Video 4: Admin Page

### 1. Database Migrations Initialization
Django comes pre-configured with default apps (`auth`, `admin`, `contenttypes`, `sessions`). Apply initial default migrations to create core system tables.

```powershell
py manage.py migrate
```

### 2. Creating Administrative Superuser Account
Run `createsuperuser` command and enter username, email, and password:

```powershell
py manage.py createsuperuser
```

Example session:
```text
Username (leave blank to use 'SEBPO'): nayamul
Email address: nayamul@example.com
Password: ********
Password (again): ********
Superuser created successfully.
```

### 3. Accessing Admin Interface
1. Run local server: `py manage.py runserver`
2. Open browser: `http://127.0.0.1:8000/admin/`
3. Log in with your superuser credentials. You can manage Users and Groups out of the box.

---

## Video 5: Database and Migrations

### 1. Defining Models (`blog/models.py`)
Django ORM translates Python model classes into database tables.

```python
# blog/models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
```

* **`models.CharField`**: For short strings with a specified `max_length`.
* **`models.TextField`**: Unrestricted text content.
* **`models.DateTimeField(default=timezone.now)`**: Sets current UTC time while preserving overrides.
* **`models.ForeignKey(User, on_delete=models.CASCADE)`**: Many-to-One relationship (one user can author many posts). `CASCADE` automatically deletes all posts if the user account is deleted.

### 2. Generating & Inspecting Migrations
```powershell
# Step 1: Generate migration file based on model changes
py manage.py makemigrations

# Step 2 (Optional): Inspect SQL generated for a migration
py manage.py sqlmigrate blog 0001

# Step 3: Apply migrations to the actual database file (db.sqlite3)
py manage.py migrate
```

### 3. Registering Models in Django Admin (`blog/admin.py`)
```python
# blog/admin.py
from django.contrib.admin import admin
from .models import Post

admin.site.register(Post)
```

### 4. Interactive Python Shell Experiments & Common Pitfalls
Launch the shell: `py manage.py shell`

#### Complete Terminal Experiment Breakdown & Mechanics
```python
# Correct Imports
from blog.models import Post
from django.contrib.auth.models import User

# Pitfall 1: Incorrect module/class case imports
# >>> from blog.models import post    --> ImportError (Python is case-sensitive)
# >>> from blog.models import posts   --> ImportError

# Pitfall 2: Syntax errors on imports
# >>> from django.contrib.auth.models user --> SyntaxError (missing 'import')

# Pitfall 3: Typo in 'objects' manager
# >>> User.object.all()  --> AttributeError: type object 'User' has no attribute 'object'.

# Fetching records via Manager
User.objects.all()                   # Returns QuerySet of all User instances
user_1 = User.objects.first()        # Returns first User object instance
user_last = User.objects.last()      # Returns last User object instance

# Filter vs Get/First Mechanics
qs = User.objects.filter(username='nayamul') # Returns a QuerySet [<User: nayamul>]
# >>> qs.id  --> AttributeError: 'QuerySet' object has no attribute 'id'
# Rule: QuerySets are list-like containers. Individual attributes exist on instances, not QuerySets.

u = User.objects.get(id=1) # Returns single User object instance: <User: nayamul>
u.id                       # Returns: 1
u.pk                       # Returns primary key: 1

# Creating Post instances
# Method A: Assign User instance directly to foreign key field
post_1 = Post(title='Blog 1', content='first post content!', author=u)

# Pitfall 4: Forgetting parentheses when saving
# >>> post_1.save  --> Returns bound method reference without executing SQL write!
post_1.save() # Executes INSERT INTO blog_post statement

# Method B: Assigning ID integer directly to the synthesized _id field
post_2 = Post(title='Blog 2', content='Second Post content', author_id=u.id)
post_2.save()

# Method C: Reverse relationship manager (User -> Posts)
u.post_set.all() # Returns QuerySet of posts authored by this user
u.post_set.create(title='Blog 3', content='Content of Third post!') # Instantiates and saves in 1 step!
```

### 5. Connecting Real Database Objects to Views (`blog/views.py`)
Replace the hardcoded dummy list with real ORM queries:

```python
# blog/views.py
from django.shortcuts import render
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
```

---

## Video 6: User Registration

### 1. Creating the `users` Application
```powershell
py manage.py startapp users
```
Add `'users.apps.UsersConfig'` to `INSTALLED_APPS` inside `django_project/settings.py`.

### 2. Creating Custom Registration Form (`users/forms.py`)
Django provides a built-in `UserCreationForm`. We inherit from it to add an email field.

```python
# users/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']
```

### 3. Writing Registration View with Flash Messages (`users/views.py`)
Django's **Messages Framework** allows passing temporary notifications between HTTP requests.

```python
# users/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() # Hashes password and persists user to database
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
```

### 4. Flash Message Display in Base Template (`blog/templates/blog/base.html`)
Add message loops inside `base.html` directly above content block:

```html
<main role="main" class="container">
  <div class="row">
    <div class="col-md-8">
      {% if messages %}
        {% for message in messages %}
          <div class="alert alert-{{ message.tags }}">
            {{ message }}
          </div>
        {% endfor %}
      {% endif %}
      {% block content %}{% endblock %}
    </div>
  </div>
</main>
```

### 5. Registration Template (`users/templates/users/register.html`)
Must include `{% csrf_token %}` to protect forms from Cross-Site Request Forgery attacks.

```html
{% extends "blog/base.html" %}
{% block content %}
    <div class="content-section">
        <form method="POST">
            {% csrf_token %}
            <fieldset class="form-group">
                <legend class="border-bottom mb-4">Join Today</legend>
                {{ form.as_p }}
            </fieldset>
            <div class="form-group">
                <button class="btn btn-outline-info" type="submit">Sign Up</button>
            </div>
        </form>
        <div class="border-top pt-3">
            <small class="text-muted">
                Already Have An Account? <a class="ml-2" href="{% url 'login' %}">Sign In</a>
            </small>
        </div>
    </div>
{% endblock content %}
```

---

## Video 7: Login and Logout System

### 1. Registering Auth Views (`django_project/urls.py`)
Django provides class-based views for user authentication (`LoginView` and `LogoutView`).

```python
# django_project/urls.py
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', user_views.logout_view, name='logout'),
    path('', include('blog.urls')),
]
```

### 2. Login Template (`users/templates/users/login.html`)
```html
{% extends "blog/base.html" %}
{% block content %}
    <div class="content-section">
        <form method="POST">
            {% csrf_token %}
            <fieldset class="form-group">
                <legend class="border-bottom mb-4">Log In</legend>
                {{ form.as_p }}
            </fieldset>
            <div class="form-group">
                <button class="btn btn-outline-info" type="submit">Login</button>
            </div>
        </form>
        <div class="border-top pt-3">
            <small class="text-muted">
                Need An Account? <a class="ml-2" href="{% url 'register' %}">Sign Up Now</a>
            </small>
        </div>
    </div>
{% endblock content %}
```

### 3. Logout Template (`users/templates/users/logout.html`)
#Since `GET` requests can no longer be used with Django's `logout` method, we must use the `POST` method.
```html
{% extends "blog/base.html" %}
{% block content %}
    <h2>You have been Log Out</h2>
    <form action="{% url 'logout' %}" method="post">
        {% csrf_token %}
    </form>
    <div class="border-top pt-3">
        <small class="text-muted">
            <a href="{% url 'login' %}">Login again</a>
        </small>
    </div>
{% endblock content %}
```
### 4. Logout  (`users/views.py`)
#### The built-in logout method is no longer working due to the 'GET' method, so we have used a custom method for it.
```
def logout_view(request):
    logout(request)
    return render(request,'users/logout.html')
```

### 5. Configuring Login Settings (`django_project/settings.py`)
```python
# Redirect settings after authentication actions
LOGIN_REDIRECT_URL = 'blog-home'
LOGIN_URL = 'login'
```

### 6. Access Control Decorator (`users/views.py`)
Use `@login_required` to block unauthenticated visitors from accessing views:

```python
# users/views.py
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'users/profile.html')
```

---

## Video 8: User Profile and Picture

### 1. Profile Model Definition (`users/models.py`)
Extend the base `User` model using a 1-to-1 relationship mapping.

```python
# users/models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
```

### 2. Installing Pillow, Migrating, and Admin Registration
```powershell
# Install Pillow imaging library for handling ImageField
pip install Pillow

# Generate and apply migrations for Profile model
py manage.py makemigrations
py manage.py migrate
```

Register `Profile` in `users/admin.py`:
```python
# users/admin.py
from django.contrib import admin
from .models import Profile

admin.site.register(Profile)
```

### 3. Automated Profile Creation via Signals (`users/signals.py`)
Use Django post-save signals to generate a `Profile` instance automatically whenever a `User` record is created.

```python
# users/signals.py
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
```

Register the signals module inside `users/apps.py`:
```python
# users/apps.py
from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import users.signals
```

### 4. Configuring Media File Delivery (`settings.py` & `urls.py`)
In `django_project/settings.py`:
```python
import os

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

In `django_project/urls.py`:
```python
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## Video 9: Update User Profile

### 1. Creating Update Forms (`users/forms.py`)
```python
# users/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
```

### 2. Dual Form Processing View (`users/views.py`)
Handle both `UserUpdateForm` and `ProfileUpdateForm` inside a single view endpoint. Note the use of `request.FILES` for image payload uploads.

```python
# users/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile') # Prevents POST reload warnings via PRG Pattern
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
```

### 3. Profile Template Update (`users/templates/users/profile.html`)
Form elements handling files **must** specify `enctype="multipart/form-data"`.

```html
{% extends "blog/base.html" %}
{% block content %}
    <div class="content-section">
      <div class="media">
        <img class="rounded-circle account-img" src="{{ user.profile.image.url }}">
        <div class="media-body">
          <h2 class="account-heading">{{ user.username }}</h2>
          <p class="text-secondary">{{ user.email }}</p>
        </div>
      </div>
      <form method="POST" enctype="multipart/form-data">
          {% csrf_token %}
          <fieldset class="form-group">
              <legend class="border-bottom mb-4">Profile Info</legend>
              {{ u_form.as_p }}
              {{ p_form.as_p }}
          </fieldset>
          <div class="form-group">
              <button class="btn btn-outline-info" type="submit">Update</button>
          </div>
      </form>
    </div>
{% endblock content %}
```

### 4. Automated Image Resizing with Pillow (`users/models.py`)
Override the model's `save()` method to auto-scale uploaded profile images larger than 300x300 pixels:

```python
# users/models.py
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) # Call parent save method

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
```

---

## Video 10: Create, Update, and Delete Posts (Class-Based Views)

### 1. Refactoring Views to Class-Based Views (`blog/views.py`)
Class-Based Views (CBVs) reduce boilerplate for common patterns like list displays, detail pages, and form handlings.

```python
# blog/views.py
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post

# Displays list of posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']      # Displays newest posts first

# Displays individual post
class PostDetailView(DetailView):
    model = Post

# Creates a new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user # Sets logged-in user as post author
        return super().form_valid(form)

# Updates an existing post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author # Ensures only post author can edit

# Deletes a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
```

### 2. Post Model Redirect Target (`blog/models.py`)
Define `get_absolute_url` so Django knows where to route users after post creation.

```python
# blog/models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
```

### 3. URL Dispatcher Mapping (`blog/urls.py`)
```python
# blog/urls.py
from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
```

### 4. CBV Template Definitions
#### Detail Template (`blog/templates/blog/post_detail.html`)
```html
{% extends "blog/base.html" %}
{% block content %}
  <article class="media content-section">
    <div class="media-body">
      <div class="article-metadata">
        <a class="mr-2" href="#">{{ object.author }}</a>
        <small class="text-muted">{{ object.date_posted|date:"F d, Y" }}</small>
        {% if object.author == user %}
          <div>
            <a class="btn btn-secondary btn-sm mt-1 mb-1" href="{% url 'post-update' object.id %}">Update</a>
            <a class="btn btn-danger btn-sm mt-1 mb-1" href="{% url 'post-delete' object.id %}">Delete</a>
          </div>
        {% endif %}
      </div>
      <h2 class="article-title">{{ object.title }}</h2>
      <p class="article-content">{{ object.content }}</p>
    </div>
  </article>
{% endblock content %}
```

#### Form Template (`blog/templates/blog/post_form.html`)
Used for both creation and update actions.

```html
{% extends "blog/base.html" %}
{% block content %}
    <div class="content-section">
        <form method="POST">
            {% csrf_token %}
            <fieldset class="form-group">
                <legend class="border-bottom mb-4">Blog Post</legend>
                {{ form.as_p }}
            </fieldset>
            <div class="form-group">
                <button class="btn btn-outline-info" type="submit">Post</button>
            </div>
        </form>
    </div>
{% endblock content %}
```

#### Confirm Delete Template (`blog/templates/blog/post_confirm_delete.html`)
```html
{% extends "blog/base.html" %}
{% block content %}
    <div class="content-section">
        <form method="POST">
            {% csrf_token %}
            <fieldset class="form-group">
                <legend class="border-bottom mb-4">Delete Post</legend>
                <h2>Are you sure you want to delete the post "{{ object.title }}"?</h2>
            </fieldset>
            <div class="form-group">
                <button class="btn btn-outline-danger" type="submit">Yes, Delete</button>
                <a class="btn btn-outline-secondary" href="{% url 'post-detail' object.id %}">Cancel</a>
            </div>
        </form>
    </div>
{% endblock content %}
```

---

## Video 11: Pagination

### 1. Adding Pagination to List Views (`blog/views.py`)
Add `paginate_by` attribute to `ListView`. Create `UserPostListView` to filter posts belonging to a single user.

```python
# blog/views.py
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
```

### 2. URL Configuration for User Posts (`blog/urls.py`)
```python
# blog/urls.py
path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
```

### 3. Navigation Controls Template Snippet (`blog/templates/blog/home.html`)
```html
{% if is_paginated %}

  {% if page_obj.has_previous %}
    <a class="btn btn-outline-info mb-4" href="?page=1">First</a>
    <a class="btn btn-outline-info mb-4" href="?page={{ page_obj.previous_page_number }}">Previous</a>
  {% endif %}

  {% for num in page_obj.paginator.page_range %}
    {% if page_obj.number == num %}
      <a class="btn btn-info mb-4" href="?page={{ num }}">{{ num }}</a>
    {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
      <a class="btn btn-outline-info mb-4" href="?page={{ num }}">{{ num }}</a>
    {% endif %}
  {% endfor %}

  {% if page_obj.has_next %}
    <a class="btn btn-outline-info mb-4" href="?page={{ page_obj.next_page_number }}">Next</a>
    <a class="btn btn-outline-info mb-4" href="?page={{ page_obj.paginator.num_pages }}">Last</a>
  {% endif %}

{% endif %}
```

---

## Video 12: Email and Password Reset

### 1. Registering Password Reset Routes (`django_project/urls.py`)
Django includes four views to handle password resets via email securely.

```python
# django_project/urls.py
from django.contrib.auth import views as auth_views

urlpatterns = [
    # ... previous routes ...
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]
```

### 2. Configuring SMTP Settings (`django_project/settings.py`)
```python
import os

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')
```

### 3. Reset Password Templates
`users/templates/users/password_reset.html`:
```html
{% extends "blog/base.html" %}
{% block content %}
    <div class="content-section">
        <form method="POST">
            {% csrf_token %}
            <fieldset class="form-group">
                <legend class="border-bottom mb-4">Reset Password</legend>
                {{ form.as_p }}
            </fieldset>
            <div class="form-group">
                <button class="btn btn-outline-info" type="submit">Request Password Reset</button>
            </div>
        </form>
    </div>
{% endblock content %}
```

`users/templates/users/password_reset_done.html`:
```html
{% extends "blog/base.html" %}
{% block content %}
    <div class="alert alert-info">
        An email has been sent with instructions to reset your password.
    </div>
{% endblock content %}
```

`users/templates/users/password_reset_confirm.html`:
```html
{% extends "blog/base.html" %}
{% block content %}
    <div class="content-section">
        <form method="POST">
            {% csrf_token %}
            <fieldset class="form-group">
                <legend class="border-bottom mb-4">Reset Password</legend>
                {{ form.as_p }}
            </fieldset>
            <div class="form-group">
                <button class="btn btn-outline-info" type="submit">Reset Password</button>
            </div>
        </form>
    </div>
{% endblock content %}
```

`users/templates/users/password_reset_complete.html`:
```html
{% extends "blog/base.html" %}
{% block content %}
    <div class="alert alert-info">
        Your password has been reset successfully.
    </div>
    <a href="{% url 'login' %}">Sign In Here</a>
{% endblock content %}
```

---

## Video 13: AWS S3 File Uploads

### 1. Why AWS S3?
Storing media files locally on production application servers presents major risks: files can be lost when instances restart, and scaling horizontally across multiple web servers breaks local storage. Amazon S3 provides reliable cloud asset storage.

### 2. Package Installation
```powershell
pip install boto3 django-storages
```

### 3. Configuring S3 Parameters (`django_project/settings.py`)
Add `storages` to `INSTALLED_APPS` and configure keys:

```python
# django_project/settings.py
INSTALLED_APPS = [
    # ...
    'storages',
]

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_REGION_NAME = 'us-east-1'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
```

---

## Video 14: Environment Variables and Secret Keys

### 1. Rationale
Never commit hardcoded credentials, secret keys, or passwords to public source repositories (like GitHub).

### 2. Setting Variables per Platform
#### Windows PowerShell (Current Session)
```powershell
$env:SECRET_KEY="my-secret-key-value"
$env:EMAIL_USER="myemail@gmail.com"
$env:EMAIL_PASS="my-app-password"
```

#### Windows Permanent (CMD / System Properties)
```cmd
setx SECRET_KEY "my-secret-key-value"
setx EMAIL_USER "myemail@gmail.com"
setx EMAIL_PASS "my-app-password"
```

#### Linux / macOS (`~/.bashrc` or `~/.zshrc`)
```bash
export SECRET_KEY='my-secret-key-value'
export EMAIL_USER='myemail@gmail.com'
export EMAIL_PASS='my-app-password'
```

### 3. Reading Variables in Settings (`django_project/settings.py`)
```python
import os

SECRET_KEY = os.environ.get('SECRET_KEY')
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')
```

---

## Video 15: Deploying to an Ubuntu Linux Server

### 1. Provisioning & Initial System Setup
SSH into your Ubuntu server and update packages:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv nginx git ufw -y
```

### 2. Configuring Firewall
```bash
sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'
sudo ufw enable
```

### 3. Cloning Project & Virtual Environment Setup
```bash
git clone https://github.com/yourusername/django_project.git
cd django_project

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
pip install gunicorn

python manage.py collectstatic
python manage.py migrate
```

### 4. Gunicorn Systemd Service Creation
Create `/etc/systemd/system/gunicorn.service`:

```ini
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/django_project
ExecStart=/home/ubuntu/django_project/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/ubuntu/django_project/gunicorn.sock django_project.wsgi:application

[Install]
WantedBy=multi-user.target
```

Start and enable Gunicorn daemon:
```bash
sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```

### 5. Nginx Reverse Proxy Configuration
Create `/etc/nginx/sites-available/django_project`:

```nginx
server {
    listen 80;
    server_name your_server_ip_or_domain;

    location /static/ {
        root /home/ubuntu/django_project;
    }

    location /media/ {
        root /home/ubuntu/django_project;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/django_project/gunicorn.sock;
    }
}
```

Enable site block and restart Nginx:
```bash
sudo ln -s /etc/nginx/sites-available/django_project /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

---

## Video 16: Custom Domain & SSL Setup

### 1. DNS Configuration
In your domain registrar dashboard, add the following records:
* **A Record:** `@` pointing to your server's public IP address.
* **CNAME Record:** `www` pointing to `@`.

### 2. Certbot SSL Installation
Install Certbot for Nginx to obtain a free SSL certificate from Let's Encrypt:

```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

### 3. Verifying Certificate Renewal
Certbot sets up an automated timer. Test renewal with:
```bash
sudo certbot renew --dry-run
```

---

## Video 17: Common Deployment Errors & Troubleshooting

### 1. Logging Diagnostics Commands
When issues arise on production servers (`DEBUG = False`), check system logs:

```bash
# Check Gunicorn execution status
sudo systemctl status gunicorn

# Read last 50 entries in Gunicorn journal logs
sudo journalctl -u gunicorn --no-pager -n 50

# Check Nginx error logs in real-time
sudo tail -f /var/log/nginx/error.log
```

### 2. Comprehensive Troubleshooting Matrix

| Issue | Root Cause | Solution |
| :--- | :--- | :--- |
| **500 Internal Server Error** | Python runtime exception while `DEBUG = False`. | Inspect `journalctl -u gunicorn` tracebacks for missing variables or broken database queries. |
| **Static CSS / JS 404 Errors** | Assets were not consolidated, or Nginx pathing is misaligned. | Run `python manage.py collectstatic`. Check `/static/` alias root in `/etc/nginx/sites-available/`. |
| **Permission Denied (SQLite / Uploads)** | Web worker user (`www-data`) lacks write permissions. | Run `sudo chown -R ubuntu:www-data /home/ubuntu/django_project` and `sudo chmod 775 db.sqlite3`. |
| **DisallowedHost Error** | Domain or server IP is missing from settings configuration. | Add domain to `ALLOWED_HOSTS = ['yourdomain.com', 'SERVER_IP']` inside `settings.py`. |
| **Gunicorn.sock Failure / Connection Refused** | Socket path mismatch, permissions issue, or Gunicorn startup crash. | Verify paths inside `/etc/systemd/system/gunicorn.service` using `which gunicorn`. |

---
*End of Corey Schafer's Django Series Complete Playlist Manual.*