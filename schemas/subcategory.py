from typing import List, Optional
from pydantic import Field, BaseModel


class SubCategoryBase(BaseModel):
    name : str = Field(...,max_length=200, unique=True)
    categories_id : int = Field(...,gt=0)

class SubCategoryCreate(SubCategoryBase):
    pass 


class SubCategoryUpdate(SubCategoryBase):
    name : str = Field(...,max_length=200, unique=True)
    categories_id : int = Field(...,gt=0)

class SubCategory(SubCategoryBase):
    id : int

    class Config:
        orm_mode: True

