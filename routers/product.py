from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from database.db import get_db
from schemas.product import ProductCreate, ProductUpdate, ProductResponse, ProductListResponse
from crud.product import get_product, get_products, create_product, update_product, delete_product, get_product_by_code_or_barcode

router = APIRouter()

# ruta que de listar todos los productos
@router.get("/", response_model=ProductListResponse)
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = get_products(db, skip=skip, limit=limit)
    return {"products": products}

# buscar por ID de un producto
@router.get("/{id}", response_model=ProductResponse)
def read_product(id: int, db: Session = Depends(get_db)):
    product = get_product(db, id=id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product

# ruta de busqueda por codigo de barras o codigo del producto
@router.get("/search/", response_model=ProductResponse)
def search_product(
    product_code: str = Query(None, description="Código del producto"),
    barcode: str = Query(None, description="Código de barras del producto"),
    db: Session = Depends(get_db)
):
    product = get_product_by_code_or_barcode(db, code=product_code, barcode=barcode)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product


# ruta de crear un producto
@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_new_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product=product)



# ruta de actualizar un producto, todos sus atributos o algun producto
@router.patch("/{id}", response_model=ProductResponse)
def update_existing_product(id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    updated_product = update_product(db, id=id, product=product)
    if not updated_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return updated_product


# ruta de eliminación de un producto por su ID
@router.delete("/{id}", response_model=ProductResponse)
def delete_existing_product(id: int, db: Session = Depends(get_db)):
    deleted_product = delete_product(db, id=id)
    if not deleted_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return deleted_product
