from fastapi import Body, FastAPI
from pydantic import BaseModel, Field, HttpUrl
import read as select
import schemas as paraula
from typing import List


app = FastAPI()


@app.get("/penjat/tematica/opcions", response_model=List[dict])
def select_theme():
    return paraula.themes_schema(select.select_theme())