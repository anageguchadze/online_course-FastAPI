# FastAPI Online Course Management System

## Description
A FastAPI-based backend for managing users, courses, lessons, and enrollments in an online course platform. It includes user authentication, database management with SQLAlchemy, and Alembic for migrations.

## Features
- Create, read, and authenticate users.
- Manage courses, lessons, and enrollments.
- RESTful API endpoints.

## Technologies Used
- **FastAPI**, **SQLAlchemy**, **Alembic**, **Pydantic**, **Uvicorn**, **SQLite**.

## Installation
1. Clone the repository and navigate to the folder:
   git clone https://github.com/anageguchadze/online_course-FastAPI.git
  
2. Set up a virtual environment:
   python -m venv venv
   source venv/bin/activate
   
3. Install dependencies:
   pip install -r requirements.txt
   
4. Apply database migrations:
   alembic upgrade head
   
5. Run the application:
   uvicorn app.main:app --reload

## API Endpoints
- **POST `/users/`**: Create a new user.
- **POST `/login/`**: Login with username and password.
- **GET `/userss/`**: Get a specific user by ID.
- **GET `/users/`**: List all users.

## Database Migrations
- Create a migration: `alembic revision --autogenerate -m "message"`
- Apply migrations: `alembic upgrade head`

## Project Structure
```
project/
|-- app/
|   |-- main.py         # FastAPI app
|   |-- models.py       # SQLAlchemy models
|   |-- schemas.py      # Pydantic models
|   |-- crud.py         # CRUD operations
|-- alembic/            # Alembic migrations
|-- README.md           # Project documentation
```

## License
This project is licensed under the MIT License.

