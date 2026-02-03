# WebFlow

WebFlow is a **Django**-based web portal that helps schools manage students and related administrative tasks in one place. It uses PostgreSQL as the database and can be run either via Docker (recommended) or with Django's development server.

## Features

- Student management for schools (Django-based portal).
- PostgreSQL database backend configured via environment variables.
- Docker / Docker Compose setup for production-style runs.
- Local development mode with Django's built-in server.
- Environment-dependent debug mode (`DEBUG=True`/`False`).

## Tech Stack

- **Backend:** Django (Python)
- **Database:** PostgreSQL
- **Frontend:** HTML, JavaScript
- **Containerization:** Docker, Docker Compose

## Getting Started

You can run WebFlow in two main ways:

### Option 1: Run with Docker (recommended)

Docker handles dependency installation (including `requirements.txt`) and the runtime environment.

**Prerequisites:**
- Docker and Docker Compose installed

**Steps:**
1. Set up your `.env` file in the project root (see **Environment variables** below).
2. Build and start the containers:

   ```bash
   docker compose up --build -d
   ```

3. Open your browser and go to `http://localhost:8000/`.

4. To stop the containers:

   ```bash
   docker compose down
   ```

### Option 2: Local development (Django dev server)

Use this mode if you want to actively develop and debug the project without Docker.

**Prerequisites:**
- Python 3.x
- **PostgreSQL installed and running locally** (create the database `webflow_db`)
- `pip` and `virtualenv`

**Steps:**

1. Clone the repository:

   ```bash
   git clone https://github.com/lwijshoff/webflow.git
   cd webflow
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables (create `.env` file):

   ```env
   DB_NAME=webflow_db
   DB_USER=postgres
   DB_PASSWORD=postgres
   DB_HOST=localhost
   DB_PORT=5432
   ```

5. Apply migrations and create a superuser:

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

   **Default admin credentials** (change these for production):
   - Username: `leonard`
   - Password: `test`

6. Run the development server:

   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

   Visit `http://localhost:8000/`.

## Debug settings

Set **DEBUG** appropriately in `settings.py`:

- **Development** (local): `DEBUG = True`
- **Production/Docker**: `DEBUG = False`

**Never use `DEBUG = True` on public servers.**

## Environment variables

In `.env` file:

- `DB_NAME` – PostgreSQL database name
- `DB_USER` – PostgreSQL user
- `DB_PASSWORD` – PostgreSQL password
- `DB_HOST` – PostgreSQL host
- `DB_PORT` – PostgreSQL port (default `5432`)

## Roadmap

Potential enhancements:
- Role-based permissions
- Reworked admin interface

## Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/my-feature`
3. Commit: `git commit -m "Add my feature"`
4. Push: `git push origin feature/my-feature`
5. Open Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Created and maintained by **Leonard Wijshoff** ([@lwijshoff](https://github.com/lwijshoff)).