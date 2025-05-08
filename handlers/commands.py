from aiogram import F, types, Router
from aiogram.filters import Command
from ..config import dp
import asyncio

router =Router()


@router.message(Command("start"))
async def cmd_start(message:types.Message):
    await message.answer('Здарова заебал')
dp.include_router(router)

