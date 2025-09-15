from database import get_db
from models.bot import Bot
from sqlalchemy.orm import Session

def create_bot(db: Session, bot_name: str, bot_username: str, created_by: int):
    bot = Bot(bot_name=bot_name, bot_username=bot_username, created_by=created_by)
    db.add(bot)
    db.commit()
    db.refresh(bot)
    return bot

def list_bots(db: Session):
    return db.query(Bot).all()