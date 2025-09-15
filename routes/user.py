from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter()

@router.get("/me")
def get_profile(user_id: int = 1, db: Session = Depends(get_db)):
    # placeholder: return user profile
    return {"user_id": user_id, "first_name": "Test", "last_name": "User"}