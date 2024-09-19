from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import pandas as pd
import pymysql.cursors
import csv

app = FastAPI()

origins = [
    "http://localhost:8899",
    "https://samdul01food.web.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_path():
    file_path=__file__
    dirpath = os.path.dirname(file_path)
    
    return dirpath

@app.get("/")
def read_root():
    return {"Hello": "n01"}


@app.get("/food")
def food(name: str):
    import os

    time = datetime.now()
    FILE_PATH = '/home/ubuntu/data/n04'
    df = pd.DataFrame([[name, time]], columns=['food','time'])

    # Connect to the database
    connection = pymysql.connect(host=os.getenv("DB_IP", "localhost"),
                             user='food',
                             password='1234',
                             database='fooddb',
                             port = int(os.getenv("DB_PORT", 33306)), #포트도 getenv
                             cursorclass=pymysql.cursors.DictCursor)
    
    sql = "INSERT INTO foodhistory(`username`, `foodname`, `dt`) VALUES(%s,%s,%s)"

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, ('n04', name, datetime.now()))

        connection.commit()

    #CSV
    file_path = os.getenv("FILE_PATH", f"{os.getenv('HOME')}/tmp/foodcsv/food.csv")
    if not os.path.exists(file_path):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow({name, datetime.now()})

    return {"food": name, "time": datetime.now()}
