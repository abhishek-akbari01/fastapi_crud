# crud/item.py

from sqlalchemy.orm import Session
from models.item import Item

def create_item(db: Session, item_data):
    db_item = Item(**item_data.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def read_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Item).offset(skip).limit(limit).all()

def read_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()

def update_item(db: Session, item_id: int, item_data):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item:
        for key, value in item_data.dict().items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: int):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item
