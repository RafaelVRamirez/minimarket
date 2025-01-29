from pydantic import BaseModel
from typing import Optional


class ProductImageBase(BaseModel):
    product_id: int

class ProductImageCreate(ProductImageBase):
    name: str
    imagen: str

class ProductImageResponse(ProductImageBase):
    id: int
    name: str
    imagen: str

    class Config:
        from_attributes = True









#class ProductImageBase(BaseModel):
    #imagen: str
    #product_id: int

#class ProductImageCreate(ProductImageBase):
 #   pass

#class ProductImage(ProductImageBase):
 #   id: int
 #   imagen: str

  #  class Config:
  #      from_attributes = True
