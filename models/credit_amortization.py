from sqlalchemy import Column,ForeignKey,Integer,Date,Float,Text,Enum
from sqlalchemy.orm import relationship
from database.db import Base
from datetime import date



#creando el modelo de la tabla Categoría (Category)
class Credit_Amortization(Base): 
    __tablename__= "credit_amortization"

    id = Column(Integer,primary_key=True,index=True,autoincrement="auto")
    date_amortization = Column(Date, default=date.today)
    amortization_amount = Column(Float, nullable=False)
    saldo = Column(Float, nullable=False)
    purchase_document_id = Column(Integer,ForeignKey("purchase_document.id"), nullable=False)
    purchase_document = relationship("Purchase_Document", back_populates="credit_amortization") 

   
