# Blog API

A simple blog API with RESTful endpoints for creating, retrieving, updating and deleting blog posts. This project uses Django, Django REST Framework (DRF), and def-yasg for API documentation. It include user authrntication and API documentation with Swagger and Redoc.

## Features

- User Registration and Authentication
- Create, Retieve, Update, and Delete Blog posts
- API Documentation (Swagger and Redoc)
- Simple, clean and extensible architecture

## Prerequisites

### Before you begin, ensure you have the following installed

Back-end

    - python 3.8+
    - Django 4.2+
    - PostgreSQL or SQLite for local development
All other depencies is available in the requirements.txt file

front-end

    - Node.js (if frontend is included)
    - React + Vite

## Apply Migrations

    - python manage.py makemigrations
    - python manage.py migrate

## Create a Superuser (for Admin)

    - python manage.py createsuperuser. follow the prompt

## Run the Server

  python manage.py runserver
  visit <http://127.0.0.1:8000/admin> to access the admin panel.

## API Documentaion

    - Swagger UI: <http://127.0.0.1:8000/swagger/>
    - Redoc: <http://127.0.0.1:8000/redoc/>

## Deployment Process

### Backend Deployment on Render

1. Log in to your Render account.

2. Create a new Web Service.

3. Connect your Git repository to the Render service.

4. Set the following build and start commands:

    - Build Command: pip install -r requirements.txt && python manage.py collectstatic --noinput

    - Start Command: gunicorn CWTBlogAPI.wsgi

5. Add the required environment variables, such as DATABASE_URL and any secret keys.

6. Deploy the application and wait for the build to complete.

## Frontend Integration

If using the frontend hosted on Render:

  1. Ensure the backend API is live and accessible.

  2. Update the .env file in the frontend project to point to the deployed API URL:

      VITE_API_BASE_URL=<https://your-backend-url.onrender.com/api>

  3. Follow the frontend setup and deployment instructions to integrate both services.
