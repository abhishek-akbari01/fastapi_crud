from sqlalchemy import Column, Integer, String
from db1 import Base,engine
from pydantic import BaseModel

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(50), unique=True, index=True)
    password = Column(String(10))

Base.metadata.create_all(bind=engine)

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str