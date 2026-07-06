from fastapi import APIRouter
from models import Task

router = APIRouter() # Just simplifying in a variable

@router.get("/") # The same thing as 'app'
def read_root(id: int = 0, name: str = "Braian"): # Show the 'id' based on the 'id int' you add to the path
    return {"id": id, "name": name}

@router.post("/tasks") # Validating Task class data
def create_task(task: Task): # http://127.0.0.1:8000/docs# -> Try it out
    return task
