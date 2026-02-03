# WebFlow

Is a WebPortal created using Django allowing schools to manage students. 

## WebFlow runs PostgreSQL

Setup a PostgreSQL and create a databse, then configure these settings in your .env file

```.env
DB_NAME=webflow_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```

## Default pass (for admin if forgot)
leonard
test

# Run Dev
```bash
python manage.py runserver 0.0.0.0:8000
```

# Run Prod
```bash
docker compose up --build -d
```