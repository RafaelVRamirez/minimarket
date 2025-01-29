from fastapi import FastAPI, Depends,HTTPException,APIRouter,status
from sqlalchemy.orm import Session
import crud.subcategory as subcateg_crud
import schemas.subcategory as subcateg_schemas
from database.db import get_db

router = APIRouter()

# Devuelve todas las subcategorías, 
@router.get('/subcategory', response_model=list[subcateg_schemas.SubCategory], status_code=status.HTTP_200_OK)
async def read_subcategories(skip: int=0, limit: int=100, db: Session = Depends(get_db)):
  return subcateg_crud.get_all_subcategories(db,skip=skip,limit=limit)

# Devuelve la subcategoría por su ID
@router.get("/subcategory/{id}", response_model=subcateg_schemas.SubCategory, status_code=status.HTTP_200_OK)
async def read_subcategory_by_id(id:int,db: Session = Depends(get_db)):
  subcat_id = subcateg_crud.get_subcategory_by_id(db,id)
  if not subcat_id:
    raise HTTPException(status_code=404,detail="Subcategory not found")
  
  return subcat_id

# Devuelve la subcategoría por su nombre (name)
@router.get("/subcategory/search/{name}", response_model=subcateg_schemas.SubCategory, status_code=status.HTTP_200_OK)
async def read_subcategory_by_name(name:str, db:Session = Depends(get_db)):
  subcat_name = subcateg_crud.get_subcategory_by_name(db,name=name)
  if not subcat_name:
    raise HTTPException(status_code=404,detail="Subcategory not found")
  
  return subcat_name

# crear una nueva categoría
@router.post("/subcategory",response_model=subcateg_schemas.SubCategory, status_code=status.HTTP_201_CREATED)
async def create_subcategory(subcategory:subcateg_schemas.SubCategoryCreate, db:Session = Depends(get_db)):
  subcat_new = subcateg_crud.get_subcategory_by_name(db, name=subcategory.name) # verifico si existe la subcategoría
  if subcat_new: #si existe, envia un error con mensaje que ya existe
    raise HTTPException(status_code=400, detail='Subcategory already registered')
  
  return subcateg_crud.create_Subcategory(db, subcategory)


# actualizar una nueva categoría
@router.put("/subcategory/{id}",response_model=subcateg_schemas.SubCategory, status_code=status.HTTP_200_OK)
async def update_subcategory(id: int, subcategory:subcateg_schemas.SubCategoryCreate, db:Session = Depends(get_db)):
  subcat_id = subcateg_crud.get_subcategory_by_id(db, id)
  if subcat_id is None:
    raise HTTPException(status_code=400, detail='Subcategory already registered')
  
  return subcateg_crud.update_Subcategory(db,id,subcategory)


# Eliminar una Categoría
@router.delete("/subcategory/{id}",response_model=subcateg_schemas.SubCategory, status_code=status.HTTP_200_OK)
async def delete_subcategory(id: int,  db:Session = Depends(get_db)):
  subcat_id = subcateg_crud.get_subcategory_by_id(db, id)
  if subcat_id is None:
    raise HTTPException(status_code=400, detail='Category not found')
  
  return subcateg_crud.delete_Subcategory(db,id)