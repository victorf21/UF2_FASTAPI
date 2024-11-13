# Imports
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Modelo para validar datos que recibimos del POST
class Item(BaseModel):
    name: str
    cognom: str 
    edad: int
    altura: float  
    correo: str 
    telefono: int | None = None # Opcional

app = FastAPI()

# Ruta GET para obtener los datos de alumne
@app.get("/alumne")
async def root():
    return {"nom": "Victor",
            "cognom": "Fernandez",
            "edad": "20"
            }

# Simulación de diccionario, para simular base de datos
items = {"foo": "The Foo Wrestlers"}

# Ruta GET para leer un item a partir de un ID
@app.get("/items/{item_id}")
async def read_item(item_id: str):
    # Si el item no existe, lanza error 404
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item no encontrado, introduce un id ")
    # Si existe devuelve el valor
    return {"item": items[item_id]}

# Ruta POST para crear un nuevo item
@app.post("/items/")
async def create_item(item: Item):
    # Devuelve lo creado
    return item