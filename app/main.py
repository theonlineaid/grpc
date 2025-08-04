from fastapi import FastAPI, Depends, Body
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.crud import get_user_by_id, create_user

app = FastAPI()  # <-- Create FastAPI app instance

@app.post("/user")
async def create_user_endpoint(
    db: AsyncSession = Depends(get_db),
    name: str = Body(...),
    email: str = Body(...)
):
    user = await create_user(db, name=name, email=email)
    return user


@app.get("/user/{user_id}")
async def get_and_store_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await get_user_by_id(db, user_id)
    if user:
        return user
