from fastapi import APIRouter
from models import Task

router = APIRouter() # Just simplifying in a variable
tasks = []

@router.post("/tasks")
def create_task(taskModel: Task):
    tasks.append(taskModel)
    return taskModel

@router.get("/tasks")
def get_task():
    return tasks
