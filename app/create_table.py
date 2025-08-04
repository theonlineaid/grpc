# create_tables.py

import asyncio
from database import engine
from models import Base  # make sure your model is correctly imported

async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(create_db())
