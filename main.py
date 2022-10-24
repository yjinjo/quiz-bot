from typing import List

from fastapi import FastAPI, Query, Path
from pydantic import BaseModel, parse_obj_as

app = FastAPI()

inventory = (
    {
        "id": 1,
        "user_id": 1,
        "name": "Legend Portion",
        "price": 2500.0,
        "amount": 100,
    },
    {
        "id": 2,
        "user_id": 1,
        "name": "Normal Portion",
        "price": 300.0,
        "amount": 50,
    },
)


class Item(BaseModel):
    name: str
    price: float
    amount: int = 0


@app.get("/users/{user_id}/inventory", response_model=List[Item])
def get_item(
        user_id: int = Path(..., gt=1, title='User id', description="DB's user.id"),
        name: str = Query(None, min_length=1, max_length=2, title="Item's name")
    ):
    user_items = []
    for item in inventory:
        if item['user_id'] == user_id:
            user_items.append(item)

    response = []
    for item in user_items:
        if name is None:
            response = user_items
            break
        if item['name'] == name:
            response.append(item)

    return response


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)

