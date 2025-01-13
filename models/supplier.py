from sqlalchemy import Column,ForeignKey,Integer,String,Float,Text,Enum
from sqlalchemy.orm import relationship
from database.db import Base,engine
from utils.constants import *


#creando el modelo de la tabla Proveedor (Supplier)
class Supplier(Base): 
    __tablename__= "suppliers"

    id = Column(Integer,primary_key=True,index=True,autoincrement="auto")
    name = Column(String(120), nullable=False) # nombre o razón social 
    ruc = Column(String(11), nullable=False) # 
    address = Column(String(150), nullable=False) # dirección
    email = Column(String(50), nullable=False) # correo
    phone = Column(String(12), nullable=False) # teléfono 
    state = Column(Enum(EstadoActivo), nullable=False) # estado del proveedor Ata o Baja
    sellers_suppliers = relationship("Seller_Supplier", back_populates="suppliers")
