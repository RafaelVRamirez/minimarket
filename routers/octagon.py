from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from database.db import get_db
from crud.octagon import create_octagon,get_all_octagons,get_octagon_by_id,delete_octagon_by_id
from schemas.octagon import OctagonCreate, OctagonResponse
import os
import shutil

router = APIRouter()

UPLOAD_DIR = "assets/octagons"

# Crear una nueva imagen
@router.post("/", response_model=OctagonResponse)
def upload_octagon_image(
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
    image_data = OctagonCreate(name=name_imagen,imagen=file.filename)
    return create_octagon(db, image_data)

# Obtener todas las imágenes
@router.get("/", response_model=list[OctagonResponse])
def read_octagons(db: Session = Depends(get_db)):
    return get_all_octagons(db)

# Obtener una imagen por ID
@router.get("/{image_id}", response_model=OctagonResponse)
def read_octagon_by_id(id: int, db: Session = Depends(get_db)):
    db_image = get_octagon_by_id(db, id)
    if not db_image:
        raise HTTPException(status_code=404, detail="Octogon not found")
    return db_image

# Eliminar una imagen por ID
@router.delete("/{image_id}", response_model=OctagonResponse)
def delete_octogon(id: int, db: Session = Depends(get_db)):
    db_image = delete_octagon_by_id(db, id)
    if not db_image:
        raise HTTPException(status_code=404, detail="Octogon not found")
    return db_image
