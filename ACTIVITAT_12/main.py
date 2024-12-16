from fastapi import FastAPI
from CRUD import crud
from typing import List, Dict
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class Informacio(BaseModel):
    total_intents: int = 10
    textos_joc: str = None
    partidas_jugadas: int = 0
    partidas_ganadas: int = 0
    puntos_totales: int = 0
    nombre_usuario: str = None
    mejor_partida: datetime = None

@app.post("/infos", response_model=List[Dict])
def create_info(info: Informacio):
    nueva_info = crud.create_informacio(info)
    return [nueva_info]