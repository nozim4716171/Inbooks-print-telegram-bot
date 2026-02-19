from sqlalchemy import select, update, delete, func
from sqlalchemy.ext.asyncio import AsyncSession
from database.session import AsyncSessionLocal
from database.base import Base
from typing import TypeVar, Type, Optional, List, Any, Dict

T = TypeVar("T", bound=Base)


# ==================== CREATE ====================

async def add_one(model: Type[T], **kwargs) -> T:
    """Bitta ma'lumot qo'shish

    Misol:
        user = await add_one(User, telegram_id=123456, first_name="Ali")
    """
    async with AsyncSessionLocal() as session:
        obj = model(**kwargs)
        session.add(obj)
        await session.commit()
        await session.refresh(obj)
        return obj


# ==================== READ ====================

async def get_one(model: Type[T], **kwargs) -> Optional[T]:
    """Bitta ma'lumot olish (filter bo'yicha)

    Misol:
        user = await get_one(User, telegram_id=123456)
    """
    async with AsyncSessionLocal() as session:
        query = select(model).filter_by(**kwargs)
        result = await session.execute(query)
        return result.scalar_one_or_none()


async def get_one_by_id(model: Type[T], obj_id: int) -> Optional[T]:
    """Bitta ma'lumot olish (id bo'yicha)

    Misol:
        user = await get_one_by_id(User, 1)
    """
    async with AsyncSessionLocal() as session:
        return await session.get(model, obj_id)


async def get_all(model: Type[T], **kwargs) -> List[T]:
    """Barcha ma'lumotlarni olish (filter bilan yoki filtersiz)

    Misol:
        users = await get_all(User)
        active_users = await get_all(User, is_active=True)
    """
    async with AsyncSessionLocal() as session:
        if kwargs:
            query = select(model).filter_by(**kwargs)
        else:
            query = select(model)
        result = await session.execute(query)
        return list(result.scalars().all())


async def get_count(model: Type[T], **kwargs) -> int:
    """Ma'lumotlar sonini olish

    Misol:
        count = await get_count(User)
        active_count = await get_count(User, is_active=True)
    """
    async with AsyncSessionLocal() as session:
        query = select(func.count()).select_from(model)
        if kwargs:
            query = query.filter_by(**kwargs)
        result = await session.execute(query)
        return result.scalar()


# ==================== UPDATE ====================

async def update_one(model: Type[T], obj_id: int, **kwargs) -> Optional[T]:
    """Bitta ma'lumotni yangilash (id bo'yicha)

    Misol:
        user = await update_one(User, 1, first_name="Vali", phone_number="+998901234567")
    """
    async with AsyncSessionLocal() as session:
        obj = await session.get(model, obj_id)
        if obj:
            for key, value in kwargs.items():
                setattr(obj, key, value)
            await session.commit()
            await session.refresh(obj)
        return obj


async def update_by_filter(model: Type[T], filters: Dict[str, Any], **kwargs) -> int:
    """Ma'lumotlarni filter bo'yicha yangilash

    Misol:
        count = await update_by_filter(User, {"is_active": True}, is_blocked=False)
    """
    async with AsyncSessionLocal() as session:
        query = update(model).filter_by(**filters).values(**kwargs)
        result = await session.execute(query)
        await session.commit()
        return result.rowcount


# ==================== DELETE ====================

async def delete_one(model: Type[T], obj_id: int) -> bool:
    """Bitta ma'lumotni o'chirish (id bo'yicha)

    Misol:
        deleted = await delete_one(User, 1)
    """
    async with AsyncSessionLocal() as session:
        obj = await session.get(model, obj_id)
        if obj:
            await session.delete(obj)
            await session.commit()
            return True
        return False


async def delete_by_filter(model: Type[T], **kwargs) -> int:
    """Ma'lumotlarni filter bo'yicha o'chirish

    Misol:
        count = await delete_by_filter(CartItems, user_id=1)
    """
    async with AsyncSessionLocal() as session:
        query = delete(model).filter_by(**kwargs)
        result = await session.execute(query)
        await session.commit()
        return result.rowcount
