from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    cognom: str 
    edad: int
    altura: float  
    correo: str 
    telefono: int | None = None

app = FastAPI()

@app.get("/alumne")
async def root():
    return {"nom": "Victor",
            "cognom": "Fernandez",
            "edad": "20"
            }

@app.get("/items/{item_id}", status_code=404)
async def read_item(item_id):
    return {"item": item_id}

@app.post("/items/")
async def create_item(item: Item):
    return item