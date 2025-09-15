from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def create_channel(name: str, owner_id: int):
    return {"name": name, "owner_id": owner_id}

@router.get("/")
def list_channels():
    return [{"id": 1, "name": "Test Channel"}]