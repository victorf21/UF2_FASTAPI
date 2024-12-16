from fastapi import FastAPI
import funcions as select
from typing import List
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class Lletras(BaseModel):
    lletres: str

class InformacioUpdate(BaseModel):
    nombre_usuario: str
    partidas_jugadas: int
    partidas_ganadas: int
    puntos_totales: int
    mejor_partida: datetime

class TotalIntentsUpdate(BaseModel):
    id_informacio: str
    total_intents: int

# Endpoint botonera començar partida
@app.get("/infos", response_model=List[dict])
def get_texts_joc():
    texts_joc = select.get_info()
    return texts_joc

# Endpoint per mostrar abecedari
@app.get("/alfabet", response_model= Lletras)
def get_alfabet(idioma: str):
    alfabet = select.get_alfabet(idioma)
    return {"lletres": alfabet}

# Endpoint per mostrar estadistiques jugador
@app.put("/informacio/{nombre_usuario}")
def update_informacio(nombre_usuario: str, informacio: InformacioUpdate):
    result = select.update_informacio(
        nombre_usuario=nombre_usuario,
        partidas_jugadas=informacio.partidas_jugadas,
        partidas_ganadas=informacio.partidas_ganadas,
        puntos_totales=informacio.puntos_totales,
        mejor_partida=informacio.mejor_partida
    )
    return result
# Endpoint per mostrar intents
@app.put("/informacio/total_intents/{id_informacio}")
def update_total_intents(id_informacio, data: TotalIntentsUpdate):
    result = select.update_total_intents(
        id_informacio = id_informacio,
        total_intents=data.total_intents
    )
    return result