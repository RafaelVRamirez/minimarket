from sqlalchemy.orm import Session
from models.octagon import Octagon
from schemas.octagon import OctagonCreate
import os


# Crear una nueva imagen
def create_octagon(db: Session, octagon_data: OctagonCreate):
    db_image = Octagon(name=octagon_data.name,imagen=octagon_data.imagen)
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image

# Obtener todas las imágenes
def get_all_octagons(db: Session):
    return db.query(Octagon).all()

# Obtener una imagen por ID
def get_octagon_by_id(db: Session, id: int):
    return db.query(Octagon).filter(Octagon.id == id).first()

# Eliminar una imagen por ID
def delete_octagon_by_id(db: Session, id: int):
    # Obtener el registro de la base de datos
    db_image = get_octagon_by_id(db, id)
    if db_image:
        # Eliminar el archivo físico
        file_path = os.path.join("assets/octagons", db_image.imagen)
        if os.path.exists(file_path):
            os.remove(file_path)

        # Eliminar el registro de la base de datos
        db.delete(db_image)
        db.commit()
    return db_image