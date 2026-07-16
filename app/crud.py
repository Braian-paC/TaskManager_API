from models import Task
from database import read_data, save_data

def create_task_func(taskModel: Task): # Create a task
    data = read_data()
    data.append(taskModel.model_dump())
    save_data(data)
    print(data)
    return taskModel

def get_task_func(): # Read the database
    return read_data()

def update_task_func(id: int, taskModel: Task): # Update a task
    data = read_data()

    for index, item in enumerate(data):
        if item["id"] == id:
            data[index] = taskModel.model_dump()
            save_data(data)
            return taskModel
        
    return {"error": "Task not found"}

def delete_task_func(id: int): # Delete a task
    data = read_data()

    for task in data:
        if task["id"] == id:
            data.remove(task)
            save_data(data)
            return task
    
    return {"message": "Task not found"}
