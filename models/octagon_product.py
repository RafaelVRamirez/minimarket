# octogon_product.py
from sqlalchemy import Table,Column,ForeignKey,Integer
from database.db import Base

OcCategoryon_Product = Table (
    'ocCategoryon_product',# Nombre de la tabla
    Base.metadata, # Metadatos para SQLAlchemy
    Column('ocCategoryon_id', Integer, ForeignKey("ocCategoryons.id"), primary_key=True),
    Column('product_id', Integer, ForeignKey("products.id"), primary_key=True)
    )
 