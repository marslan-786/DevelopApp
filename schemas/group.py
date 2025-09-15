from pydantic import BaseModel
from typing import Optional

class GroupBase(BaseModel):
    name: str
    members: Optional[str] = ""  # comma-separated user IDs

class GroupCreate(GroupBase):
    pass

class GroupOut(GroupBase):
    id: int

    class Config:
        orm_mode = True