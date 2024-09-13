from typing import Union
from fastapi import FastAPI
import pickle
from datetime import datetime

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "n04"}

@app.get("/food")
def food(name: str):
    return {"food": name, "time": datetime.now()}
