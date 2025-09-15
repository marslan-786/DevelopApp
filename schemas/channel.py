from pydantic import BaseModel

class ChannelBase(BaseModel):
    name: str
    owner_id: int

class ChannelCreate(ChannelBase):
    pass

class ChannelOut(ChannelBase):
    id: int

    class Config:
        orm_mode = True