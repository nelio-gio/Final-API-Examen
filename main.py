from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import HTMLResponse, PlainTextResponse, JSONResponse
from starlette.responses import Response
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional 
import json



app = FastAPI()

# Route GET/ping pour assurer que ça marche
@app.get("/ping")
def get_ping():
    return PlainTextResponse(content="pong", status_code=200)

# 1- Creation des routes:

# a) GET/health
@app.get("/health")
def get_health():
    return PlainTextResponse(content="OK", status_code=200)

# b) POST/phones

class Characteristic(BaseModel):
    ram_memory: int
    rom_memory: int

class Phone(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: Characteristic

phones_db: List[Phone] = []

@app.post("/phones", status_code=201)
def create_phone(phone: Phone):
    phones_db.append(phone)
    return phone


# c) GET/phones
@app.get("/phones")
def get_phones():
    return phones_db


# d) GET /phones/{id}
@app.get("/phones/{id}")
def get_phone(id: str):
    for phone in phones_db:
        if phone.identifier == id:
            return phone
    raise HTTPException(status_code=404, detail=f"Phone with id '{id}' not found")


# e) BONUS :
@app.put("/phones/{id}/characteristics")
def update_characteristics(id: str, characteristics: Characteristic):
    for phone in phones_db:
        if phone.identifier == id:
            phone.characteristics = characteristics
            return phone
    raise HTTPException(status_code=404, detail=f"Phone with id '{id}' not found")


