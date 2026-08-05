from fastapi import APIRouter
from models import Task
from funcs import get_db

router = APIRouter()
conn = get_db()
cursor = conn.cursor()

@router.post("/tasks/") # Create a task
async def create_task(task: Task):
    cursor.execute("INSERT INTO tasks (id, name, description) VALUES (%s, %s, %s)", (task.id, task.name, task.description))
    conn.commit()
    return {"message": "Tarefa criada com sucesso", "ID:": task.id, "Nome:": task.name, "Descrição:": task.description}

@router.get("/tasks/") # Read the database
async def get_task():
    cursor.execute("SELECT id, name, description FROM tasks;")
    rows = cursor.fetchall()
    return [
        {
            "id": row[0],
            "name": row[1],
            "description": row[2]
        }
        for row in rows
    ]

@router.put("/tasks/{id}") # Update a task
def update_task(id: int, task: Task):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("UPDATE tasks SET name = %s, description = %s WHERE id = %s", (task.name, task.description, id))
    conn.commit()

@router.delete("/tasks/{id}") # Delete a task
def delete_task(id: int):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(f"DELETE FROM tasks WHERE id = {id}")
    conn.commit()
