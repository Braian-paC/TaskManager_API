from fastapi import APIRouter
from models import Task

router = APIRouter() # Just simplifying in a variable
tasks = []

@router.post("/tasks")
def create_task(taskModel: Task): # Create the model Task
    tasks.append(taskModel)
    print(tasks)
    return taskModel

@router.get("/tasks") # List the Tasks
def get_task():
    return tasks
