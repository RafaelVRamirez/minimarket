from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import category, customer_amortization, subcategory,seller_supplier,supplier,purchase_document,product,product_image,octagon,octagon_product,lote,inventory_movement,credit_amortization,purchase_detailt,customer,order,order_detail
from database.db import Base,engine
from routers import categories, subcategory,product, product_image,octagon,octagon_product


Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"Api REST en FASTAPI - Market La Paradita"}

app.include_router(categories.router,tags=["Categories"])
app.include_router(subcategory.router,tags=["Subcategory"])
app.include_router(product.router,prefix="/products",tags=["Product"])
app.include_router(product_image.router,prefix="/product_images", tags=["Product Images"] )
app.include_router(octagon.router,prefix="/octagon", tags=["Octagon"] )
app.include_router(octagon_product.router,prefix="/octagon-products", tags=["Octagon Product"] )