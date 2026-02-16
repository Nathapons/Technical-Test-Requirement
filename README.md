# MyProject

This project is built using Django and Django Ninja.

## Installation

1.  **Navigate to the project directory:**
    ```bash
    cd myproject
    ```

2.  **Create a virtual environment (optional but recommended):**
    ```bash
    python3 -m venv env
    source env/bin/activate  # On macOS/Linux
    # env\Scripts\activate   # On Windows
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (optional):**
    ```bash
    python manage.py createsuperuser
    ```

## Usage

1.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```

2.  **Access the Swagger UI:**
    Open your browser and navigate to [http://127.0.0.1:8000/api/docs](http://127.0.0.1:8000/api/docs) to view the interactive API documentation.

3.  **Alternative Documentation:**
    You can also access the ReDoc documentation at [http://127.0.0.1:8000/api/redoc](http://127.0.0.1:8000/api/redoc).
