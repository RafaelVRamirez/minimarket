# octogon_product.py
from sqlalchemy import Table,Column,ForeignKey,Integer
from database.db import Base

Octagon_Product = Table (
    'octagon_product',# Nombre de la tabla
    Base.metadata, # Metadatos para SQLAlchemy
    Column('octagon_id', Integer, ForeignKey("octagons.id"), primary_key=True,nullable=False),
    Column('product_id', Integer, ForeignKey("products.id"), primary_key=True,nullable=False)
    )
 