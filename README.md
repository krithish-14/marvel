# Marvel Movie App - Django & MS SQL

This project has been reorganized and migrated to Django with MS SQL Server support.

## Project Structure
- `templates/`: Contains all HTML files (now transformed into Django templates).
- `style/`: Contains all CSS files.
- `img/`: Contains all image and video assets.
- `marvel_site/`: Django project configuration.
- `marvel/`: Main application logic and routing.
- `venv/`: Python virtual environment.

## Setup Instructions

1. **Prerequisites**:
   - Ensure you have the **ODBC Driver 17 for SQL Server** installed on your Windows machine.
   - Ensure MS SQL Server is running.

2. **Database Setup**:
   - Create a new database named `marvel` in your MS SQL Server.
   - The current configuration uses **Windows Authentication** (Trusted Connection). If you use a username/password, update `marvel_site/settings.py`.

3. **Running the Application**:
   - Open a terminal in this directory.
   - Activate the virtual environment:
     ```powershell
     .\venv\Scripts\activate
     ```
   - Run migrations (to create Django's internal tables in your SQL database):
     ```bash
     python manage.py migrate
     ```
   - Start the development server:
     ```bash
     python manage.py runserver
     ```
   - Open your browser at `http://127.0.0.1:8000/`

## Features
- Organized file hierarchy.
- Dynamic routing for Home, Characters, Movies/Comics, Login, and Password Reset.
- MS SQL Server backend integration.
- Static asset management using Django's staticfiles.
