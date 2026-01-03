from sqlalchemy import Column, Integer, String, Float, Text
from database import Base

class Business(Base):
    __tablename__ = "businesses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String, index=True)
    phone = Column(String)
    whatsapp = Column(String)
    address = Column(String)
    description = Column(String)
    region = Column(String, index=True) # North, South, East, West, etc.
    state = Column(String, index=True)
    city = Column(String, index=True)
    vacancy_status = Column(String, default="None") # "Vacancy Available" or "None"
    is_verified = Column(Integer, default=0) # 0 for no, 1 for yes
    
    # New Advanced Fields
    logo_url = Column(String, nullable=True)
    instagram = Column(String, nullable=True)
    twitter = Column(String, nullable=True)
    facebook = Column(String, nullable=True)
    opening_hours = Column(String, nullable=True) # e.g., "Mon-Fri 8am-6pm"
    google_maps_url = Column(String, nullable=True)
    is_featured = Column(Integer, default=0) # 1 for featured, 0 for normal
    clicks_count = Column(Integer, default=0)
    average_rating = Column(Float, default=0.0)
    review_count = Column(Integer, default=0)

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    business_id = Column(Integer, index=True)
    rating = Column(Integer) # 1-5
    comment = Column(String)
    user_name = Column(String)
