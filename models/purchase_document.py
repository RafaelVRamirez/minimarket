from sqlalchemy import Column,ForeignKey,Integer,String,Float,Date,Enum
from sqlalchemy.orm import relationship
from database.db import Base
from datetime import date
from utils.constants import *
from models.purchase_detailt import purchase_detailt


class Purchase_Document(Base):
    __tablename__ = "purchase_document"

    id = Column(Integer,primary_key=True,index=True,autoincrement="auto")
    type_document = Column(Enum(TipoDocumento), nullable=False) # tipo de documento factura, boleta
    document_number = Column(String(15), nullable=False) # numero de facturra o boleta
    total = Column(Float, nullable=False)
    igv = Column(Float, nullable=False)
    perception = Column(Float, nullable=False)
    date_purchase = Column(Date, default=date.today)
    method_of_payment = Column(Enum(FormaPago), nullable=False)
    payment_condition = Column(Enum(CondicionPago), nullable=False)
    payment_status = Column(Enum(EstadoPago), nullable=False)
    supplier_id = Column(Integer,ForeignKey("suppliers.id"), nullable=False)
    suppliers = relationship("Supplier", back_populates="purchase_document")
    product = relationship("Product", secondary=purchase_detailt, back_populates="purchase_document") # relacion muchos a muchos 
    credit_amortization = relationship("Credit_Amortization", back_populates="purchase_document")

