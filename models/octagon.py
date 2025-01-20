from sqlalchemy import Table,Column,ForeignKey,Integer,String,Float,Text,Enum
from sqlalchemy.orm import relationship
from database.db import Base,engine
from utils.constants import *
from models.ocCategoryon_product import OcCategoryon_Product

# Tabla OCTOGONOS
class OcCategoryon(Base): 
    __tablename__= "ocCategoryons"

    id = Column(Integer,primary_key=True,index=True,autoincrement="auto")
    name = Column(String(45),nullable=False) # nombre del octogono
    imagen = Column(String(45))
    product = relationship("Product", secondary=OcCategoryon_Product, back_populates="ocCategoryons")

