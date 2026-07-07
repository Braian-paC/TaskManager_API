from fastapi import APIRouter
from models import Task
from database import read_data, save_data

router = APIRouter() # Just simplifying in a variable

@router.post("/tasks", response_model=Task)
def create_task(taskModel: Task): # Create the model Task
    data = read_data()
    data.append(taskModel.model_dump())
    save_data(data)
    return taskModel

@router.get("/tasks", response_model=list[Task]) # List the Tasks
def get_task():
    return read_data()
