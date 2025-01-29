from sqlalchemy import Column,ForeignKey,Integer,String,Float,Text,Enum
from sqlalchemy.orm import relationship
from database.db import Base,engine
from utils.constants import *


# creando el modelo de la tabla IMAGENES PRODUCTO 
# Relación de uno a muchos (un producto tiene 1 a muchas fotos, y una Foto pertenecea un solo producto)
class Product_Image(Base): 
    __tablename__= "products_image"

    id = Column(Integer,primary_key=True,index=True,autoincrement="auto")
    name = Column(String(45),nullable=False) # nombre de la imagen del producto
    imagen = Column(String(45),nullable=False) # imagen con extensión .jpg .png
    product_id= Column(Integer, ForeignKey("products.id") ,nullable=False) # Llave Foreana Id del producto
    products = relationship("Product", back_populates="products_image")
