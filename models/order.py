from sqlalchemy import Column,Integer,String,Enum,Date,Float,ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base
from datetime import date
from models.order_detail import order_detailt
from utils.constants import *

#creando el modelo de la tabla Pedidos (Orders)
class Order(Base): 
    __tablename__= "orders"

    id = Column(Integer,primary_key=True,index=True,autoincrement="auto")
    date_order = Column(Date, default=date.today)# fecha de pedido
    payment_type = Column(Enum(CondicionPago), nullable=False)# tpo de pago, contado o credito
    customer_id = Column(Integer, ForeignKey("customers.id") ,nullable=False)
    customers = relationship("Customer", back_populates="orders")
    product = relationship("Product", secondary=order_detailt, back_populates="orders")
    customer_amortization = relationship("Custoner_Amortization", back_populates="orders")


