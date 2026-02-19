from database.engine import engine
from database.base import Base


async def on_startup_db():
    async with engine.begin() as conn:  
        await conn.run_sync(Base.metadata.create_all)     

async def on_shutdown_db():
    await engine.dispose()