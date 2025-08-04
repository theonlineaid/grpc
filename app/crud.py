from sqlalchemy.future import select
from app.models import User
from app.database import AsyncSessionLocal
from sqlalchemy.ext.asyncio import AsyncSession


async def get_user_by_id(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalars().first()  # safer, returns None if no result

async def create_user(db, name, email):
    new_user = User(name=name, email=email)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user