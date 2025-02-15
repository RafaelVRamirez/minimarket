from sqlalchemy.orm import Session
from models.product import Product
from schemas.product import ProductCreate, ProductUpdate



# funcipn para generar codigo producto PROD00000
def generate_next_product_code(db: Session) -> str:
    # Consulta el producto con el ID más alto
    last_product = db.query(Product).order_by(Product.id.desc()).first()
    
    # Si no hay productos, empezamos en 1
    if not last_product:
        next_number = 1
    else:
        # Extraer el número actual del código del producto
        last_code = last_product.product_code.replace("PROD", "")
        next_number = int(last_code) + 1

    # Formatear el nuevo código como PROD00001
    return f"PROD{next_number:05d}"

# FIN DE LA FUNCION 


# busca por ID del producto
def get_product(db: Session, id: int):
    return db.query(Product).filter(Product.id == id).first()

# busca todos los productos
def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Product).offset(skip).limit(limit).all()

# busca el producto por Código del producto (product_code) 
# o por Código de barra (barcode)
def get_product_by_code_or_barcode(db: Session, code: str = None, barcode: str = None):
    # Busca por product_code o barcode
    if code:
        return db.query(Product).filter(Product.product_code == code).first()
    elif barcode:
        return db.query(Product).filter(Product.barcode == barcode).first()
    else:
        return None  # Si no se proporciona ni code ni barcode


# crea un nuevo producto
def create_product(db: Session, product: ProductCreate):
    # Generar automáticamente el siguiente código de producto
    product_code = generate_next_product_code(db)
    db_product = Product(
        product_code=product_code,  # Código generado automáticamente
        barcode=product.barcode,
        product_name=product.product_name,
        product_description=product.product_description,
        categorie_id=product.categorie_id,
        subcategories_id=product.subcategories_id,
        product_type=product.product_type,
        presentation_type=product.presentation_type,
        weight_and_measure=product.weight_and_measure,
        existence=product.existence,
        minimum_stock=product.minimum_stock,
        price_costo=product.price_costo,
        price_sale=product.price_sale,
        state=product.state,
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# INICIO CRUD DE ACTUALIZAR
# actualiza la tabla productos
def update_product(db: Session, id: int, product: ProductUpdate):
    # Buscar el producto por su ID
    db_product = db.query(Product).filter(Product.id == id).first()

    # Si no se encuentra el producto, devolver None
    if not db_product:
        return None

    # Actualizar solo los campos que están presentes en la solicitud
    for key, value in product.model_dump(exclude_unset=True).items():
        setattr(db_product, key, value)

    # Confirmar los cambios en la base de datos
    db.commit()

    # Refrescar el objeto para obtener los valores actualizados desde la base de datos
    db.refresh(db_product)

    # Devolver el producto actualizado
    return db_product
# FN CRUD DE ACTUALIZAR

# elimna un producto por su id
def delete_product(db: Session, id: int):
    db_product = db.query(Product).filter(Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product
