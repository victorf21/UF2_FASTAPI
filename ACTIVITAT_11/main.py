from fastapi import FastAPI
import info as select
from typing import List

app = FastAPI()

@app.get("/infos", response_model=List[dict])
def get_texts_joc():
    texts_joc = select.get_info()
    return texts_joc