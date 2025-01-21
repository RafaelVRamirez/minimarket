from fastapi import FastAPI, Depends,HTTPException,APIRouter,status
from sqlalchemy.orm import Session
import crud.categories as categ_crud
import schemas.category as categ_schemas
from database.db import get_db

router = APIRouter()

# Devuelve todas las categorías, 
@router.get('/categories', response_model=list[categ_schemas.Category], status_code=status.HTTP_200_OK)
def read_categories(skip: int=0, limit: int=100, db: Session = Depends(get_db)):
  return categ_crud.get_all_categories(db)

# Devuelve la categoría por su ID
@router.get("/categories/{id}", response_model=categ_schemas.Category, status_code=status.HTTP_200_OK)
async def read_category_by_id(id:int,db: Session = Depends(get_db)):
  category_id = categ_crud.get_category_by_id(db,id)
  if not category_id:
    raise HTTPException(status_code=404,detail="Category not found")
  
  return category_id

# Devuelve la categoría por su nombre (name)
@router.get("/categories/name/{name}", response_model=categ_schemas.Category, status_code=status.HTTP_200_OK)
async def read_category_by_name(name:str, db:Session = Depends(get_db)):
  category_name = categ_crud.get_category_by_name(db,name=name)
  if not category_name:
    raise HTTPException(status_code=404,detail="Category not found")
  
  return category_name

# crear una nueva categoría
@router.post("/categories",response_model=categ_schemas.Category, status_code=status.HTTP_201_CREATED)
async def create_category(category:categ_schemas.CategoryCreate, db:Session = Depends(get_db)):
  category_new = categ_crud.get_category_by_name(db, name=category.name) # verifico si existe la categoría
  if category_new: #si existe, envia un error con mensaje que ya existe
    raise HTTPException(status_code=400, detail='Category already registered')
  
  return categ_crud.create_Category(db, category)


# actualizar una nueva categoría
@router.put("/categories/{id}",response_model=categ_schemas.Category, status_code=status.HTTP_200_OK)
async def update_category(id: int, category:categ_schemas.CategoryCreate, db:Session = Depends(get_db)):
  category_id = categ_crud.get_category_by_id(db, id)
  if category_id is None:
    raise HTTPException(status_code=400, detail='Category already registered')
  
  return categ_crud.update_Category(db,id,category)


# Eliminar una Categoría
@router.delete("/categories/{id}",response_model=categ_schemas.Category, status_code=status.HTTP_200_OK)
async def delete_category(id: int,  db:Session = Depends(get_db)):
  category_id = categ_crud.get_category_by_id(db, id)
  if category_id is None:
    raise HTTPException(status_code=400, detail='Category not found')
  
  return categ_crud.delete_Category(db,id)