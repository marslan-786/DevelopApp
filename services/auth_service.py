from database import get_db
from models.user import User
from sqlalchemy.orm import Session

def create_user(db: Session, user_data):
    # placeholder: save user to DB
    db_user = User(**user_data)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def send_otp(email: str):
    # placeholder: send OTP via email
    otp = "123456"  # demo
    print(f"OTP sent to {email}: {otp}")
    return otp