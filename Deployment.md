# Deployment Steps

Follow these steps to successfully deploy the backend and frontend of the application on Render.
Backend Deployment

1. Prepare the Backend for Production

    Update the settings.py file to adapt to Render's deployment environment:
        Set DEBUG=False.
        Configure ALLOWED_HOSTS to include the Render domain.
        Add the production database credentials.

2. Create a Render Account

    Visit Render and create an account.
    Log in to the Render Cloud portal and navigate to the dashboard.

3. Set Up the Database

    Create a PostgreSQL database on Render.
    Copy the connection string and update the DATABASES configuration in your Django project.

4. Configure Web Services

    Create a new Web Service for the backend in Render.
    Connect your backend repository on GitHub to Render.

5. Deployment Configuration

    Ensure the following environment variables are added in Render:
        SECRET_KEY: Your Django secret key.
        Database credentials (from the PostgreSQL database setup).
        Any other required environment variables.

6. Finalize Deployment

    Verify that the web service is deployed successfully on Render.
    Check for any errors in the Render logs and troubleshoot if necessary.

7. Post-Deployment Tasks

    Run database migrations:

      python manage.py migrate

    Create a superuser:

      python manage.py createsuperuser

The 7th step can also be done, by including the post-deployment commands in build.sh file

## Additional Notes

## Troubleshooting

    - If the deployment fails, check the Render logs for detailed error messages.
    - Common issues:
        - Missing or incorrect environment variables.
        - Incorrect database configuration.
        - Backend API not accessible from the frontend.

## Verify Deployment

    - Test the entire application (backend and frontend) to ensure all features are functioning as expected.
