from sqlalchemy.orm import Session
from .models import SubItemCreate

def create_subitem(db: Session, subitem: SubItemCreate):
    db.add(subitem)
    db.commit()
    db.refresh(subitem)
    return subitem

def read_subitem(db: Session, subitem_id: int):
    return db.query(SubItemCreate).filter(SubItemCreate.id == subitem_id).first()

def update_subitem(db: Session, subitem_id: int, new_subitem: SubItemCreate):
    db_subitem = db.query(SubItemCreate).filter(SubItemCreate.id == subitem_id).first()
    for key, value in new_subitem.dict().items():
        setattr(db_subitem, key, value)
    db.commit()
    db.refresh(db_subitem)
    return db_subitem

def delete_subitem(db: Session, subitem_id: int):
    subitem = db.query(SubItemCreate).filter(SubItemCreate.id == subitem_id).first()
    db.delete(subitem)
    db.commit()
    return {"message": "SubItem deleted successfully"}
