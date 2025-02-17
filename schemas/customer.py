from typing import Optional, List
from pydantic import BaseModel, Field,EmailStr
from datetime import date
from utils.constants import EstadoActivo,DocumentoCliente

class CustomerBase(BaseModel):
    name : str = Field(..., max_length=120, example="First name Last Name")
    email : EmailStr = Field(...,  example="ejemplo@ejemplo.com")
    type_document : DocumentoCliente =  Field(..., example=DocumentoCliente.DNI)
    number_document : str = Field(..., max_length=12, example="############")
    phone : str = Field(..., max_length=15, example="############")
    date_of_birth : date 
    state: EstadoActivo = Field(..., example=EstadoActivo.ALTA)
