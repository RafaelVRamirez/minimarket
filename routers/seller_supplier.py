from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from database.db import get_db
from schemas.seller_supplier import SellerSupplierListResponse,SellerSupplierCreate,SellerSupplierUpdate,SellerSupplierResponse
from crud.seller_supplier import get_seller_supplier,get_sellers_supplieres,create_seller_supplier,update_seller_supplier,delete_seller_supplier

router = APIRouter()


# ruta que de listar todos los vendedores proveedores
@router.get("/", response_model=SellerSupplierListResponse)
def read_seller_suppliers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    seller_suppliers = get_sellers_supplieres(db, skip=skip, limit=limit)
    return  {"seller_supplier":seller_suppliers}

# buscar por ID de un vemdedor
@router.get("/{id}", response_model=SellerSupplierResponse)
def read_seller_supplier(id: int, db: Session = Depends(get_db)):
    seller_supplier_id = get_seller_supplier(db, id=id)
    
    if not seller_supplier_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Seller Supplier not found")
    return seller_supplier_id


# ruta de crear un proveedor
@router.post("/", response_model=SellerSupplierResponse, status_code=status.HTTP_201_CREATED)
def create_new_seller_supplier(seller_supplier: SellerSupplierCreate, db: Session = Depends(get_db)):
    return create_seller_supplier(db, seller_supplier=seller_supplier)



# ruta de actualizar un producto, todos sus atributos o algun producto
@router.patch("/{id}", response_model=SellerSupplierResponse)
def update_existing_sellersupplier(id: int, sellersupplier: SellerSupplierUpdate, db: Session = Depends(get_db)):
    updated_seller_supplier = update_seller_supplier(db, id=id, sellersupplier=sellersupplier)
    if not updated_seller_supplier:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Seller Supplier not found")
    return updated_seller_supplier


# ruta de eliminación de un producto por su ID
@router.delete("/{id}", response_model=SellerSupplierResponse)
def delete_existing_seller_supplier(id: int, db: Session = Depends(get_db)):
    deleted_sellersupplier = delete_seller_supplier(db, id=id)
    if not deleted_sellersupplier:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Seller Supplier not found")
    return deleted_sellersupplier
