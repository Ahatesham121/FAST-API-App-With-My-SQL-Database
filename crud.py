from app.models import users
from app.database import database
from app.schemas import UserIn

async def create_user(user: UserIn):
    query = users.insert().values(name=user.name, email=user.email)
    user_id = await database.execute(query)
    return {**user.dict(), "id": user_id}

async def get_users():
    query = users.select()
    return await database.fetch_all(query)

async def get_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)
