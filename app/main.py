import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "todo_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)

Base.metadata.create_all(bind=engine)

app = FastAPI()

class TodoCreate(BaseModel):
    title: str

@app.get('/health')
def health():
    return {'status': 'ok'}

@app.get('/todos')
def get_todos():
    db = SessionLocal()
    todos = db.query(Todo).all()
    db.close()
    return {'todos': todos}

@app.get('/todos/{id}')
def get_todo(id: int):
    db = SessionLocal()
    todo = db.get(Todo, id)
    db.close()

    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    return {"todo": todo}

@app.post('/todos')
def create_todo(todo: TodoCreate):
    db = SessionLocal()
    new_todo = Todo(title=todo.title)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    db.close()
    return todo

@app.delete('/todos/{id}')
def delete_todo(id: int):
    db = SessionLocal()
    todo = db.get(Todo, id)

    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    db.delete(todo)
    db.commit()
    db.close()

    return {"todo": todo}