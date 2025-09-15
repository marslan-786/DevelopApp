from fastapi import APIRouter

router = APIRouter()

@router.post("/create")
def create_bot(bot_name: str, bot_username: str, created_by: int):
    return {"bot_name": bot_name, "bot_username": bot_username, "created_by": created_by}

@router.get("/")
def list_bots():
    return [{"id": 1, "bot_name": "Test Bot", "bot_username": "@testbot"}]