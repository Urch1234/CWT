# Blog API

A simple blog API with RESTful endpoints for creating, retrieving, updating and deleting blog posts. This project uses Django, Django REST Framework (DRF), and def-yasg for API documentation. It include user authrntication and API documentation with Swagger and Redoc.

## Features

- User Registration and Authentication
- Create, Retieve, Update, and Delete Blog posts
- API Documentation (Swagger and Redoc)
- Simple, clean and extensible architecture

## Prerequisites

### Before you begin, ensure you have the following installed

- python 3.8+
- Django 4.2+
- PostgreSQL or SQLite for local development
- Node.js (if frontend is included)

## Apply Migrations

- python manage.py makemigrations
- python manage.py migrate

## Create a Superuser (for Admin)

- python manage.py createsuperuser. follow the prompt

## Run the Server

  python manage.py runserver
  visit http://127.0.0.1:8000/admin to access the admin panel.

## API Documentaion

- Swagger UI: http://127.0.0.1:8000/swagger/
- Redoc: http://127.0.0.1:8000/redoc/

## Deployment Process
