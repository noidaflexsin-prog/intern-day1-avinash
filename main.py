
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, EmailStr

app = FastAPI(title="User CRUD API")

users = {}
next_id = 1


class UserCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr


class User(UserCreate):
    id: int


@app.post("/users", response_model=User, status_code=201)
def create_user(user_data: UserCreate):
    global next_id
    user = User(id=next_id, **user_data.model_dump())
    users[next_id] = user
    next_id += 1
    return user


@app.get("/users", response_model=list[User])
def get_users():
    return list(users.values())


@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
    return {"message": "User deleted successfully"}
