# Django Blog App
A simple blog application built with Django and Django REST Framework (DRF) that allows users to create, read, update, and delete blog posts and comments.

## Features
- User authentication (sign up, log in using JWT tokens)
- Post CRUD operations (create, read, update, delete)
- Comment CRUD operations
- Author-only permissions

## Technologies Used
- Python
- Django
- DRF  
- SQLite (default, can be changed to PostgreSQL or MySQL)

## Setup & Installation

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/ActualLearner/django_blog_rebuild.git
    ```

2.  **Navigate to the Project Directory:**
    ```bash
    cd django_blog_rebuild
    ```

3.  **Navigate to the Backend Directory:**
    *All subsequent commands should be run from within the `backend` directory.*
    ```bash
    cd backend
    ```

4.  **Create and Activate a Virtual Environment:**
    ```bash
    # Create the virtual environment
    python -m venv venv

    # Activate it
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

5.  **Install Dependencies:**
    *Ensure your virtual environment is active before running this command.*
    ```bash
    pip install -r requirements.txt
    ```

6.  **Apply Database Migrations:**
    ```bash
    python manage.py migrate
    ```

7.  **Create a Superuser (Optional):**
    *This allows you to access the Django admin panel.*
    ```bash
    python manage.py createsuperuser
    ```

8.  **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```
    The API will now be running at `http://127.0.0.1:8000/`. You can access the browsable API in your browser.

## API Endpoints & Usage

The API root is available at `/api/`. All endpoints require a JSON request body.

---

### Authentication

- **`POST /api/signup/`** - Register a new user.
  - **Body:** `{ "username": "...", "password": "...", "password2": "...", "email": "(optional)" }`

- **`POST /api/token/`** - Obtain JWT tokens.
  - **Body:** `{ "username": "...", "password": "..." }`

- **`POST /api/token/refresh/`** - Refresh the access token.
  - **Body:** `{ "refresh": "..." }`

---

### Posts

- **`GET /api/posts/`**
  - **Action:** List all posts.
- **`POST /api/posts/`**
  - **Action:** Create a new post. (Authentication required)
  - **Body:** `{ "title": "...", "content": "..." }`
- **`GET /api/posts/{id}/`**
  - **Action:** Retrieve a single post.
- **`PUT /api/posts/{id}/`**
  - **Action:** Update a post. (Author only)
  - **Body:** `{ "title": "...", "content": "..." }`
- **`DELETE /api/posts/{id}/`**
  - **Action:** Delete a post. (Author only)

---

### Comments

- **`GET /api/comments/`**
  - **Action:** List all comments.
- **`POST /api/comments/`**
  - **Action:** Create a new comment. (Authentication required)
  - **Body:** `{ "post": "<post_url>", "content": "..." }`
- **`GET /api/comments/{id}/`**
  - **Action:** Retrieve a single comment.
- **`PUT /api/comments/{id}/`**
  - **Action:** Update a comment. (Author only)
  - **Body:** `{ "post": "<post_url>", "content": "..." }`
- **`DELETE /api/comments/{id}/`**
  - **Action:** Delete a comment. (Author only)

---

### Users

- **`GET /api/users/`**
  - **Action:** List all users.
- **`GET /api/users/{id}/`**
  - **Action:** Retrieve a single user.
  
