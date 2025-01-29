from sqlalchemy.orm import Session
from models.subcategory import Subcategory
from schemas.subcategory import SubCategoryCreate
from sqlalchemy import func


# Obtenemos todas las subcategorías
def get_all_subcategories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Subcategory).offset(skip).limit(limit).all()
    #subcategories = db.query(Subcategory).offset(skip).limit(limit).all()
    #for sub in subcategories:
    #    print(f"ID: {sub.id}, Name: {sub.name}, Categories ID: {sub.category_id}")
    #return subcategories


# Obtener una subcategoría por el ID
def get_subcategory_by_id(db: Session, id: int):
  return db.query(Subcategory).filter(Subcategory.id == int(id)).first()


# Obtener una subCategoría por el nombre (name)
def get_subcategory_by_name(db: Session, name: str):
  return db.query(Subcategory).filter(func.upper(Subcategory.name)==func.upper(name)).first()

# Crear uns Subcategory
def create_Subcategory(db: Session, subcat: SubCategoryCreate):
  db_subCat = Subcategory(name=subcat.name, category_id=subcat.category_id)
  db.add(db_subCat)
  db.commit()
  db.refresh(db_subCat)
  return db_subCat

# Update de un SubCategory
def update_Subcategory(db: Session, id: int, subcat: SubCategoryCreate):
  db_subCat = db.query(Subcategory).filter(Subcategory.id == id).first()
  db_subCat.name = subcat.name
  db_subCat.category_id = subcat.category_id
  db.commit()
  db.refresh(db_subCat)
  return db_subCat

# Eliminar un SubCategory
def delete_Subcategory(db: Session, id: int):
  db_subCat = db.query(Subcategory).filter(Subcategory.id == id).first()
  db.delete(db_subCat)
  db.commit()
  return db_subCat