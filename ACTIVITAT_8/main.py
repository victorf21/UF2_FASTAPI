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

items = {"foo": "The Foo Wrestlers"}
@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item no encontrado, introduce un id ")
    return {"item": items[item_id]}

@app.post("/items/")
async def create_item(item: Item):
    return item