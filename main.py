import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/users/{user_id}')
def get_user(user_id: int):
    return {'user_id': user_id}

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)

