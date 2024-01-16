from aiogram.filters import BaseFilter
from aiogram.types import Message

from config import ADMIN_IDS


class AdminFilter(BaseFilter):
    is_admin: bool = True

    async def __call__(self, obj: Message, admin_ids: ADMIN_IDS) -> bool:
        return (obj.from_user.id in admin_ids) == self.is_admin