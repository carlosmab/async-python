from pydantic import BaseModel

class Item(BaseModel):
    task: str
    done: bool = False