from fastapi import APIRouter

router = APIRouter() # Just simplifying in a variable

@router.get("/{id}") # The same thing as 'app'
def read_root(id: int): # Show the 'id' based on the 'id int' you add to the path
    return {"id": id}
