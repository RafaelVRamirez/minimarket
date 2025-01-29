from sqlalchemy import Table,Column,ForeignKey,Integer,Float
from database.db import Base
from utils.constants import *

# tabla intermedia Dcomento compra y Productos
# Tabla Products and Purchase_document
purchase_detailt = Table (
    'purchase_detail',
    Base.metadata,
    Column('purchase_document_id', Integer, ForeignKey("purchase_document.id",), primary_key=True, nullable=False),
    Column('product_id', Integer, ForeignKey("products.id"), primary_key=True, nullable=False),
    Column("amount", Float, nullable=False),
    Column("unit_price", Float, nullable=False),
    Column("subtotal", Float, nullable=False),

    )