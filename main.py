from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Item(BaseModel):
    id:int
    name:str
    description:str
    price:int
    on_offer:bool


@app.put('/item{item_id}')
def update_item(item_id:int,item:Item):
    return{'name':item.name}


@app.get('/')
def index():
    return{'message':'hello'}

@app.get('/greet/{name}')
def item_name(name:str):
    return{'greeting':f"hello {  name}"}
