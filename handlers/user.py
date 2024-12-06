from aiogram import Router

from aiogram.filters.command import Command
from aiogram.types import Message
from aiogram import F

from middleware import jaccard_index
from locales.localization import RuLocal
from locales.faq import business_club_faq_ru

router = Router()

@router.message(Command('start'))
async def greeting(msg: Message):
    await msg.reply(RuLocal.greeting)

@router.message(F.text())
async def question(msg: Message):
    if msg.text:
        sims = {}
        for i in business_club_faq_ru.keys():
            sims[jaccard_index(i, str(msg.text))] = i
        await msg.answer(business_club_faq_ru[sims[max(sims.keys())]])
