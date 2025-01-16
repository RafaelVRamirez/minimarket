from sqlalchemy import Table,Column,ForeignKey,Integer,Float
from database.db import Base
from utils.constants import *

# tabla intermedia Dcomento Pedido y Productos
# Tabla Products and Order
order_detailt = Table (
    'order_detail',
    Base.metadata,
    Column('order_id', Integer, ForeignKey("orders.id"), primary_key=True),
    Column('product_id', Integer, ForeignKey("products.id"), primary_key=True),
    Column("amount", Float, nullable=False),
    Column("unit_price", Float, nullable=False),
    Column("subtotal", Float, nullable=False),

    )