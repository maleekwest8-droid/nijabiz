from sqlalchemy import Column, Integer, String
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
