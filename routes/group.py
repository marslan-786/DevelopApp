from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def create_group(name: str):
    # placeholder: create group
    return {"name": name, "members": []}

@router.get("/")
def list_groups():
    # placeholder: return groups
    return [{"id": 1, "name": "Test Group"}]