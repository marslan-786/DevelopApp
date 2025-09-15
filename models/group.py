from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .base import Base

class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    members = Column(String)  # comma-separated user IDs
    created_at = Column(DateTime, default=datetime.utcnow)