from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import category, customer_amortization, subcategory,seller_supplier,supplier,purchase_document,product,product_image,lote,inventory_movement,credit_amortization,purchase_detailt,customer,order,order_detail
from database.db import Base,engine
from routers import categories


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(categories.router,tags=["Categories"])