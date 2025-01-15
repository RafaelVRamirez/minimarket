from sqlalchemy import Column,ForeignKey,Integer,String,Float,Text,Enum
from sqlalchemy.orm import relationship
from database.db import Base
from datetime import datetime



#creando el modelo de la tabla Categoría (Category)
class Credit_Amortization(Base): 
    __tablename__= "credit_amortization"

    id = Column(Integer,primary_key=True,index=True,autoincrement="auto")
    date_amortization = Column(datetime(), default=datetime.now)
    amortization_amount = Column(Float, nullable=False)
    saldo = Column(Float, nullable=False)
    purchase_document_id = Column(Integer,ForeignKey("purchase_document.id"))
    purchase_document = relationship("Purchase_Document", back_populates="credit_amortization") 

   
