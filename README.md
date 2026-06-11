# Todo Docker App

Simple Todo API built with FastAPI, PostgreSQL, Docker Compose and Nginx reverse proxy.

## Stack
- FastAPI
- PostgreSQL
- Docker
- Docker Compose
- SQLAlchemy
- Nginx

## How to run

Create `.env` file in the project root:

```env
DB_NAME=todo_db
DB_USER=postgres
DB_PASSWORD=your_password
```

Run the application:

``` bash
docker compose up --build
```

The application is available through Nginx:

```text
http://localhost/health
http://localhost/todos
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

Nginx receives requests on port `80` and forwards them to the FastAPI container on port `8000`.

To stop containers:

```bash
docker compose down
```

To remove containers and volume:

```bash
docker compose down -v
```

## Kubernetes

The project also contains basic Kubernetes manifests in the `k8s/` directory.

Used Kubernetes resources:

- Deployment
- Service
- ConfigMap
- Secret

Run:

```bash
kubectl apply -f k8s/
```

## What I learned

- Building Docker images
- Running containers with Docker Compose
- Connecting FastAPI and PostgreSQL containers
- Using Docker volumes
- Using environment variables
- Debugging containers with logs
- Configuring Nginx as a reverse proxy
- Routing requests from Nginx to FastAPI container