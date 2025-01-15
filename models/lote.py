from sqlalchemy import Column,ForeignKey,Integer,String,Float,Text,Enum
from sqlalchemy.orm import relationship
from datetime import date
from database.db import Base,engine
from utils.constants import *


#creando el modelo de la tabla Lote (para llevar el control de fchas de vencimiento)
class Lote(Base): 
    __tablename__= "lotes"

    id = Column(Integer,primary_key=True,index=True,autoincrement="auto")
    code_lote = Column(String(15), nullable=True)
    entry_date = Column(date()) # fecha de ingreso, será la fecha del servidor
    expiration_date = Column(date(), nullable=False) # fecha de vencimiento
    quantity = Column(Integer, nullable=False) # cantidad del producto en unidades que ingresa
    stock = Column(Integer, nullable=False) # stock actual con los ingresos que se realiza 
    product_id= Column(Integer, ForeignKey("products.id") ,nullable=False)
    products= relationship("Product", back_populates="lotes")
    inventory_movements= relationship("Inventory_Movements", back_populates="lotes")
