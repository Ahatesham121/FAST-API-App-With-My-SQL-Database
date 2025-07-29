# FAST-API-App-With-My-SQL-Database
# 🚀 FastAPI + MySQL Starter App

This is a lightweight FastAPI application that connects to a MySQL database using SQLAlchemy and Databases library for asynchronous database operations. It provides a basic CRUD API for managing users.

---

## 📦 Tech Stack

- ⚡ [FastAPI](https://fastapi.tiangolo.com/) – Fast web framework for building APIs with Python
- 🐬 [MySQL](https://www.mysql.com/) – Relational database
- 🧮 [SQLAlchemy](https://www.sqlalchemy.org/) – Core database toolkit
- 🔌 [Databases](https://www.encode.io/databases/) – Async database access
- 🔒 [Pydantic](https://pydantic-docs.helpmanual.io/) – Data validation
- 🧪 [Uvicorn](https://www.uvicorn.org/) – ASGI web server
- 📁 `.env` for configuration management

---

## 📁 Project Structure

fastapi_mysql_app/
├── app/
│ ├── main.py # FastAPI entry point
│ ├── models.py # SQLAlchemy table schema
│ ├── schemas.py # Pydantic models
│ ├── database.py # DB connection setup
│ └── crud.py # Database operations
├── .env # Environment variables
├── requirements.txt # Dependencies
└── README.md

---

## ⚙️ Setup Instructions

### 1. 🧪 Clone the Repository

```bash
git clone https://github.com/Ahatesham121/FAST-API-App-With-My-SQL-Database.git
cd FAST-API-App-With-My-SQL-Database

🐍 Create Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

📦 Install Dependencies
pip install -r requirements.txt

⚙️ Configure .env
Create a .env file in the root directory:

env
Copy
Edit
MYSQL_USER=root
MYSQL_PASSWORD=yourpassword
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DB=testdb


🧱 Create the Database
Make sure the MySQL server is running, and manually create the database if it doesn't exist:

sql
Copy
Edit
CREATE DATABASE testdb;

▶️ Run the App
bash
Copy
Edit
uvicorn app.main:app --reload
The API will be available at: http://localhost:8000

📬 API Endpoints
Method	Endpoint	Description
POST	/users/	Create a new user
GET	/users/	Get all users
GET	/users/{id}	Get user by ID

Create a User
curl -X POST http://localhost:8000/users/ \
-H "Content-Type: application/json" \
-d '{"name": "Alice", "email": "alice@example.com"}'

Built with ❤️ by Ahatesham Mopagar
