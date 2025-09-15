from database import get_db
from models.chat import Chat
from sqlalchemy.orm import Session
from datetime import datetime

def send_message(db: Session, sender_id: int, receiver_id: int, message: str):
    chat = Chat(sender_id=sender_id, receiver_id=receiver_id, message=message, timestamp=datetime.utcnow())
    db.add(chat)
    db.commit()
    db.refresh(chat)
    return chat

def get_messages(db: Session, user_id: int):
    return db.query(Chat).filter((Chat.sender_id == user_id) | (Chat.receiver_id == user_id)).all()