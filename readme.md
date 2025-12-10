
# Task Manager API Documentation

Django REST Framework based task management API with:
* **JWT authentication**
* **Role-based access control** (admin/user)
* **Filtering, searching, and sorting**
* **Pagination**
* **Docker support**

## Environment Setup

You can run this project using two methods:

1.  **Option A** — Local Setup (Virtual Environment)
2.  **Option B** — Docker Setup


## Option A: Local Setup Using Virtual Environment

### 1. Clone the Repository

```
git clone <repo-url>
cd Task-Manager
```

### 2. Create and Activate Virtual Environment

```
python3 -m venv venv
```

-   **macOS/Linux:**
    ```
    source venv/bin/activate
    ```
    
-   **Windows:**
    ```
    venv\Scripts\activate
    ```
### 3. Install Dependencies
```
pip install -r requirements.txt
```
### 4. Setup Environment Variables
An example environment file is included named ".env.example" refer and create an ".env" file

### 5. Run Migrations
```
python manage.py migrate
```
### 6. Create Superuser
```
python manage.py createsuperuser
```
### 7. Start Development Server
```
python manage.py runserver
```
The API will be available at:   **http://127.0.0.1:8000/**

## Option B: Run Using Docker

### 1. Setup Environment Variables
An example environment file is included named ".env.example" refer and create an ".env" file

### 2. Build & Run Docker Image
```
docker compose up --build
```
The Django app will be available on  **port 8000**.
## User Registration & Authentication
### Register a User
`POST api/auth/register/`
```
{
	"username": "user1",
	"password": "pass123",
	"email": "user1@example.com" #optional
}
```
### Obtain JWT Tokens (Login)
`POST api/auth/login/`
```
{
	"username": "user1",
	"password": "pass123"
}
```
**Response:**
```
{
	"access": "jwt-access-token",
	"refresh": "jwt-refresh-token"
}
```
### Refresh Token
`POST api/auth/refresh/`
  
```
{
	"refresh": "<your-refresh-token>"
}
```


### Using JWT Tokens in Requests


Add the access token to the header:
`Authorization: Bearer <your-access-token>`

**Example (cURL):**
```
curl -H "Authorization: Bearer <token>" http://127.0.0.1:8000/api/tasks/
```

Also you can use Django Admin Login for API Access (Browser Only)

If you log in through the Django Admin (/admin/), the browser saves your session cookie.
This means you can visit API endpoints like: <br>
`http://127.0.0.1:8000/api/tasks/` <br>
without receiving a 401 Unauthorized, even without sending a JWT token.
## Roles: Admin and User

Roles are managed using Django's built-in Group model.
### Available Roles
- admin
- user

### Role Setup
#### 1. Create Roles
```
python manage.py create_roles
```
#### 2. Assign roles via Django Admin
1. Visit /admin/
2. Go to **Users**
3. Select a user
4. Add them to the desired group (admin, user, etc.)
## API Endpoints


### Authentication

| Method | Endpoint | Description |
|--------|-------------------|--------------------------|
| POST | `/api/auth/register/` | Register a new user |
| POST | `/api/auth/login/` | Obtain JWT tokens |
| POST | `/api/auth/refresh/` | Refresh access token |

### User Management (Admin only)
 

| Method | Endpoint | Description |
|--------|----------------|-------------------|
| GET | `/api/users/` | List all users |
 

### Tasks
| Method | Endpoint | Description |
|--------|-----------------------|---------------------------------|
| GET | `/api/tasks/` | List tasks (Users: own tasks. Admins: all tasks) |
| POST | `/api/tasks/` | Create a task |
| GET | `/api/tasks/<id>/` | Retrieve a specific task |
| PUT | `/api/tasks/<id>/` | Update a task |
| POST | `/api/tasks/<id>/toggle/` | Toggles status between COMPLETE and INCOMPLETE |
| DELETE | `/api/tasks/<id>/` | Delete a task |


### Filtering, Searching & Sorting

| Feature | Example |
|--------------------------------|---------------------------------------------------|
| Filter by status | `GET /api/tasks/?status=completed` |
| Filter by owner (admin only) | `GET /api/tasks/?owner=username` |
| Search by title/description | `GET /api/tasks/?search=meeting` |
| Sort by due date | `GET /api/tasks/?ordering=due_date` |
| Sort descending | `GET /api/tasks/?ordering=-due_date` |
| Sort by created_at | `GET /api/tasks/?ordering=created_at` |
| Pagination | Automatically applied on `GET /api/tasks/` (page_size = 10) |

## Project Files
| File / Folder       | Description |
|---------------------|-------------|
| **Dockerfile**      | Used to build the Docker image for running the Django application in a containerized environment. |
| **docker-compose.yml** | Defines services for running the application using Docker Compose (e.g., Django app, environment variables). Simplifies starting the project with one command. |
| **.env.example**    | Template file containing example environment variables required by the project. Users can copy it to `.env` and fill in values. |
| **requirements.txt**| Contains all Python dependencies needed to run the project. Used for `pip install -r requirements.txt`. |
| **manage.py** | Django’s main command-line utility for running the server, migrations, management commands, etc. |
| **/Task_Manager**   | Main project root containing settings, URLs, and configuration for the Django backend. |
| **/users**          | Django app responsible for user registration, JWT authentication endpoints, and role/group management logic. |
| **/tasks**          | Django app containing Task model, serializers, views, filtering, sorting, pagination, and task-related API endpoints. |


## Extra Features Implemented
- Task list pagination
- Filter by status
- Filter by owner (admin only)
- Search by title and description
- Due-date field with sorting support
- Docker and Docker Compose support
