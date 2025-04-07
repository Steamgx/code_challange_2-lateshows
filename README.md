# Late Shows Management System

A Flask-based web application for managing and tracking late-night shows.

## Features
- User authentication and authorization
- Show management (create, read, update, delete)
- Database integration with SQLAlchemy
- Alembic database migrations

## Technologies
- Python 3.x
- Flask
- SQLAlchemy
- Alembic (for database migrations)

## Setup

1. Clone the repository:
```bash
git clone https://github.com/Steamgx/code_challange_2-lateshows.git
cd code_challange_2-lateshows
```

2. Install dependencies:
```bash
pipenv install
pipenv shell
```

3. Configure the application:
- Create a `.env` file with your configuration (copy from `.env.example` if available)
- Set your database URI and secret key

4. Initialize the database:
```bash
flask db upgrade
flask seed run
```

5. Run the application:
```bash
flask run
```

## Project Structure
```
.
├── app.py                # Main application entry point
├── extensions.py         # Flask extensions initialization
├── models.py             # Database models
├── seed.py               # Database seeding script
├── Pipfile               # Python dependencies
├── Pipfile.lock
├── migrations/           # Database migration files
└── instance/             # Instance folder with database
```

## License
MIT
