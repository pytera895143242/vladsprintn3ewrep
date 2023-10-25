import asyncio
import json

from aiogram import types
from misc import dp, bot
from .sqlit import change_status,get_username,update_status
import random

text_stop = """<b>Аяяй я смотрю, кто-то решил
пошалить 😏

Сначала посмотри видео, а потом нажимай🙏🙃</b>"""



text_dogon = """Я вижу ты ещё не посмотрел(а) видосик и не вник в суть😎

Зачем забивать? Го зарабатывать 💸"""

from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

content = -1001768433035

class reg_p(StatesGroup):
    step1 = State()
    step2 = State()
    step3 = State()




@dp.callback_query_handler(lambda call: True, state = '*')
async def answer_push_inline_button(call, state: FSMContext):
    if call.data == 'go_1':
        update_status(call.message.chat.id, 1)
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='ДАВАЙ', callback_data='go_2')
        markup.add(bat_a)

        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id = 6)
        await asyncio.sleep(3)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id = 7)
        await asyncio.sleep(3)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id = 8, reply_markup=markup)

    if call.data == 'go_2':
        update_status(call.message.chat.id, 2)
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='РАССКАЖИ👂', callback_data='go_3')
        markup.add(bat_a)

        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id = 10)
        await asyncio.sleep(3)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=11, reply_markup=markup)



    if call.data == 'go_3':
        update_status(call.message.chat.id, 3)
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='ПРОДОЛЖЕНИЕ🔥', callback_data='go_4')
        markup.add(bat_a)

        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=13,reply_markup=markup)




    if call.data == 'go_4':
        update_status(call.message.chat.id, 4)
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='💸 СПРИНТ 💸', callback_data='go_5')
        markup.add(bat_a)

        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=15)
        await asyncio.sleep(2)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=17, reply_markup=markup)

    if call.data == 'go_5':
        update_status(call.message.chat.id, 5)
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='🔥НАЧИНАЕМ🔥', callback_data='go_6')
        markup.add(bat_a)

        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=19)
        await asyncio.sleep(2)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=21, reply_markup=markup)


    if call.data == 'go_6':
        update_status(call.message.chat.id, 6)
        await state.update_data(v1='stop')
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='😎ОП ОП😎', callback_data='go_7')
        markup.add(bat_a)

        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=24, reply_markup=markup)
        await asyncio.sleep(60) # 1  минута
        await state.update_data(v1='start')

        # поставить таймер на 30  минут!!
        await asyncio.sleep(1800) #если не нажимал на кнопку в течении 30 минут (1800)
        if ((await state.get_data())['v1']) != 'ready':
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=33)
            await call.message.answer("""Так кайфует тот, кто уже посмотрел видосик выше ☝️ 

<b>Погнали смотреть🙄</b>""",parse_mode='html')


    if call.data == 'go_7':
        try:
            if ((await state.get_data())['v1']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            update_status(call.message.chat.id, 7)
            await state.update_data(v1='ready')
            await state.update_data(v2='stop')

            markup = types.InlineKeyboardMarkup()
            bat_1 = types.InlineKeyboardButton(text='🤓ПРОЙТИ ТЕСТ🤓', callback_data='go_8')
            markup.add(bat_1)

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=35,reply_markup=markup)
            await asyncio.sleep(60) #Таймер на 60 секунд
            await state.update_data(v2='start')

            # поставить таймер на 30  минут!!
            await asyncio.sleep(1800)  # если не нажимал на кнопку в течении 30 минут (1800)
            if ((await state.get_data())['v2']) != 'ready':
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=37)
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=38)


    if call.data == 'go_8':
        try:
            if ((await state.get_data())['v2']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            update_status(call.message.chat.id, 8)
            await state.update_data(v2='ready')

            markup = types.InlineKeyboardMarkup()
            bat_1 = types.InlineKeyboardButton(text='1️⃣', callback_data='go_9')
            bat_2 = types.InlineKeyboardButton(text='2️⃣', callback_data='answer_false')
            bat_3 = types.InlineKeyboardButton(text='3️⃣', callback_data='answer_false')
            markup.add(bat_1, bat_2, bat_3)

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=39,reply_markup=markup)


    if call.data == 'answer_false':
        await bot.send_message(chat_id=call.message.chat.id, text= "<b>Нет, это не арбитраж трафика. Пересмотри видео и попробуй ещё раз🙃</b>", parse_mode='html')


    if call.data == 'go_9':
        update_status(call.message.chat.id, 9)

        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='🫡ГОТОВО✔️', callback_data='go_10')
        markup.add(bat_a)

        await state.update_data(v3='stop')
        await bot.send_message(chat_id=call.message.chat.id, text="""<b>Красава😎 Двигаемся дальше🚀</b>""",parse_mode='html')
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=43,reply_markup=markup)
        await asyncio.sleep(90)  # (90 сек)
        await state.update_data(v3='start')
        await asyncio.sleep(1800)  # если не нажимал на кнопку в течении 30 минут
        if ((await state.get_data())['v3']) != 'ready':
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=46)


    if call.data == 'go_10':
        try:
            if ((await state.get_data())['v3']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            update_status(call.message.chat.id, 10)
            await state.update_data(v3='ready')

            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='🫡ГОТОВО✔️', callback_data='go_11')
            markup.add(bat_a)

            await state.update_data(v4='stop')
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id = 47)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id = 49,reply_markup=markup)
            await asyncio.sleep(30)  # (30 сек)
            await state.update_data(v4='start')
            await asyncio.sleep(1800)  # если не нажимал на кнопку в течении 30 минут
            if ((await state.get_data())['v4']) != 'ready':
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=52)
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=53)

    if call.data == 'go_11':
        try:
            if ((await state.get_data())['v4']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            await state.update_data(v4='ready')
            update_status(call.message.chat.id, 11)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=56)
            await asyncio.sleep(240) #4 минуты
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=60)
            await asyncio.sleep(360)  # 6 минут
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=62)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=63)
            await asyncio.sleep(3600)  # 60 минут
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=65)
            await asyncio.sleep(5400)  # 90 минут
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=67)
            await asyncio.sleep(86400)  # 24 часа
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=69)
            await asyncio.sleep(21600)  # 6 часов
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=71)
            await asyncio.sleep(43200) # 12 часов
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=73)
            await asyncio.sleep(43200)  # 12 часов
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=75)
            await asyncio.sleep(43200)  # 12 часов
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=77)
            await asyncio.sleep(21600)  # 6 часов
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=79)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=80)
            await asyncio.sleep(86400)  # 24 часа
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=82)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=83)
            await asyncio.sleep(86400)  # 24 часа
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=85)