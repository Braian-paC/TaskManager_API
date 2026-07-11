from fastapi import APIRouter
from models import Task
from database import read_data, save_data

router = APIRouter() # Just simplifying in a variable

@router.post("/tasks", response_model=Task)
def create_task(taskModel: Task): # Create the model Task
    data = read_data()
    data.append(taskModel.model_dump())
    save_data(data)
    print(data)
    return taskModel

@router.get("/tasks", response_model=list[Task]) # List the Tasks
def get_task():
    return read_data()

@router.put("/tasks/{id}", response_model=Task) # Update task stats
def update_task(id: int, task: Task):
    data = read_data()

    for index, item in enumerate(data):
        if item["id"] == id:
            data[index] = task.model_dump()
            save_data(data)
            return task
        
    return {"error": "Task not found"}

@router.delete("/tasks/{id}")
def delete_task(id: int):
    data = read_data()

    for task in data:
        if task["id"] == id:
            data.remove(task)
            save_data(data)
            return task
    
    return {"message": "Task not found"}
