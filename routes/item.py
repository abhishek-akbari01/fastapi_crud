# routes/item.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db1 import SessionLocal
from controllers.item import create_item, read_items, read_item, update_item, delete_item
from models.item import Item,ItemCreate,ItemUpdate,ItemResponse
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/items/", response_model=ItemCreate)
def create_item_route(item: ItemCreate, db: Session = Depends(get_db)):
    return create_item(db, item)

@router.get("/items/", response_model=List[ItemResponse])
def read_items_route(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return read_items(db, skip, limit)

@router.get("/items/{item_id}", response_model=ItemResponse)
def read_item_route(item_id: int, db: Session = Depends(get_db)):
    item = read_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.put("/items/{item_id}", response_model=ItemUpdate)
def update_item_route(item_id: int, item: ItemCreate, db: Session = Depends(get_db)):
    db_item = update_item(db, item_id, item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.delete("/items/{item_id}", response_model=ItemResponse)
def delete_item_route(item_id: int, db: Session = Depends(get_db)):
    db_item = delete_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
