# Django

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](requirements.txt)
[![Django](https://img.shields.io/badge/Django-5+-green.svg)](requirements.txt)

A consolidated **Django 5** learning project combining two earlier experiments:

- **Geek Blog** — authenticated feed with posts and comments
- **Profile search** — look up user profiles by username

Previously split across two separate Django 2 experiments; now one modern codebase.

## Features

- User registration and session login
- Create posts and comment on posts
- Auto-created `UserProfile` with optional avatar upload
- Profile search by username
- Django admin for posts, comments, and profiles

## Requirements

- Python 3.11+
- pip

## Setup

```bash
git clone git@github.com:PiyushMishra318/django-learning-projects.git
cd django-learning-projects/django-blog
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/home/` after logging in.

## Routes

| Path | Description |
|------|-------------|
| `/home/` | Post feed |
| `/search/` | Profile search |
| `/register/` | Create account |
| `/login/` | Log in |
| `/admin/` | Django admin |

## Development

```bash
python manage.py test
pytest
```

## Project layout

```text
config/           # Django project settings
accounts/         # Models, views, forms
templates/        # Bootstrap UI
static/           # CSS and assets
media/            # Uploaded profile images (gitignored)
```

## License

MIT © 2026 [Piyush Mishra](https://github.com/PiyushMishra318)
