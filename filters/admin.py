# admin.py
from aiogram.filters import BaseFilter
from aiogram.types import Message
from config import ADMIN_IDS

class AdminFilter(BaseFilter):
    is_admin: bool = True

    async def __call__(self, obj: Message) -> bool:
        return (obj.from_user.id in ADMIN_IDS) == self.is_admin