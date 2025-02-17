from sqlalchemy.orm import Session
from models.category import Category
from schemas.category import CategoryCreate
from sqlalchemy import func
from utils.formats import formatear_nombre_completo


# Obtenemos todas las categorías
def get_all_categories(db: Session, skip: int=0, limit : int =100):
  return db.query(Category).offset(skip).limit(limit).all()


# Obtener una categoría por el ID
def get_category_by_id(db: Session, id: int):
  return db.query(Category).filter(Category.id == int(id)).first()


# Obtener una Categoría por el nombre (name)
def get_category_by_name(db: Session, name: str):
  return db.query(Category).filter(func.upper(Category.name)==func.upper(name)).first()

# Crear un Category
def create_Category(db: Session, category: CategoryCreate):
  db_Category = Category(name= formatear_nombre_completo(category.name))
  db.add(db_Category)
  db.commit()
  db.refresh(db_Category)
  return db_Category

# Update de un Category
def update_Category(db: Session, id: int, category: CategoryCreate):
  db_Category = db.query(Category).filter(Category.id == id).first()
  db_Category.name = category.name
  db.commit()
  db.refresh(db_Category)
  return db_Category

# Eliminar un Category
def delete_Category(db: Session, id: int):
  db_Category = db.query(Category).filter(Category.id == id).first()
  db.delete(db_Category)
  db.commit()
  return db_Category