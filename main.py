from fastapi import FastAPI
from enum import Enum
app = FastAPI()

@app.get("/") 
async def root():
    return {"message": "Hello World"}

@app.post("/creat")
async def post():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def list_items(item_id: int):
    return {"message": "list items route"}

class FoodEnum(str,Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"

@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == "vegetables":
        return {"food_name": food_name, "message": "you are vegetables"}
    elif food_name == "dairy":
        return {"food_name": food_name, "message": "you are dairy"}
    else:
        return {"food_name": food_name, "message": "you are fruits"}