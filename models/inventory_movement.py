from sqlalchemy import Column,ForeignKey,Integer,String,Float,Text,Enum
from sqlalchemy.orm import relationship
from datetime import date, datetime
from database.db import Base,engine
from utils.constants import *


#creando el modelo de la tabla Movimiento de inventario
# para llevar control de ingreso y salid de productos
class Inventory_Movement(Base): 
    __tablename__= "inventory_movements"

    id = Column(Integer,primary_key=True,index=True,autoincrement="auto")
    type_movement = Column(Enum(TipoMovimiento), nullable=True)
    quantity = Column(Integer, nullable=False) # cantidad del producto en unidades que ingresa
    movement_date = Column(datetime(), default=datetime.now) # fecha de movimiento, será la fecha del servidor
    lote_id= Column(Integer, ForeignKey("lotes.id") ,nullable=False)
    lotes= relationship("Lote", back_populates="inventory_movements")
