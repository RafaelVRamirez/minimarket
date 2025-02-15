from sqlalchemy.orm import Session
from models.supplier import Supplier
from schemas.supplier import SupplierCreate,SupplierUpdate


# busca por ID del proveedor
def get_supplier(db: Session, id: int):
    return db.query(Supplier).filter(Supplier.id == id).first()

# busca todos los proveedores
def get_suppliers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Supplier).offset(skip).limit(limit).all()


# crea un nuevo provedor
def create_supplier(db: Session, supplier: SupplierCreate):
    db_supplier = Supplier(
        name = supplier.name, 
        ruc = supplier.ruc,
        address = supplier.address,
        email= supplier.email,
        phone = supplier.phone,
        state=supplier.state,
    )
    db.add(db_supplier)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier

# INICIO CRUD DE ACTUALIZAR
# actualiza la tabla proveedores
def update_supplier(db: Session, supplier_id: int, supplier: SupplierUpdate):
    # Buscar el proveeedor por su ID
    db_supplier = db.query(Supplier).filter(Supplier.id == supplier_id).first()

    # Si no se encuentra el producto, devolver None
    if not db_supplier :
        return None

    # Actualizar solo los campos que están presentes en la solicitud
    for key, value in supplier.model_dump(exclude_unset=True).items():
        setattr(db_supplier , key, value)

    # Confirmar los cambios en la base de datos
    db.commit()

    # Refrescar el objeto para obtener los valores actualizados desde la base de datos
    db.refresh(db_supplier)

    # Devolver el producto actualizado
    return db_supplier 
# FN CRUD DE ACTUALIZAR

# elimna un producto por su id
def delete_supplier(db: Session, supplier_id: int):
    db_supplier = db.query(Supplier).filter(Supplier.id == supplier_id).first()
    if db_supplier:
        db.delete(db_supplier)
        db.commit()
    return db_supplier
