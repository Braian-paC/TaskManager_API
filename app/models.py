from pydantic import BaseModel
from random import randint

id_list = []

id_var = randint(0, 999)
while id_var in id_list:
    id_var = randint(0, 999)
id_list.append(id_var)

class Task(BaseModel): # Task Model
    id: int = id_var
    name: str
    description: str
