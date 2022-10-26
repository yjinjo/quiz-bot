from datetime import datetime, timedelta
from typing import Optional

import bcrypt
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials,
    OAuth2PasswordRequestForm,
)
from pydantic import BaseModel
from jose import jwt
from jose.exceptions import ExpiredSignatureError

app = FastAPI()
security = HTTPBearer()

ALGORITHM = "HS256"
SECRET_KEY = "3223030dc326406436c81c9b2ee7ddaa192f8591f1ce362454616f511cf2a5a2"
fake_user_db = {
    "user": {
        "id": 1,
        "username": "user",
        "email": "user@gmail.com",
        "password": "$2b$12$JvkesFhrVX8Sf9iW56dwnuGWlOMqNYEksztgwzC93zb2aoxYlASdG"
    }
}


class User(BaseModel):
    id: int
    username: str
    email: str


class UserPayload(User):
    exp: datetime


async def create_access_token(data: dict, exp: Optional[timedelta] = None):
    expire = datetime.utcnow() + (exp or timedelta(minutes=30))
    user_info = UserPayload(**data, exp=expire)

    return jwt.encode(user_info.dict(), SECRET_KEY, algorithm=ALGORITHM)


async def get_user(cred: HTTPAuthorizationCredentials = Depends(security)):
    token = cred.credentials
    try:
        decoded_data = jwt.decode(token, SECRET_KEY, ALGORITHM)
    except ExpiredSignatureError:
        raise HTTPException(401, "Expired")
    user_info = User(**decoded_data)

    return fake_user_db[user_info.username]


@app.post("/login")
async def issue_token(data: OAuth2PasswordRequestForm = Depends()):
    user = fake_user_db[data.username]

    if bcrypt.checkpw(data.password.encode(), user["password"].encode()):
        return await create_access_token(user, exp=timedelta(minutes=30))
    raise HTTPException(401)


@app.get("/users/me", response_model=User)
async def get_current_user(user: dict = Depends(get_user)):
    return user

