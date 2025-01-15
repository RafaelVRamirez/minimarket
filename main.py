from fastapi import FastAPI, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import category, subcategory,seller_supplier,supplier,purchase_document,product,octagon,octagon_product,product_image,lote,inventory_movement,credit_amortization,purchase_detailt
from database.db import Base,engine


Base.metadata.create_all(bind=engine)

app = FastAPI()

