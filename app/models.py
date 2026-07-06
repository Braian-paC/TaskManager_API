from pydantic import BaseModel

class Task(BaseModel): # Task Model
    id: int
    name: str
    checked: bool
