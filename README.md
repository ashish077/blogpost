# blogpost

A simple blog writing web application built with Django. Follow the steps below to get a local development environment running.

## Installation

1. **Clone the repository** and enter the project directory:

   ```bash
   git clone <repo-url>
   cd blogpost
   ```

2. **Create a virtual environment** (recommended) and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**. The project relies on Django 1.10.7:

   ```bash
   pip install Django==1.10.7
   ```

## Running the app

1. **Apply database migrations**:

   ```bash
   python manage.py migrate
   ```

2. **Start the development server**:

   ```bash
   python manage.py runserver
   ```

Visit `http://127.0.0.1:8000/` in your browser to see the application.
