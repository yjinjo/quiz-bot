import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class User(BaseModel):
    name: str
    avatar_url: Optional[HttpUrl] = "<https://noticon-static.tammolo.com/dgggcrkxq/image/upload/v1666370853/noticon/u30ai8t1wvq2ws9iojwx.gif>"


class CreateUser(User):
    password: str


@app.post("/users", response_model=User) # 응답 모델
def create_user(user: CreateUser): # 요청 모델
    return user 


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)

