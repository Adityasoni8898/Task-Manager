
# Task Manager API

A Django REST Framework-based task management API with JWT authentication, role-based access control (admin/user), filtering, searching, sorting, pagination, and Docker support.

## Environment Setup

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd task-manager
```

### 2. Create and Activate Virtual Environment

Bash

```
python3 -m venv venv

# macOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install Dependencies

Bash

```
pip install -r requirements.txt
```

## Database Setup & Migrations

### Apply Migrations

Bash

```
python manage.py migrate
```

### Create Superuser

Bash

```
python manage.py createsuperuser
```

###  Start Development Server

Bash

```
python manage.py runserver
```

The API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000/)

## User Registration & Authentication

### Register a User

POST /auth/register/

JSON

```
{
  "username": "user1",
  "password": "pass123",
  "email": "user1@example.com" #optional
}
```

### Obtain JWT Tokens (Login)

POST /auth/login/

JSON

```
{
  "username": "user1",
  "password": "pass123"
}
```

**Response:**

JSON

```
{
  "access": "jwt-access-token",
  "refresh": "jwt-refresh-token"
}
```

### Refresh Token

POST /auth/refresh/

JSON

```
{
  "refresh": "<your-refresh-token>"
}
```

### Using JWT Tokens in Requests

Add the access token to the header:

text

```
Authorization: Bearer <your-access-token>
```

**Example (cURL):**

Bash

```
curl -H "Authorization: Bearer <token>" http://127.0.0.1:8000/api/tasks/
```

## Roles: Admin and User

Roles are managed using Django's built-in Group model.

### Available Roles

-   admin
-   user

### Assign Roles

#### Option 1: Via Django Admin

1.  Visit  /admin/
2.  Go to  **Users**
3.  Select a user
4.  Add them to the desired group (admin,  user, etc.)

#### Option 2: Management Command

Bash

```
python manage.py create_roles
```

## API Endpoints

### Authentication
| Method | Endpoint | Description | 
|--------|-------------------|--------------------------| 
| POST | `/auth/register/` | Register a new user | 
| POST | `/auth/login/` | Obtain JWT tokens | 
| POST | `/auth/refresh/` | Refresh access token |


### User Management (Admin only)

| Method | Endpoint       | Description       |
|--------|----------------|-------------------|
| GET    | `/api/users/`  | List all users    |

### Tasks

| Method | Endpoint              | Description                     |
|--------|-----------------------|---------------------------------|
| GET    | `/api/tasks/`         | List tasks (filtered by role)   |
| POST   | `/api/tasks/`         | Create a task                   |
| GET    | `/api/tasks/<id>/`    | Retrieve a specific task        |
| PUT    | `/api/tasks/<id>/`    | Update a task                   |
| DELETE | `/api/tasks/<id>/`    | Delete a task                   |


### Filtering, Searching & Sorting

| Feature                        | Example                                           |
|--------------------------------|---------------------------------------------------|
| Filter by status               | `GET /api/tasks/?status=completed`                |
| Filter by owner (admin only)   | `GET /api/tasks/?owner=username`                  |
| Search by title/description    | `GET /api/tasks/?search=meeting`                  |
| Sort by due date               | `GET /api/tasks/?ordering=due_date`               |
| Sort descending                | `GET /api/tasks/?ordering=-due_date`              |
| Pagination                     | Automatically applied                             |
### Task Model Extra Field

-   due_date  – used for sorting and deadline tracking

## Docker Support

### Build Image

Bash

```
docker build -t task-manager .
```

### Run with Docker Compose

Bash

```
docker-compose up
```

Services:

-   Django app available on port 8000

## Project Files

-   Dockerfile
-   docker-compose.yml
-   Full Django + DRF project
-   JWT authentication
-   Role-based permissions using Groups
-   Advanced filtering, search, sorting, and pagination

## Extra Features Implemented

-   Task list pagination
-   Filter by status
-   Filter by owner (admin only)
-   Search by title and description
-   Due-date field with sorting support
-   Docker and Docker Compose support