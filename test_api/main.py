import json
from fastapi import FastAPI
import schemas

app = FastAPI()

fake_database =  {
    1: {'task': 'Clean car', 'done': True},
    2: {'task': 'Write blog', 'done': False},
    3: {'task': 'Start stream', 'done': False}
}


@app.get("/")
async def get_items():
    return fake_database


@app.get("/{id}") # Type validation pydantic
async def get_item(id: int):
    return fake_database[id]


@app.post("/")
async def add_item(item: schemas.Item):
    fake_database[len(fake_database) + 1] = {"task" : item.task, "done": item.done}
    

    

    
    