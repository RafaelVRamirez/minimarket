from typing import Optional,List
from pydantic import BaseModel, Field
from utils.constants import EstadoActivo

class SellerSupplierBase(BaseModel):
    name: str = Field(..., max_length=50, example="first name last name")
    phone: str = Field(..., max_length=12, example="999999999")
    supplier_id: int 
    state: EstadoActivo = Field(..., example=EstadoActivo.ALTA)

class SellerSupplierCreate(SellerSupplierBase):
    pass 

class SellerSupplierUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=50, example="first name last name")
    phone: Optional[str] = Field(None, max_length=12, example="999999999")
    supplier_id: Optional[int] = None
    state: Optional[EstadoActivo] = None

class SellerSupplierResponse(SellerSupplierBase):
    id: int

# Esquema para listar 
class SellerSupplierListResponse(BaseModel):
    seller_supplier: List[SellerSupplierResponse]

    class Config:
        from_attributes = True