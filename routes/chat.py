from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter()

@router.post("/")
def send_message(sender_id: int, receiver_id: int, message: str, db: Session = Depends(get_db)):
    # placeholder: save message to DB
    return {"sender_id": sender_id, "receiver_id": receiver_id, "message": message}

@router.get("/")
def get_messages(user_id: int, db: Session = Depends(get_db)):
    # placeholder: return chat history
    return [{"sender_id": 1, "receiver_id": user_id, "message": "Hello"}]