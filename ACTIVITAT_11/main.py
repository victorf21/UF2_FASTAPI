from fastapi import FastAPI
import info as select
from typing import List
from pydantic import BaseModel

app = FastAPI()

class Lletras(BaseModel):
    lletres: str

@app.get("/infos", response_model=List[dict])
def get_texts_joc():
    texts_joc = select.get_info()
    return texts_joc

@app.get("/alfabet", response_model= Lletras)
def get_alfabet(idioma: str):
    alfabet = select.get_alfabet(idioma)
    return {"lletres": alfabet}