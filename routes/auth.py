from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.user import UserCreate, UserOut

router = APIRouter()

@router.post("/signup", response_model=UserOut)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    # placeholder: create user
    return user

@router.post("/login")
def login(email: str, db: Session = Depends(get_db)):
    # placeholder: OTP send & verification
    return {"message": f"OTP sent to {email}"}