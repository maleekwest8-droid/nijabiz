from pydantic import BaseModel
from typing import Optional

class BusinessBase(BaseModel):
    name: str
    category: str
    phone: str
    whatsapp: str
    address: str
    description: str

class BusinessCreate(BusinessBase):
    pass

class Business(BusinessBase):
    id: int

    class Config:
        from_attributes = True
        # or orm_mode = True for older pydantic
