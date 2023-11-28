from sqlalchemy.orm import Session
from .models import ItemCreate, ItemResponse,ItemBase


def create_item(db: Session, item: ItemCreate):
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def read_item(db: Session, item_id: int):
    return db.query(ItemBase).filter(ItemBase.id == item_id).first()

def update_item(db: Session, item_id: int, new_item: ItemBase):
    db_item = db.query(ItemBase).filter(ItemBase.id == item_id).first()
    for key, value in new_item.dict().items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: int):
    item = db.query(ItemBase).filter(ItemBase.id == item_id).first()
    db.delete(item)
    db.commit()
