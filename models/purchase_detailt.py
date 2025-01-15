from sqlalchemy import Table,Column,ForeignKey,Integer,String,Float,Text,Enum
from database.db import Base
from utils.constants import *

# tabla intermedia Dcomento compra y Productos
# Tabla Products and Purchase_document
purchase_detailt = Table ('purchase_detail',Base.metadata,
    purchase_document_id = Column(Integer, ForeignKey("purchase_document.id") ,primary_key=True),
    product_id = Column(Integer, ForeignKey("products.id") ,primary_key=True),
    amount = Column(Integer, nullable=False), #cantidad
    unit_price = Column(Float, nullable=False),
    subtotal = Column(Float, nullable=False)


    )