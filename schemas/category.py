from typing import List, Optional
from pydantic import Field, BaseModel


class CategoryBase(BaseModel):
    name : str = Field(...,max_length=50, unique=True)

class CategoryCreate(CategoryBase):
    pass 


class CategoryUpdate(CategoryBase):
    name : str = Field(...,max_length=50, unique=True)

class Category(CategoryBase):
    id : int

    class Config:
        from_attributes = True

