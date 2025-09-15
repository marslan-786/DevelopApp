from database import get_db
from models.user import User
from sqlalchemy.orm import Session

def get_user(db: Session, user_id: int):
    # placeholder: return user
    return db.query(User).filter(User.id == user_id).first()

def update_profile(db: Session, user_id: int, update_data: dict):
    user = db.query(User).filter(User.id == user_id).first()
    for key, value in update_data.items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user