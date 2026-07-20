from fastapi import APIRouter
from models import Task
from crud import create_task_func, get_task_func, update_task_func, delete_task_func

router = APIRouter()

@router.post("/tasks", response_model=Task) # Create a task
def create_task(taskModel: Task):
    return create_task_func(taskModel)

@router.get("/tasks", response_model=list[Task]) # Read the database
def get_task():
    return get_task_func()

@router.put("/tasks/{id}", response_model=Task) # Update a task
def update_task(id: int, taskModel: Task):
    return update_task_func(id, taskModel)

@router.delete("/tasks/{id}") # Delete a task
def delete_task(id: int):
    return delete_task_func(id)
