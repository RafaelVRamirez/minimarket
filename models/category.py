from sqlalchemy import Column,ForeignKey,Integer,String,Float,Text,Enum
from sqlalchemy.orm import relationship
from database.db import Base,engine
from utils.constants import *


#creando el modelo de la tabla Categoría (Category)
class Category(Base): 
    __tablename__= "categories"

    id = Column(Integer,primary_key=True,index=True,autoincrement="auto")
    name = Column(String(50), nullable=False)
    product = relationship("Product", back_populates="categories")
    subcategory = relationship("Subcategory", back_populates="categories")
