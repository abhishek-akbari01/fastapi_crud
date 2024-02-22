from sqlalchemy import Column, Integer, String
from db1 import Base,engine
from pydantic import BaseModel

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    description = Column(String(50), index=True)

# Create the tables
Base.metadata.create_all(bind=engine)

# Pydantic models for request and response
class ItemCreate(BaseModel):
    name: str
    description: str

class ItemUpdate(BaseModel):
    name: str
    description: str

class ItemResponse(BaseModel):
    id: int
    name: str
    description: str