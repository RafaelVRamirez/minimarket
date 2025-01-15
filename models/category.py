from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship
from database.db import Base



#creando el modelo de la tabla Categoría (Category)
class Category(Base): 
    __tablename__= "categories"

    id = Column(Integer,primary_key=True,index=True,autoincrement="auto")
    name = Column(String(50), nullable=False)
    products = relationship("Product", back_populates="categories")
    subcategories = relationship("Subcategory", back_populates="categories")
