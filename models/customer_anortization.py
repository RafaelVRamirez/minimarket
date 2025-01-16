from sqlalchemy import Column,ForeignKey,Integer,Date,Float,Text,Enum
from sqlalchemy.orm import relationship
from database.db import Base
from datetime import date



#creando el modelo de la tabla Categoría (Category)
class Custoner_Amortization(Base): 
    __tablename__= "customer_amortization"

    id = Column(Integer,primary_key=True,index=True,autoincrement="auto")
    date_amortization = Column(Date, default=date.today)
    amortization_amount = Column(Float, nullable=False)
    saldo = Column(Float, nullable=False)
    order_id = Column(Integer,ForeignKey("orders.id"))
    orders = relationship("Order", back_populates="order_amortization") 

   
