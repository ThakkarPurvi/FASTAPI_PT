from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List


class SuperMarket(BaseModel):
    name: str
    expiry_date: str
    description: str
    price: float

app = FastAPI(title="SuperMarket API")

# Create, Read, Update, Delete

store_supermarket = []


@app.get('/')
async def home():
    return {"Hello": "Purvi"}


@app.post('/supermarket/')
async def create_supermarket(supermarket: SuperMarket):
    store_supermarket.append(supermarket)
    return supermarket


@app.get('/supermarket/', response_model=List[SuperMarket])
async def get_all_supermarket():
    return store_supermarket


@app.get('/supermarket/{id}')
async def get_supermarket(id: int):
    try:

        return store_supermarket[id]

    except:

        raise HTTPException(status_code=404, detail="Supermarket Not Found")


@app.put('/supermarket/{id}')
async def update_supermarket(id: int, supermarket: SuperMarket):
    try:

        store_supermarket[id] = supermarket
        return store_supermarket[id]

    except:

        raise HTTPException(status_code=404, detail="Supermarket Not Found")


@app.delete('/supermarket/{id}')
async def delete_supermarket(id: int):
    try:

        obj = store_supermarket[id]
        store_supermarket.pop(id)
        return obj

    except:

        raise HTTPException(status_code=404, detail="Supermarket Not Found")
