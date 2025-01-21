from sqlalchemy import Column,ForeignKey,Integer,String,Float,Text,Enum
from sqlalchemy.orm import relationship
from database.db import Base
from utils.constants import *
from models.purchase_detailt import purchase_detailt
from models.order_detail import order_detailt

#creando el modelo de la tabla PRODUCTO (Product)
class Product(Base): 
    __tablename__= "products"

    id = Column(Integer,primary_key=True,index=True,autoincrement="auto")
    product_code = Column(String(13),nullable=False) # código del producto interno
    barcode = Column(String(13),nullable=False) # código de barras
    product_name = Column(Text(150), nullable=False) # nombre del producto
    product_description = Column(Text(250), nullable=False) # descripción del producto
    categorie_id = Column(Integer,ForeignKey("categories.id"))
    categories = relationship("Category", back_populates="products") 
    subcategories_id = Column(Integer,ForeignKey("subcategories.id"))
    subcategories = relationship("Subcategory", back_populates="products")
    product_type = Column(String(20),nullable=False) # arroz, azucar, atun, leche, galleta
    presentation_type = Column(String(13),nullable=False) # display, sachet, lata, botella, pquete
    weight_and_measure = Column(String(10),nullable=False) # Peso y unid de medida Ej. 50 gr, 500 ml, 1 kg
    existence = Column(Integer) # stock actual (existencias)
    minimum_stock = Column(Integer) # stock mínimo
    price_costo = Column(Float,default=0.00) # precio costo
    price_sale = Column(Float,default=0.00) # precio venta
    state = Column(Enum(EstadoProducto), nullable=False) # Estado del producto Alta, Baja, Agotado
    products_image = relationship("Product_Image", back_populates="products")
    lotes= relationship("Lote", back_populates="products")
    purchase_document = relationship("Purchase_Document", secondary=purchase_detailt, back_populates="product") # relacion muchos a muchos 
    orders =relationship("Order", secondary=order_detailt, back_populates="product")

