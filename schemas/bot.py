from pydantic import BaseModel

class BotBase(BaseModel):
    bot_name: str
    bot_username: str
    created_by: int

class BotCreate(BotBase):
    pass

class BotOut(BotBase):
    id: int

    class Config:
        orm_mode = True