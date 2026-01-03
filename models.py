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
