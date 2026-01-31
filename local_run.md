# Local Run Instructions

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd warsaw-weather-django
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (if needed):**

    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7.  **Access the application in your browser at** `http://localhost:8000/`

**Note:** The current version uses a placeholder API key. To get real data, obtain an API key from OpenWeatherMap and replace the placeholder in `weather/views.py`.
