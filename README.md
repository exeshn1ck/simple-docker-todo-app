# Todo Docker App

Simple Todo API built with FastAPI, PostgreSQL and Docker Compose.

## Stack
- FastAPI
- PostgreSQL
- Docker
- Docker Compose
- SQLAlchemy

## How to run

Create `.env` file in the project root:

```env
DB_NAME=todo_db
DB_USER=postgres
DB_PASSWORD=your_password
```

Run the application:

``` bash
docker-compose up --build
```

## API endpoints

```text
GET     /health
GET     /todos
GET     /todos/{id}
POST    /todos
DELETE  /todos/{id}
```

## Example POST request

```json
{
    "title": "Learn Docker"
}
```

## Notes

PostgreSQL data is stored in a Docker volume, so data is preserved after container restart.

To stop containers:

```bash
docker compose down
```

To remove containers and volume:

```bash
docker compose down -v
```

## What I learned

- Building Docker images
- Running containers with Docker Compose
- Connecting FastAPI and PostgreSQL containers
- Using Docker volumes
- Using environment variables
- Debugging containers with logs