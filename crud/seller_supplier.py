from sqlalchemy.orm import Session
from models.seller_supplier import Seller_Supplier
from schemas.seller_supplier import SellerSupplierCreate,SellerSupplierUpdate
from utils.formats import formatear_nombre_completo

# buscar por ID
def get_seller_supplier(db:Session, id:int):
    return db.query(Seller_Supplier).filter(Seller_Supplier.id==id).first()

# buscar todos los vendedores de proveedor
def get_sellers_supplieres(db:Session, skip: int = 0, limit: int = 100):
    return db.query(Seller_Supplier).offset(skip).limit(limit).all()

# creacion de vendedor del proveedor
def create_seller_supplier(db:Session, seller_supplier=SellerSupplierCreate):
    db_seller_supplier = Seller_Supplier(
        name = formatear_nombre_completo(seller_supplier.name),
        phone = seller_supplier.phone,
        supplier_id = seller_supplier.supplier_id,
        state = seller_supplier.state,
    )
    db.add(db_seller_supplier)
    db.commit()
    db.refresh(db_seller_supplier)
    return db_seller_supplier

# actualización de seller supplier 
def update_seller_supplier(db:Session, id:int, sellersupplier:SellerSupplierUpdate):
    # buscamos el vendedor por su ID
    db_seller_supplier = db.query(Seller_Supplier).filter(Seller_Supplier.id==id).first()
    # Si no se encuentra el producto, devolver None
    if not db_seller_supplier :
        return None
    
    # Actualizar solo los campos que están presentes en la solicitud
    for key, value in sellersupplier.model_dump(exclude_unset=True).items():
        setattr(db_seller_supplier , key, value)
    db.commit()
    db.refresh(db_seller_supplier)
    return db_seller_supplier

# elimna un producto por su id
def delete_seller_supplier(db: Session, id: int):
    db_seller_supplier = db.query(Seller_Supplier).filter(Seller_Supplier.id == id).first()
    if db_seller_supplier:
        db.delete(db_seller_supplier)
        db.commit()
    return db_seller_supplier