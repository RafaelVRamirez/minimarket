from sqlalchemy import Column,ForeignKey,Integer,String,Float,Text,Enum
from sqlalchemy.orm import relationship
from database.db import Base,engine
from utils.constants import *


# creando el modelo de la tabla OCTOGONOS (alto en azucar, alto en sodio ..) 
# Relación de muchos a  muchos octogono y productos : crea tabla intermedia OCTOGO_PRODUCTO

# Tabla Octogono_Producto
class Octagon_Product(Base): 
    __tablename__= "octagons_products"

    octagon_id = Column(Integer, ForeignKey("octagons.id") ,primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id") ,primary_key=True)
 