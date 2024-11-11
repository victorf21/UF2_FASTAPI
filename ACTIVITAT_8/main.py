from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    cognom: str | None = None
    edad: int
    altura: float | None = None

app = FastAPI()

@app.get("/alumne")
async def root():
    return {"nom": "Victor",
            "cognom": "Fernandez",
            "edad": "20"
            }
