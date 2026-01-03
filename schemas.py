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
    
    # Advanced Fields
    logo_url: Optional[str] = None
    instagram: Optional[str] = None
    twitter: Optional[str] = None
    facebook: Optional[str] = None
    opening_hours: Optional[str] = None
    google_maps_url: Optional[str] = None
    is_featured: Optional[int] = 0
    clicks_count: Optional[int] = 0
    average_rating: Optional[float] = 0.0
    review_count: Optional[int] = 0

class ReviewBase(BaseModel):
    business_id: int
    rating: int
    comment: str
    user_name: str

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int
    class Config:
        from_attributes = True

class BusinessCreate(BusinessBase):
    pass

class Business(BusinessBase):
    id: int

    class Config:
        from_attributes = True
        # or orm_mode = True for older pydantic
