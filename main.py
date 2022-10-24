from typing import List

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, title="Name")
    price: float = Field(None, ge=0)
    amount: int = Field(
        defulat = 1,
        gt = 0,
        le = 100,
        title = "Amount",
        description = "Item's amount. You can have item between 1 and 100"
    )


@app.post("/users/{user_id}/item")
def create_item(item: Item):
    return item


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)

