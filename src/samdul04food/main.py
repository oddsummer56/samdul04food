from typing import Union
from fastapi import FastAPI
import pickle
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:8899",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def read_root():
    return {"Hello": "n04"}

@app.get("/food")
def food(name: str):
    return {"food": name, "time": datetime.now()}
