from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship
from database.db import Base,engine
from utils.constants import *
from models.octagon_product import Octagon_Product

# Tabla OCTOGONOS
class Octagon(Base): 
    __tablename__= "octagons"

    id = Column(Integer,primary_key=True,index=True,autoincrement="auto")
    name = Column(String(45),nullable=False) # nombre del octogono
    imagen = Column(String(100),nullable=False)
    products = relationship("Product", secondary=Octagon_Product, back_populates="octagons")

