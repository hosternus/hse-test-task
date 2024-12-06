from aiogram import Router

from aiogram.filters.command import Command
from aiogram.types import Message
from aiogram import F

from middleware import jaccard_index, addUserLastAction
from locales.localization import RuLocal
from locales.faq import business_club_faq_ru

router = Router()

@router.message(Command('start'))
async def greeting(msg: Message):
    if msg.from_user:
        addUserLastAction(msg.from_user.id, '/start')
    await msg.reply(RuLocal.greeting)

@router.message(F.text())
async def question(msg: Message):
    if (msg.text and msg.from_user):
        addUserLastAction(msg.from_user.id, 'question')
        sims = {}
        for i in business_club_faq_ru.keys():
            sims[jaccard_index(i, str(msg.text))] = i
        await msg.answer(business_club_faq_ru[sims[max(sims.keys())]])
