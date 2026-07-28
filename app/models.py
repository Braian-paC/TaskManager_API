from pydantic import BaseModel, Field
from random import randint

id_list = []

def id_func():
    id_var = randint(0, 999)
    while id_var in id_list:
        id_var = randint(0, 999)
    id_list.append(id_var)
    return id_var

class Task(BaseModel): # Task Model
    id: int = Field(default_factory=id_func)
    name: str
    description: str
