from fastapi import APIRouter
from models import Task

router = APIRouter() # Just simplifying in a variable
tasks = []

@router.post("/tasks")
def create_task(taskModel: Task): # Create the model Task
    tasks.append(taskModel)
    return taskModel

@router.get("/tasks") # List the Tasks
def get_task():
    decision = int(input("[1] -> List the tasks\n[2] -> Pass\n"))
    if decision == 1:
        return tasks
    else:
        pass
