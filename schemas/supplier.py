from typing import Optional, List
from pydantic import BaseModel, Field,EmailStr
from utils.constants import EstadoActivo

class SupplierBase(BaseModel):
    name: str = Field(..., max_length=120)
    ruc: str = Field(..., max_length=11)
    address: str = Field(..., max_length=150)
    email: EmailStr
    phone: str = Field(..., max_length=12)
    state: EstadoActivo = Field(..., example=EstadoActivo.ALTA)
   
# Schemas para creación y actualización
class SupplierCreate(SupplierBase):
    pass

class SupplierUpdate(BaseModel):
    name: Optional[str] = Field(..., max_length=120)
    ruc: Optional[str] = Field(..., max_length=11)
    address: Optional[str] = Field(..., max_length=150)
    email: Optional[EmailStr] 
    phone: Optional[str] = Field(..., max_length=12)
    state: Optional[EstadoActivo] = None

# Esquema para mostrar un producto
class SupplierResponse(SupplierBase):
    id: int 
    

# Esquema para listar productos
class SupplierListResponse(BaseModel):
    suppliers: List[SupplierResponse]

    class Config:
        from_attributes = True
