from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .crud import create_item, read_item, update_item, delete_item
from database import SessionLocal
from .models import ItemCreate

router = APIRouter()

@router.post("/items/",response_model=ItemCreate)
def create_item_api(item: ItemCreate, db: Session = Depends(SessionLocal)):
    return create_item(db, item)

@router.get("/items/{item_id}", response_model=list[ItemCreate])
def read_item_api(item_id: int, db: Session = Depends(SessionLocal)):
    return read_item(db, item_id)

@router.put("/items/{item_id}")
def update_item_api(item_id: int, new_item: ItemCreate, db: Session = Depends(SessionLocal)):
    return update_item(db, item_id, new_item)

@router.delete("/items/{item_id}")
def delete_item_api(item_id: int, db: Session = Depends(SessionLocal)):
    return delete_item(db, item_id)
