from sqlalchemy.orm import Session
from models.product_image import Product_Image
from schemas.product_image import ProductImageCreate
import os


# Crear una nueva imagen
def create_product_image(db: Session, image_data: ProductImageCreate):
    db_image = Product_Image(product_id=image_data.product_id,name=image_data.name,
        imagen=image_data.imagen)
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image

# Obtener todas las imágenes
def get_all_product_images(db: Session):
    return db.query(Product_Image).all()

# Obtener una imagen por ID
def get_product_image_by_id(db: Session, image_id: int):
    return db.query(Product_Image).filter(Product_Image.id == image_id).first()

# Eliminar una imagen por ID
def delete_product_image_by_id(db: Session, image_id: int):
    # Obtener el registro de la base de datos
    db_image = get_product_image_by_id(db, image_id)
    if db_image:
        # Eliminar el archivo físico
        file_path = os.path.join("assets/product", db_image.imagen)
        if os.path.exists(file_path):
            os.remove(file_path)

        # Eliminar el registro de la base de datos
        db.delete(db_image)
        db.commit()
    return db_image