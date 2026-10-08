# 📝 Django Blog Platform

A full-featured, responsive blog platform built with Django. This application provides a complete ecosystem for content creation and user management, featuring a modern UI and automated profile handling.

## ✨ Key Features

### 👤 User Management
- **Secure Authentication**: Complete registration, login, and logout workflow.
- **Enhanced Profiles**: Dedicated user profiles with customizable details.
- **Smart Image Processing**: Automated profile picture resizing (max 300x300px) using Pillow to ensure UI consistency and optimal storage.

### ✍️ Blogging System
- **Full CRUD**: Create, read, update, and delete blog posts with ease.
- **Author Attribution**: Every post is linked to a registered user.
- **Content Discovery**: Home page feed for all posts and dedicated author pages to view posts by a specific user.

### 🎨 UI/UX
- **Modern Design**: Built with **Bootstrap 5** for a mobile-first, responsive experience.
- **Professional Forms**: Integrated `django-crispy-forms` with `crispy-bootstrap5` for clean and consistent form rendering.

## 🛠️ Tech Stack

- **Backend**: Django 6.1.1
- **Database**: SQLite (Default) / MySQL (Optional migration path)
- **Image Processing**: Pillow
- **Email Service**: Gmail SMTP
- **Frontend**: Bootstrap 5 & HTML/CSS
- **Form Styling**: Django Crispy Forms
- **Environment**: `python-dotenv` for secure configuration

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- A Gmail account (for email features)

### Installation

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd django_project
   ```

2. **Set Up Virtual Environment**
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # Unix/macOS
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   Create a `.env` file in the project root:
   ```env
   SECRET_KEY=your-django-secret-key
   EMAIL_HOST_USER=your-gmail-email@gmail.com
   EMAIL_HOST_PASSWORD=your-app-specific-password
   ```

5. **Initialize Database & Run**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## 🗺️ Project Map

### Key Endpoints
| Page | URL | Description |
| :--- | :--- | :--- |
| **Home** | `/` | Recent blog posts feed |
| **Post Detail**| `/post/<id>/` | Full view of a specific post |
| **New Post** | `/post/new/` | Create a new blog entry |
| **Profile** | `/profile/` | Manage account & profile picture |
| **Register** | `/register/` | Create a new account |
| **Login** | `/login/` | User authentication |

### Architecture
- `users/`: Manages authentication, the custom `Profile` model, and account signals.
- `blog/`: Core logic for posts, categories, and content delivery.
- `media/`: Storage for user-uploaded profile pictures.
