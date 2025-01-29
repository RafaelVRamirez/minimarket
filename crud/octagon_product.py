# octagon_product_crud.py
from sqlalchemy import delete
from sqlalchemy.orm import Session
from models.octagon_product import Octagon_Product
from schemas.octagon_product import OctagonProductCreate

def get_octagon_product(db: Session, octagon_id: int, product_id: int):
    return db.query(Octagon_Product).filter(Octagon_Product.c.octagon_id == octagon_id, Octagon_Product.c.product_id == product_id).first()

def create_octagon_product(db: Session, octagon_product: OctagonProductCreate):
    db_octagon_product = Octagon_Product.insert().values(**octagon_product.dict())
    db.execute(db_octagon_product)
    db.commit()
    return octagon_product

def delete_octagon_product(db: Session, octagon_id: int, product_id: int):
    # Crear una sentencia DELETE para eliminar el registro
    stmt = delete(Octagon_Product).where(
        (Octagon_Product.c.octagon_id == octagon_id) &
        (Octagon_Product.c.product_id == product_id)
    )
    result = db.execute(stmt)
    db.commit()

    # Verificar si se eliminó algún registro
    if result.rowcount > 0:
        return True
    return False