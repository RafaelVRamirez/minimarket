from sqlalchemy import Column,ForeignKey,Integer,String,Float,Text,Enum
from sqlalchemy.orm import relationship
from database.db import Base,engine
from utils.constants import *



#creando el modelo de la tabla Vendedor (Seller)
class Seller_Supplier(Base): 
    __tablename__= "sellers_suppliers"

    id = Column(Integer,primary_key=True,index=True,autoincrement="auto")
    name = Column(String(50), nullable=False) # nombre o contacto del vendedor del proveedor
    phone = Column(String(12), nullable=False) # celular del vendedor
    supplier_id = Column(Integer,ForeignKey("suppliers.id")) 
    suppliers = relationship("Supplier", back_populates="sellers_suppliers")
    state = Column(Enum(EstadoActivo), nullable=False) # Estado del vendedor del proveedor Alta o Baja
