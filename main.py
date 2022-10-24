from typing import Optional, List  # 추가: List

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


# 추가: Item 클래스
class Item(BaseModel):
    name: str
    price: float
    amount: int = 0


class User(BaseModel):
    name: str
    password: str
    avatar_url: Optional[HttpUrl] = None
    inventory: List[Item] = []  # 추가: inventory


@app.post("/users")
def create_user(user: User):
    return user


# 추가: get_user()
@app.get("/users/me")
def get_user():
    fake_user = User(
        name="FastCampus",
        password="1234",
        inventory=[
            Item(name="전설 무기", price=1_000_000),
            Item(name="전설 방어구", price=900_000),
        ]
    )
    return fake_user

