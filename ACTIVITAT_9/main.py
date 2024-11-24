from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field, HttpUrl

import db_connect.conn as conn
import schemas.user as user
import crud.read as read
from typing import List


app = FastAPI()

class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel): 
    name: str
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None
    tags: set[str] = set()
    images: list[Image] | None = None

class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]

class tablaUsers(BaseModel):
    user_id: str
    user_name: str
    user_surname: str        
    user_age: str         
    user_email: str
    user_telefon: int


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results

@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer

# Ruta para obtener todos los users
@app.get("/users", response_model=List[dict])
def read_users():
    return user.user_schema(read.read_users())
