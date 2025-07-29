from fastapi import FastAPI, HTTPException
from app.database import database, engine, metadata
from app.schemas import UserIn, UserOut
from app import crud

metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/users/", response_model=UserOut)
async def create(user: UserIn):
    return await crud.create_user(user)

@app.get("/users/", response_model=list[UserOut])
async def read_users():
    return await crud.get_users()

@app.get("/users/{user_id}", response_model=UserOut)
async def read_user(user_id: int):
    user = await crud.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
