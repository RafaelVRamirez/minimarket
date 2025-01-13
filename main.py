from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from models import models


app = FastAPI()

