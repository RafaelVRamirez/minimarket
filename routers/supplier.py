from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from database.db import get_db
from schemas.supplier import SupplierCreate,SupplierUpdate, SupplierResponse, SupplierListResponse
from crud.supplier import get_supplier,get_suppliers,create_supplier,update_supplier,delete_supplier

router = APIRouter()


# ruta que de listar todos los proveedores
@router.get("/", response_model=SupplierListResponse)
def read_suppliers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    suppliers = get_suppliers(db, skip=skip, limit=limit)
    return {"suppliers": suppliers}

# buscar por ID de un proveedor
@router.get("/{supplier_id}", response_model=SupplierResponse)
def read_supplier(id: int, db: Session = Depends(get_db)):
    supplier = get_supplier(db, id=id)
    if not supplier:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Supplier not found")
    return supplier


# ruta de crear un proveedor
@router.post("/", response_model=SupplierResponse, status_code=status.HTTP_201_CREATED)
def create_new_supplier(supplier: SupplierCreate, db: Session = Depends(get_db)):
    return create_supplier(db, supplier=supplier)



# ruta de actualizar un producto, todos sus atributos o algun producto
@router.patch("/{supplier_id}", response_model=SupplierResponse)
def update_existing_supplier(supplier_id: int, supplier: SupplierUpdate, db: Session = Depends(get_db)):
    updated_supplier = update_supplier(db, supplier_id=supplier_id, supplier=supplier)
    if not updated_supplier:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Supplier not found")
    return updated_supplier


# ruta de eliminación de un producto por su ID
@router.delete("/{supplier_id}", response_model=SupplierResponse)
def delete_existing_supplier(supplier_id: int, db: Session = Depends(get_db)):
    deleted_supplier = delete_supplier(db, supplier_id=supplier_id)
    if not deleted_supplier:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Supplier not found")
    return deleted_supplier
