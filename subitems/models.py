from pydantic import BaseModel
from datetime import datetime

class SubItemBase(BaseModel):
    name: str
    description: str

class SubItemCreate(SubItemBase):
    item_id: int

class SubItemResponse(SubItemBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
