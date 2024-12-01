from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field, HttpUrl

from typing import List


app = FastAPI()


@app.get("/penjat/tematica/opcions", response_model=List[dict])
async def select_theme():
    return

