# Django Training Compass — Backend

## Description

This project represents the backend of a learning platform, **Django Training Compass**, built using **Django** and **Django REST Framework**. The backend provides APIs for managing materials, categories, user registration/authentication, and project information.

## Features

- User Registration & Authentication
- Categories and Materials Management
- Project Information Retrieval
- Dynamic Data Handling for materials and categories
- CSRF Protection for requests

## Technologies

- Python 3.8+
- Django 3.1.2
- Django REST Framework
- SQLite3 (default database)
- JSON Web Tokens (JWT) for user authentication
- CSRF (Cross-Site Request Forgery) protection

## Quick Start

### Clone the repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/MaximShamiakov/django-training-compass.git
cd django-training-compass

python3 -m venv .venv
source .venv/bin/activate   # For macOS/Linux
.venv\Scripts\activate      # For Windows

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
