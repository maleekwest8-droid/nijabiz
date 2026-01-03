from pydantic import BaseModel
from typing import Optional

class BusinessBase(BaseModel):
    name: str
    category: str
    phone: str
    whatsapp: str
    address: str
    description: str
    region: Optional[str] = "South West"
    state: Optional[str] = "Lagos"
    city: Optional[str] = "Lagos"
    vacancy_status: Optional[str] = "None"
    is_verified: Optional[int] = 0

class BusinessCreate(BusinessBase):
    pass

class Business(BusinessBase):
    id: int

    class Config:
        from_attributes = True
        # or orm_mode = True for older pydantic
