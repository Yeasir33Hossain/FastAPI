from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .crud import create_subitem, read_subitem, update_subitem, delete_subitem
from database import SessionLocal
from .models import SubItemCreate

router = APIRouter()

@router.post("/subitems/")
def create_subitem_api(subitem: SubItemCreate, db: Session = Depends(SessionLocal)):
    return create_subitem(db, subitem)

@router.get("/subitems/{subitem_id}")
def read_subitem_api(subitem_id: int, db: Session = Depends(SessionLocal)):
    return read_subitem(db, subitem_id)

@router.put("/subitems/{subitem_id}")
def update_subitem_api(subitem_id: int, new_subitem: SubItemCreate, db: Session = Depends(SessionLocal)):
    return update_subitem(db, subitem_id, new_subitem)

@router.delete("/subitems/{subitem_id}")
def delete_subitem_api(subitem_id: int, db: Session = Depends(SessionLocal)):
    return delete_subitem(db, subitem_id)
