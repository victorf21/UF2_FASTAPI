from fastapi import Body, FastAPI
import read as select
import schemas 
from typing import List


app = FastAPI()


@app.get("/penjat/tematica/opcions", response_model=List[dict])
def select_theme():
    tematiques = select.select_theme()
    return schemas.tematiques_schema(tematiques)


@app.get("/penjat/tematica/{option}", response_model=List[dict])
def get_word(option: str):
    paraula = select.get_word(option)
    return [schemas.paraula_schema(paraula)]