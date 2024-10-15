from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()

# Start - uvicorn home_work_3:app

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_users() -> dict:
    return users


@app.post('/users/{username}/{age}')
async def add_users(username: str =
                    Path(min_length=5, max_length=20, description="Enter your name", example="Mihail")
                        , age: int =
                    Path(ge=18, le=120, description='Enter age',example=24)) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f'Имя: {username}, возраст: {age}'
    return f'User {current_index} is registered'


@app.put('/user/{user_id}/{user_name}/{age}')
async def put_users(user_id: int =
                    Path(ge=1, le=100, description='Enter User ID', example=1)
                , user_name: str =
                    Path(min_length=5, max_length=20, description='Enter username',example='UrbanUser')
                      , age: int =
                    Path(ge=18, le=120, description='Enter age',example=24)) -> str:
    users[str(user_id)] = f'Имя: {user_name}, возраст: {age}'
    return f'User {user_id} has been update'

@app.delete('/user/{user_id}')
async def del_users(user_id: int = Path(ge=1, le=100, description='Enter User ID', example=1)) -> str:
    users.pop(str(user_id))
    return f'User {user_id} has been delete'
