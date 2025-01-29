# octagon_product_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud.octagon_product import get_octagon_product, create_octagon_product, delete_octagon_product
from schemas.octagon_product import OctagonProductCreate, OctagonProduct
from database.db import get_db

router = APIRouter()

@router.post("/", response_model=OctagonProduct)
def create_octagon_product_endpoint(octagon_product: OctagonProductCreate, db: Session = Depends(get_db)):
    return create_octagon_product(db, octagon_product)

@router.get("/{octagon_id}/{product_id}", response_model=OctagonProduct)
def read_octagon_product(octagon_id: int, product_id: int, db: Session = Depends(get_db)):
    db_octagon_product = get_octagon_product(db, octagon_id, product_id)
    if db_octagon_product is None:
        raise HTTPException(status_code=404, detail="OctagonProduct not found")
    return db_octagon_product

@router.delete("/{octagon_id}/{product_id}")
def delete_octagon_product_endpoint(octagon_id: int, product_id: int, db: Session = Depends(get_db)):
    if not delete_octagon_product(db, octagon_id, product_id):
        raise HTTPException(status_code=404, detail="OctagonProduct not found")
    return {"message": "OctagonProduct deleted successfully"}