from sqlalchemy import Table,Column,ForeignKey,Integer,String,Float,Text,Enum
from database.db import Base,engine


# tabla intermedia
# Tabla Octogono_Producto
Octagon_Product = Table ('octagon_product',Base.metadata,
    octagon_id = Column(Integer, ForeignKey("octagons.id") ,primary_key=True),
    product_id = Column(Integer, ForeignKey("products.id") ,primary_key=True)
    )
 