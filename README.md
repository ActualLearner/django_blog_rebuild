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
1. Clone the repository:
   ```bash
   git clone
    ```
2. Navigate to the project directory:
   ```bash
    cd django-blog-app
    ```
3. Create a virtual environment:
   ```bash
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
      ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
      ```bash
        source venv/bin/activate
        ```
5. Install the required packages:
   ```bash
    pip install -r requirements.txt
    ```
6. Apply migrations:
    ```bash
     python manage.py migrate
     ```
7. Create a superuser:
    ```bash
     python manage.py createsuperuser
    ```
8. Run the development server:
    ```bash
     python manage.py runserver
    ```
9. Open your browser and navigate to `http://localhost:8000`

## API endpoints & Usage

All API endpoints are prefixed with `/api/`.


### Authentication
- `POST /api/signup/` - Register a new user.
- `POST /api/token/` - Obtain JWT token by providing username and password.
- `POST /api/token/refresh/` - Refresh an expired access token using a valid refresh token.

### Posts Endpoints
- `GET /api/posts/` - List all posts.
- `POST /api/posts/` - Create a new post (Requires authentication).
- `GET /api/posts/{id}/` - Retrieve a specific post.
- `PUT /api/posts/{id}/` - Update a specific post (Requires authentication, author only).
- `DELETE /api/posts/{id}/` - Delete a specific post (Requires authentication, author only).

### Comments Endpoints
- `GET /api/comments/` - List all comments.
- `POST /api/comments/` - Create a new comment on a post (Requires authentication).
- `GET /api/comments/{id}/` - Retrieve a specific comment.
- `PUT /api/comments/{id}/` - Update a specific comment (Requires authentication, author only).
- `DELETE /api/comments/{id}/` - Delete a specific comment (Requires authentication, author only).

### Users Endpoints
- `GET /api/users/` - List all users.
- `GET /api/users/{id}/` - Retrieve a specific user's public profile.

