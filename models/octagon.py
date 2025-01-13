from sqlalchemy import Column,ForeignKey,Integer,String,Float,Text,Enum
from sqlalchemy.orm import relationship
from database.db import Base,engine
from utils.constants import *

 

# Tabla OCTOGONOS
class Octagon(Base): 
    __tablename__= "octagons"

    id = Column(Integer,primary_key=True,index=True,autoincrement="auto")
    name = Column(String(45),nullable=False) # nombre del octogono
    imagen = Column(String(45))
    product = relationship("Product", secondary="octagons_products", back_populates="octagons")

