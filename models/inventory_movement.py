from sqlalchemy import Column,ForeignKey,Integer,Date,Enum
from sqlalchemy.orm import relationship
from datetime import date
from database.db import Base
from utils.constants import *


#creando el modelo de la tabla Movimiento de inventario
# para llevar control de ingreso y salid de productos
class Inventory_Movement(Base): 
    __tablename__= "inventory_movements"

    id = Column(Integer,primary_key=True,index=True,autoincrement="auto")
    type_movement = Column(Enum(TipoMovimiento), nullable=True)
    quantity = Column(Integer, nullable=False) # cantidad del producto en unidades que ingresa
    movement_date = Column(Date, default=date.today) # fecha de movimiento, será la fecha del servidor
    lote_id= Column(Integer, ForeignKey("lotes.id") ,nullable=False)
    lotes= relationship("Lote", back_populates="inventory_movements")
