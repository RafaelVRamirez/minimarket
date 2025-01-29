from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from database.db import get_db
from crud.product_image import (
    create_product_image,
    get_all_product_images,
    get_product_image_by_id,
    delete_product_image_by_id,
)
from schemas.product_image import ProductImageCreate, ProductImageResponse
import os
import shutil

router = APIRouter()

UPLOAD_DIR = "assets/product"

# Crear una nueva imagen
@router.post("/", response_model=ProductImageResponse)
def upload_product_image(
    product_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    # Guardar el archivo en el directorio de destino
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Crear la entrada en la base de datos
    name_imagen = os.path.splitext(file.filename)[0]# extraigo sólo el nombre de la imagen, sin sus extensiones (.jpg, .png)
    image_data = ProductImageCreate(product_id=product_id, name=name_imagen,imagen=file.filename)
    return create_product_image(db, image_data)

# Obtener todas las imágenes
@router.get("/", response_model=list[ProductImageResponse])
def read_product_images(db: Session = Depends(get_db)):
    return get_all_product_images(db)

# Obtener una imagen por ID
@router.get("/{image_id}", response_model=ProductImageResponse)
def read_product_image(image_id: int, db: Session = Depends(get_db)):
    db_image = get_product_image_by_id(db, image_id)
    if not db_image:
        raise HTTPException(status_code=404, detail="Image not found")
    return db_image

# Eliminar una imagen por ID
@router.delete("/{image_id}", response_model=ProductImageResponse)
def delete_product_images(image_id: int, db: Session = Depends(get_db)):
    db_image = delete_product_image_by_id(db, image_id)
    if not db_image:
        raise HTTPException(status_code=404, detail="Image not found")
    return db_image
