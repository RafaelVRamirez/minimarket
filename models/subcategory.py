from sqlalchemy import Column,ForeignKey,Integer,String,Float,Text,Enum
from sqlalchemy.orm import relationship
from database.db import Base,engine
from utils.constants import *


#creando el modelo de la tabla Subcategoría (Subategory)
class Subcategory(Base): 
    __tablename__= "subcategories"

    id = Column(Integer,primary_key=True,index=True,autoincrement="auto")
    name = Column(String(200), nullable=False)
    category_id = Column(Integer,ForeignKey("categories.id"))
    categories = relationship("Category", back_populates="subcategories")
    products = relationship("Product", back_populates="subcategories")
