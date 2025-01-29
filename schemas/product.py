# schemas/product.py
from typing import Optional, List
from pydantic import BaseModel, Field

from utils.constants import EstadoProducto

# Schema base común
class ProductBase(BaseModel):
    barcode: str = Field(..., max_length=13, example="5901234123457")
    product_name: str = Field(..., max_length=150, example="Arroz Premium")
    product_description: str = Field(..., max_length=250, example="Arroz extra largo de grano entero")
    categorie_id: int = Field(..., example=1)
    subcategories_id: int = Field(..., example=1)
    product_type: str = Field(..., max_length=20, example="arroz")
    presentation_type: str = Field(..., max_length=13, example="display")
    weight_and_measure: str = Field(..., max_length=10, example="1 kg")
    existence: int = Field(..., example=100)
    minimum_stock: int = Field(..., example=10)
    price_costo: float = Field(..., example=2.50)
    profit_margin: float = Field(..., example=0.10) 
    price_sale: float = Field(..., example=3.99)
    state: EstadoProducto = Field(..., example=EstadoProducto.ALTA)

# Schemas para creación y actualización
class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    barcode: Optional[str] = Field(None, max_length=13)
    product_name: Optional[str] = Field(None, max_length=150)
    product_description: Optional[str] = Field(None, max_length=250)
    product_type: Optional[str] = Field(None, max_length=20)
    presentation_type: Optional[str] = Field(None, max_length=13)
    weight_and_measure: Optional[str] = Field(None, max_length=10)
    existence: Optional[int] = None
    minimum_stock: Optional[int] = None
    price_costo: Optional[float] = None
    profit_margin : Optional[float] = None
    price_sale: Optional[float] = None
    state: Optional[EstadoProducto] = None

# Esquema para mostrar un producto
class ProductResponse(ProductBase):
    id: int 
    product_code: str
    
# Esquema para listar productos
class ProductListResponse(BaseModel):
    products: List[ProductResponse]

    class Config:
        from_attributes = True
