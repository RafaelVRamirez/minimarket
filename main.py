from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from models import models
from database.db import Base,engine


Base.metadata.create_all(bind=engine)

app = FastAPI()

