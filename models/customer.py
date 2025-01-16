from sqlalchemy import Column,Integer,String,Enum,Date,Float
from sqlalchemy.orm import relationship
from database.db import Base
from datetime import date
from utils.constants import *

#creando el modelo de la tabla Cliente (Customer)
class Customer(Base): 
    __tablename__= "customers"

    id = Column(Integer,primary_key=True,index=True,autoincrement="auto")
    name = Column(String(120), nullable=False) # nombre o razón social del cliente
    email = Column(String(120),nullable=False) # correo
    type_document = Column(Enum(DocumentoCliente),nullable=True)# dni,ruc,CE
    number_document = Column(String(12), nullable=True)
    phone = Column(String(15), nullable=False)
    date_of_birth = Column(Date, nullable=False) # fecha de nacimiento
    credit_amount = Column(Float, nullable=True) # mon de credito por cliente, no todos tienen credito
    address = Column(String(150),nullable=False) # dirección
    registration_date = Column(Date, default=date.today) # fecha de registro
    orders = relationship("Order", back_populates="customers")



