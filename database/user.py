from typing import Optional
from sqlalchemy import func, select, insert, update
from .model import User
from .setup  import async_session  

async def select_user(user_id: int) -> Optional[User]:
    async with async_session() as session:
        select_stmt = select(User).where(User.user_id == user_id)
        result = await session.execute(select_stmt)
        return result.scalar_one_or_none()
   

async def add_user(user_id: int) -> None:
    async with async_session() as session:
        insert_stmt = insert(User).values(user_id=user_id)
        await session.execute(insert_stmt)
        await session.commit()

async def update_bonus_count(user_id: int):
    async with async_session() as session:
        try:
            stmt = (update(User).where(User.user_id == user_id).values(bonus_count=User.bonus_count + 10))
            await session.execute(stmt)
            await session.commit()
        except Exception as e:
            print(f"Error updating bonus count: {str(e)}")



async def plus_user_rating(user_id: int):
    async with async_session() as session:
        try:
            stmt = (update(User).where(User.user_id == user_id).values(rating=User.rating + 1))
            await session.execute(stmt)
            await session.commit()
        except Exception as e:
            print(f"Error updating bonus count: {str(e)}")



async def minus_user_rating(user_id: int):
    async with async_session() as session:
        try:
            stmt = (update(User).where(User.user_id == user_id).values(rating=User.rating - 1))
            await session.execute(stmt)
            await session.commit()
        except Exception as e:
            print(f"Error updating bonus count: {str(e)}")




async def get_all_count():
    async with async_session() as session:
        result = await session.execute(func.count(User.user_id))
        return result.scalar()
    

async def get_all_user_ids():
    async with async_session() as session:
        stmt = select(User.user_id)
        result = await session.execute(stmt)
        user_ids = [row[0] for row in result.fetchall()]
        return user_ids

