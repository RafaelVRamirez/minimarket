from sqlalchemy import Column,ForeignKey,Integer,String,Float,Text,Enum
from sqlalchemy.orm import relationship
from database.db import Base,engine
from utils.constants import *

#creando el modelo de la tabla Proveedor (Supplier)
class Supplier(Base): 
    __tablename__= "suppliers"

    id = Column(Integer,primary_key=True,index=True,autoincrement="auto")
    name = Column(String(120), nullable=False) # nombre o razón social 
    ruc = Column(String(11), nullable=False) # 
    address = Column(String(150), nullable=False) # dirección
    email = Column(String(50), nullable=False) # correo
    phone = Column(String(12), nullable=False) # teléfono 
    state = Column(Enum(EstadoActivo), nullable=False) # estado del proveedor Ata o Baja
    sellers_suppliers = relationship("Seller_Supplier", back_populates="suppliers")


#creando el modelo de la tabla Vendedor (Seller)
class Seller_Supplier(Base): 
    __tablename__= "sellers_suppliers"

    id = Column(Integer,primary_key=True,index=True,autoincrement="auto")
    name = Column(String(50), nullable=False) # nombre o contacto del vendedor del proveedor
    phone = Column(String(12), nullable=False) # celular del vendedor
    supplier_id = Column(Integer,ForeignKey("suppliers.id")) 
    supplier = relationship("Supplier", back_populates="sellers_suppliers")
    state = Column(Enum(EstadoActivo), nullable=False) # Estado del vendedor del proveedor Alta o Baja

#creando el modelo de la tabla Categoría (Category)
class Category(Base): 
    __tablename__= "categories"

    id = Column(Integer,primary_key=True,index=True,autoincrement="auto")
    name = Column(String(50), nullable=False)
    product = relationship("Product", back_populates="categories")
    subcategory = relationship("Subcategory", back_populates="categories")

#creando el modelo de la tabla Subcategoría (Subategory)
class Subcategory(Base): 
    __tablename__= "subcategories"

    id = Column(Integer,primary_key=True,index=True,autoincrement="auto")
    name = Column(String(200), nullable=False)
    category_id = Column(Integer,ForeignKey("categories.id"))
    category = relationship("Category", back_populates="subcategories")
    product = relationship("Product", back_populates="subcategories")


#creando el modelo de la tabla PRODUCTO (Product)
class Product(Base): 
    __tablename__= "products"

    id = Column(Integer,primary_key=True,index=True,autoincrement="auto")
    product_code = Column(String(13),nullable=False) # código del producto interno
    barcode = Column(String(13),nullable=False) # código de barras
    product_name = Column(Text(150), nullable=False) # nombre del producto
    product_description = Column(Text(250), nullable=False) # descripción del producto
    categorie_id = Column(Integer,ForeignKey("categories.id"))
    category = relationship("Category", back_populates="products") 
    subcategories_id = Column(Integer,ForeignKey("subcategories.id"))
    subcategory = relationship("Subacategory", back_populates="products")
    product_type = Column(String(20),nullable=False) # arroz, azucar, atun, leche, galleta
    presentation_type = Column(String(13),nullable=False) # display, sachet, lata, botella, pquete
    weight_and_measure = Column(String(10),nullable=False) # Peso y unid de medida Ej. 50 gr, 500 ml, 1 kg
    existence = Column(Integer) # stock actual (existencias)
    minimum_stock = Column(Integer) # stock mínimo
    price_costo = Column(Float,default=0.00) # precio costo
    price_sale = Column(Float,default=0.00) # precio venta
    state = Column(Enum(EstadoProducto), nullable=False) # Estado del producto Alta, Baja, Agotado
    products_image = relationship("Poducts_Image", back_populates="products")
    octagons = relationship("Octagon", secondary="octagons_products", back_populates="products") # relacion muchos a muchos 


# creando el modelo de la tabla IMAGENES PRODUCTO 
# Relación de uno a muchos (un producto tiene 1 a muchas fotos, y una Foto pertenecea un solo producto)
class Poducts_Image(Base): 
    __tablename__= "products_image"

    id = Column(Integer,primary_key=True,index=True,autoincrement="auto")
    name = Column(String(13),nullable=False) # código del producto interno
    product_id= Column(Integer, ForeignKey("products.id") ,nullable=False) # Llave Foreana Id del producto
    product = relationship("Product", back_populates="products_image")

# creando el modelo de la tabla OCTOGONOS (alto en azucar, alto en sodio ..) 
# Relación de muchos a  muchos octogono y productos : crea tabla intermedia OCTOGO_PRODUCTO


# Tabla Octogono_Producto
class Octagon_Product(Base): 
    __tablename__= "octagons_products"

    octagon_id = Column(Integer, ForeignKey("octagons.id") ,primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id") ,primary_key=True)
    

# Tabla OCTOGONOS
class Octagon(Base): 
    __tablename__= "octagons"

    id = Column(Integer,primary_key=True,index=True,autoincrement="auto")
    name = Column(String(45),nullable=False) # nombre del octogono
    imagen = Column(String(45))
    product = relationship("Product", secondary="octagons_products", back_populates="octagons")




# Tabla OCTOGONOS
class Octagon(Base): 
    __tablename__= "octagons"

    id = Column(Integer,primary_key=True,index=True,autoincrement="auto")

























# Crear las tablas en las bases de datos
Base.metadata.create_all(bind=engine)
