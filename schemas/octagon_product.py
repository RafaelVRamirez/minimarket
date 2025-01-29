# octagon_product_schema.py
from pydantic import BaseModel

class OctagonProductBase(BaseModel):
    octagon_id: int
    product_id: int

class OctagonProductCreate(OctagonProductBase):
    pass

class OctagonProduct(OctagonProductBase):
    class Config:
        from_attributes = True