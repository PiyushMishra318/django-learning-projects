# Django REST API

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](requirements.txt)
[![Django](https://img.shields.io/badge/Django-5+-green.svg)](requirements.txt)

Django REST Framework API for **code snippets** with Pygments syntax highlighting, owner permissions, and **JWT authentication**.

Based on the official [Django REST framework tutorial](https://www.django-rest-framework.org/tutorial/1-serialization/).

## Features

- CRUD API for code snippets (`/snippets/`)
- Syntax-highlighted HTML via `/snippets/{id}/highlight/`
- Read-only users API (`/users/`)
- JWT auth at `/api/token/` and `/api/token/refresh/`
- Browsable API + session login at `/api-auth/`
- Simple HTML feed page at `/feed/`

## Requirements

- Python 3.11+
- pip

## Setup

```bash
git clone git@github.com:PiyushMishra318/django-learning-projects.git
cd django-learning-projects/django-rest-api
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/feed/` or the browsable API at `http://127.0.0.1:8000/snippets/`.

## JWT usage

```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username":"demo","password":"your-password"}'
```

Use the `access` token as `Authorization: Bearer <token>` on protected requests.

## Development

```bash
python manage.py test
# or
pytest
```

## Project layout

```text
djangorestapi/       # Django project settings + root URLs
newapp/              # Snippet model, serializers, viewsets
templates/feed.html  # Simple landing page
manage.py
```

## License

MIT © 2026 [Piyush Mishra](https://github.com/PiyushMishra318)
