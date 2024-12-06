from aiogram import Router

from aiogram.filters.command import Command
from aiogram.types import Message

from middleware import getNumberOfUsers
from locales.localization import AdminRuLocal

router = Router()

@router.message(Command('admin'))
async def numberOfUsers(msg: Message):
    await msg.reply(AdminRuLocal.numOfUsers + str(getNumberOfUsers()))