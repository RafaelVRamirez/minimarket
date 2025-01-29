from typing import Optional
from pydantic import Field, BaseModel


class SubCategoryBase(BaseModel):
    name : str = Field(...,max_length=200, unique=True)
    category_id : int = Field(...,gt=0)

class SubCategoryCreate(SubCategoryBase):
    pass 


class SubCategoryUpdate(SubCategoryBase):
   pass
   # name : str = Field(...,max_length=200, unique=True)
   # category_id : int = Field(...,gt=0)

class SubCategory(SubCategoryBase):
    id : int
    name: str
    category_id: int 
    class Config:
        from_attributes = True

