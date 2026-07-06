from fastapi import APIRouter

router = APIRouter()

@router.get("/{id}")
def read_root(id: int):
    return {"id": id}
