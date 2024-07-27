import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Filter
from aiogram.types import Message, CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import kbr

dp = Dispatcher()

chat_id = int('-100' + str(2201632419))


class MyFilter(Filter):
    def __init__(self, text: str) -> None:
        self.text = text

    async def __call__(self, message: Message | CallbackQuery) -> bool:
        if isinstance(message, Message):
            return message.text == self.text
        elif isinstance(message, CallbackQuery):
            return str(message.data.split()[0]) == self.text


@dp.message(CommandStart())
async def start_message(message: Message) -> None:
    try:
        dp['data'] = {
            'first_command': '',
            'second_command': '',
            'winner': '',
            'type': '',
            'format': '',
            'score_first': 0,
            'score_second': 0,
            'map': 0,
            'rate_type': '',
            'rate': ''
        }
        await message.answer(f"Здравствуйте, {html.bold(message.from_user.full_name)}, чтобы вы хотели от меня?",
                             reply_markup=kbr.start_kb)
    except Exception as e:
        await message.answer('start_message_error', e)


@dp.message(MyFilter('Предсказания'))
async def predict_handler(message: Message) -> None:
    try:
        dp['data'] = {
            'first_command': '',
            'second_command': '',
            'winner': '',
            'type': '',
            'format': '',
            'score_first': 0,
            'score_second': 0,
            'map': 0,
            'rate_type': '',
            'rate': ''
        }
        await message.answer(f"Выбрать команду", reply_markup=kbr.commands_kb)
    except Exception as e:
        await message.answer('predict_handler_error', e)


@dp.callback_query(MyFilter('__command__'))
async def callback_query_command(callback_query: CallbackQuery) -> None:
    try:
        bot = dp.get('bot')
        if not dp['data']['first_command']:
            dp['data']['first_command'] = ' '.join(callback_query.data.split()[1:])
            return

        if not dp['data']['second_command']:
            dp['data']['second_command'] = ' '.join(callback_query.data.split()[1:])
            await bot.send_message(chat_id=callback_query.from_user.id, text="Выбрать тип", reply_markup=kbr.type_kb)
            return
    except Exception as e:
        await bot.send_message(chat_id=callback_query.from_user.id, text="callback_query_command_error" + e.message)


@dp.callback_query(MyFilter('__type__'))
async def callback_query_type(callback_query: CallbackQuery) -> None:
    try:
        bot = dp.get('bot')
        dp['data']['type'] = callback_query.data.split()[1]
        await bot.send_message(chat_id=callback_query.from_user.id, text="Выбрать формат", reply_markup=kbr.format_kb)
        return
    except Exception as e:
        await bot.send_message(chat_id=callback_query.from_user.id, text="callback_query_type_error" + e.message)


@dp.callback_query(MyFilter('__format__'))
async def callback_query_format(callback_query: CallbackQuery) -> None:
    d = {
        'bo1': kbr.bo1_kb,
        'bo2': kbr.bo2_kb,
        'bo3': kbr.bo3_kb,
        'bo5': kbr.bo5_kb,
    }
    try:
        a = dp['data']
        bot = dp.get('bot')
        dp['data']['format'] = callback_query.data.split()[1]

        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f"Матч {html.bold(dp['data']['format'])}\n {html.bold(dp['data']['first_command'])} VS {html.bold(dp['data']['second_command'])}",
                               reply_markup=d[dp['data']['format']])

        return
    except Exception as e:
        await bot.send_message(chat_id=callback_query.from_user.id, text="callback_query_format_error" + e.message)


@dp.callback_query(MyFilter('__format_bo1__'))
async def callback_query_format_bo1(callback_query: CallbackQuery) -> None:
    bot = dp.get('bot')
    try:
        dp['data']['winner'] = callback_query.data.split()[1]
        if dp['data']['winner'] == 'first_win':
            dp['data']['score_first'] = 1
            dp['data']['winner'] = dp['data']['first_command']
        elif dp['data']['winner'] == 'second_win':
            dp['data']['score_second'] = 1
            dp['data']['winner'] = dp['data']['second_command']

        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f"Матч {html.bold(dp['data']['format'])}, {html.bold(dp['data']['first_command'])} VS {html.bold(dp['data']['second_command'])}\n"
                                    f"Победа {html.bold(dp['data']['winner'])}", reply_markup=kbr.succ_kb)
    except Exception as e:
        await bot.send_message(chat_id=callback_query.from_user.id, text="callback_query_format_bo1_error" + e.message)


@dp.callback_query(MyFilter('__format_bo2__'))
async def callback_query_format_bo2(callback_query: CallbackQuery) -> None:
    bot = dp.get('bot')
    try:
        dp['data']['winner'] = callback_query.data.split()[1]
        if dp['data']['winner'] == 'first_win':
            dp['data']['score_first'] = 2
            dp['data']['winner'] = dp['data']['first_command']
        elif dp['data']['winner'] == 'second_win':
            dp['data']['score_second'] = 2
            dp['data']['winner'] = dp['data']['second_command']
        elif dp['data']['winner'] == 'draw':
            dp['data']['score_second'] = 1
            dp['data']['score_first'] = 1
            dp['data']['winner'] = 'Ничья'

        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f"Матч {html.bold(dp['data']['format'])}, {html.bold(dp['data']['first_command'])} VS {html.bold(dp['data']['second_command'])}\n"
                                    f"{html.bold(dp['data']['score_first'])}:{html.bold(dp['data']['score_second'])}\n"
                                    f"{'' if dp['data']['winner'] == 'draw' else 'Победитель -'} {html.bold(dp['data']['winner'])}",
                               reply_markup=kbr.succ_kb)
    except Exception as e:
        await bot.send_message(chat_id=callback_query.from_user.id, text="callback_query_format_bo2_error" + e.message)


@dp.callback_query(MyFilter('__format_bo3__'))
async def callback_query_format_bo3(callback_query: CallbackQuery) -> None:
    bot = dp.get('bot')
    try:
        dp['data']['winner'] = callback_query.data.split()[1]
        if dp['data']['winner'] == 'two_zero':
            dp['data']['score_first'] = 2
            dp['data']['score_second'] = 0
            dp['data']['winner'] = dp['data']['first_command']
        elif dp['data']['winner'] == 'two_one':
            dp['data']['score_first'] = 2
            dp['data']['score_second'] = 1
            dp['data']['winner'] = dp['data']['first_command']
        elif dp['data']['winner'] == 'one_two':
            dp['data']['score_first'] = 1
            dp['data']['score_second'] = 2
            dp['data']['winner'] = dp['data']['second_command']
        elif dp['data']['winner'] == 'zero_two':
            dp['data']['score_first'] = 0
            dp['data']['score_second'] = 2
            dp['data']['winner'] = dp['data']['second_command']

        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f"Матч {html.bold(dp['data']['format'])}, {html.bold(dp['data']['first_command'])} VS {html.bold(dp['data']['second_command'])}\n"
                                    f"{html.bold(dp['data']['score_first'])}:{html.bold(dp['data']['score_second'])}\n"
                                    f"Победитель - {html.bold(dp['data']['winner'])}", reply_markup=kbr.succ_kb)
    except Exception as e:
        await bot.send_message(chat_id=callback_query.from_user.id, text="callback_query_format_bo3_error" + e.message)


@dp.callback_query(MyFilter('__format_bo5__'))
async def callback_query_format_bo5(callback_query: CallbackQuery) -> None:
    bot = dp.get('bot')
    a = dp['data']
    try:
        dp['data']['winner'] = callback_query.data.split()[1]
        if dp['data']['winner'] == 'tree_zero':
            dp['data']['score_first'] = 3
            dp['data']['score_second'] = 0
            dp['data']['winner'] = dp['data']['first_command']
        elif dp['data']['winner'] == 'tree_one':
            dp['data']['score_first'] = 3
            dp['data']['score_second'] = 1
            dp['data']['winner'] = dp['data']['first_command']
        elif dp['data']['winner'] == 'tree_two':
            dp['data']['score_first'] = 3
            dp['data']['score_second'] = 2
            dp['data']['winner'] = dp['data']['first_command']
        elif dp['data']['winner'] == 'two_three':
            dp['data']['score_first'] = 2
            dp['data']['score_second'] = 3
            dp['data']['winner'] = dp['data']['second_command']
        elif dp['data']['winner'] == 'one_three':
            dp['data']['score_first'] = 1
            dp['data']['score_second'] = 3
            dp['data']['winner'] = dp['data']['second_command']
        elif dp['data']['winner'] == 'zero_three':
            dp['data']['score_first'] = 0
            dp['data']['score_second'] = 3
            dp['data']['winner'] = dp['data']['second_command']

        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f"Матч {html.bold(dp['data']['format'])}, {html.bold(dp['data']['first_command'])} VS {html.bold(dp['data']['second_command'])}\n"
                                    f"{html.bold(dp['data']['score_first'])}:{html.bold(dp['data']['score_second'])}\n"
                                    f"Победитель - {html.bold(dp['data']['winner'])}", reply_markup=kbr.succ_kb)
    except Exception as e:
        await bot.send_message(chat_id=callback_query.from_user.id, text="callback_query_format_bo1_error" + e.message)


@dp.callback_query(MyFilter('__map__'))
async def callback_query_map(callback_query: CallbackQuery) -> None:
    bot = dp.get('bot')
    dp['data']['map'] = callback_query.data.split()[1]
    try:
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=callback_query.message.text + f'\nКарта{dp["data"]["map"][-1]}', reply_markup=
                               kbr.board)
    except Exception as e:
        await bot.send_message(chat_id=callback_query.from_user.id, text="callback_query_map_error" + e.message)


@dp.callback_query(MyFilter('__rates__'))
async def callback_query_rates(callback_query: CallbackQuery) -> None:
    bot = dp.get('bot')
    a = dp['data']
    d = {
        'map_duration': kbr.map_duration,
        'total_kills': kbr.total_kills,
        'kill_handicap': kbr.kill_handicap,
        'killing_race': kbr.killing_race
    }
    dp['data']['rate_type'] = callback_query.data.split()[1]
    try:
        if dp['data']['rate_type'] == 'first_command' or dp['data']['rate_type'] == 'second_command':
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text=callback_query.message.text + f'\nПобеда команды {dp["data"][dp["data"]["rate_type"]]}', reply_markup=kbr.succ_kb)
        else:
            await bot.send_message(chat_id=callback_query.from_user.id,
                               text=callback_query.message.text, reply_markup=d[dp['data']['rate_type']])
    except Exception as e:
        await bot.send_message(chat_id=callback_query.from_user.id, text="callback_query_statistic_rates" + e.message)


@dp.callback_query(MyFilter('__map_duration__'))
async def callback_query_map_duration(callback_query: CallbackQuery) -> None:
    bot = dp.get('bot')
    dp['data']['rate'] = callback_query.data.split()[1]
    try:
        a = dp['data']['rate'][-2:]
        b = dp['data']['rate'][-6:-2]
        if b == 'less':
            b = 'Меньше'
        elif b == 'more':
            b = 'Больше'
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=callback_query.message.text + '\n' + 'Продолжительность карты ' + b + ' ' + a,
                               reply_markup=kbr.succ_kb)
    except Exception as e:
        await bot.send_message(chat_id=callback_query.from_user.id, text="callback_query_map_duration_error" + e.message)


@dp.callback_query(MyFilter('__total_kills__'))
async def callback_query_total_kills(callback_query: CallbackQuery) -> None:
    bot = dp.get('bot')
    dp['data']['rate'] = callback_query.data.split()[1]
    try:
        a = dp['data']['rate'][-4:]
        b = dp['data']['rate'][-8:-4]
        if b == 'less':
            b = 'Меньше'
        elif b == 'more':
            b = 'Больше'
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=callback_query.message.text + '\n' + 'Тотал убийств ' + b + ' ' + a, reply_markup=
                               kbr.succ_kb)
    except Exception as e:
        await bot.send_message(chat_id=callback_query.from_user.id, text="callback_query_total_kills_error" + e.message)


@dp.callback_query(MyFilter('__kill_handicap__'))
async def callback_query_total_kill_handicap(callback_query: CallbackQuery) -> None:
    bot = dp.get('bot')
    dp['data']['rate'] = [callback_query.data.split()[1], callback_query.data.split()[2]]
    try:
        a = dp['data']['rate'][0]
        b = dp['data']['rate'][1]
        if a == 'first':
            a = dp['data']['first_command']
        elif a == 'second':
            a = dp['data']['second_command']
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=callback_query.message.text + '\n' + 'Фора по убийствам ' + b + ' ' + a, reply_markup=
                               kbr.succ_kb)
    except Exception as e:
        await bot.send_message(chat_id=callback_query.from_user.id, text="callback_query_total_kill_handicap_error" + e.message)


@dp.callback_query(MyFilter('__killing_race__'))
async def callback_query_total_killing_race(callback_query: CallbackQuery) -> None:
    bot = dp.get('bot')
    dp['data']['rate'] = [callback_query.data.split()[1], callback_query.data.split()[2]]
    try:
        a = dp['data']['rate'][0]
        b = dp['data']['rate'][1]
        if a == 'first':
            a = dp['data']['first_command']
        elif a == 'second':
            a = dp['data']['second_command']
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=callback_query.message.text + '\n' + 'Гонка убийств ' + b + ' ' + a, reply_markup=
                               kbr.succ_kb)
    except Exception as e:
        await bot.send_message(chat_id=callback_query.from_user.id, text="callback_query_total_killing_race_error" + e.message)

@dp.callback_query(MyFilter('__succecc__'))
async def callback_query_succecc(callback_query: CallbackQuery) -> None:
    bot = dp.get('bot')
    try:
        if callback_query.data.split()[1] == 'confirm':
            await bot.send_message(chat_id=chat_id,
                                   text=callback_query.message.text)
        elif callback_query.data.split()[1] == 'cancel':
            await bot.send_message(chat_id=callback_query.from_user.id, text=f"Что будем предсказывать?",
                                   reply_markup=kbr.start_kb)

    except Exception as e:
        await bot.send_message(chat_id=callback_query.from_user.id, text="callback_query_succecc_error" + e.message)


@dp.callback_query(MyFilter('__statistic__'))
async def callback_query_statistic(callback_query: CallbackQuery) -> None:
    bot = dp.get('bot')
    a = kbr.map_list
    try:
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=callback_query.message.text, reply_markup=
                               InlineKeyboardMarkup(inline_keyboard=[
                                   kbr.map_list[:int(callback_query.data[-1])],
                               ]))
    except Exception as e:
        await bot.send_message(chat_id=callback_query.from_user.id, text="callback_query_statistic_error" + e.message)


# @dp.message(CommandStart())
# async def command_start_handler(message: Message) -> None:
#     await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup=kbr.start_kb)
#     # await message.answer(f"Ваш ID чата: {html.code(message.chat.id)}")
#
#
#
#
# @dp.message(MyFilter('Предсказание на матч'))
# async def match_predict_handler(message: Message) -> None:
#     try:
#         dp['data'] = {
#             'first_command': '',
#             'second_command': '',
#             'winner': '',
#             'type': 'match_predict',
#             'score_first': 0,
#             'score_second': 0,
#         }
#         await message.answer(f"Выбрать команду", reply_markup=kbr.string_builder)
#     except Exception as e:
#         print(e)
#         await message.answer('ошибка')
#
#
# @dp.callback_query()
# async def callback_handler(callback_query: CallbackQuery) -> None:
#     a = dp['data']
#     bot = dp.get('bot')
#
#     if not dp['data']['first_command']:
#         dp['data']['first_command'] = callback_query.data
#         return
#
#     if dp['data']['type'] == 'map_predict':
#         if not dp['data']['second_command']:
#             dp['data']['second_command'] = callback_query.data
#             string_predict = InlineKeyboardMarkup(inline_keyboard=[
#                 [
#                     InlineKeyboardButton(text=dp['data']['first_command'], callback_data='first_command'),
#                     InlineKeyboardButton(text=dp['data']['second_command'], callback_data='second_command'),
#                 ],
#             ])
#             await bot.send_message(chat_id=callback_query.from_user.id, text="Кто победит?",
#                                    reply_markup=string_predict)
#             return
#
#         if 'first_command' == callback_query.data or 'second_command' == callback_query.data:
#             dp['data']['winner'] = dp['data'][callback_query.data]
#             await bot.send_message(chat_id=callback_query.from_user.id, text="Уверен?",
#                                    reply_markup=InlineKeyboardMarkup(inline_keyboard=[
#                                        [
#                                            InlineKeyboardButton(text='ДААА!!!',
#                                                                 callback_data='send_predict'),
#                                            InlineKeyboardButton(text='No.',
#                                                                 callback_data='clear_predict'),
#                                        ],
#                                    ]))
#             return
#
#         if 'send_predict' or 'clear_predict' in callback_query.data:
#             if 'send_predict' in callback_query.data:
#                 await bot.send_message(chat_id=chat_id,
#                                        text=f"Матч, {html.bold(dp['data']['first_command'])} VS {html.bold(dp['data']['second_command'])}\n Победа команды {html.bold(dp['data']['winner'])}")
#             elif 'clear_predict' in callback_query.data:
#                 await bot.send_message(chat_id=callback_query.from_user.id, text=f"Что будем предсказывать?",
#                                        reply_markup=kbr.start_kb)
#             dp['data'] = {
#                 'first_command': '',
#                 'second_command': '',
#                 'winner': '',
#                 'type': '',
#                 'score_first': 0,
#                 'score_second': 0,
#             }
#             return
#
#     elif dp['data']['type'] == 'match_predict':
#         if 'first' in callback_query.data or 'second' in callback_query.data:
#             dp['data']['score_' + callback_query.data.split()[0]] += int(callback_query.data.split()[1])
#             await bot.send_message(chat_id=callback_query.from_user.id, text=f"Счёт {html.bold(dp['data']['first_command'])} {html.bold(dp['data']['score_first'])} : {html.bold(dp['data']['score_second'])} {html.bold(dp['data']['second_command'])}",
#                                    reply_markup=kbr.score)
#             return
#
#         if 'success' in callback_query.data or 'cancel' in callback_query.data:
#             if 'success' == callback_query.data:
#                 await bot.send_message(chat_id=chat_id,
#                                        text=f"Матч {html.bold(dp['data']['first_command'])} {html.bold(dp['data']['score_first'])} : {html.bold(dp['data']['score_second'])} {html.bold(dp['data']['second_command'])}")
#             elif 'cancel' == callback_query.data:
#                 await bot.send_message(chat_id=callback_query.from_user.id, text=f"Что будем предсказывать?",
#                                        reply_markup=kbr.start_kb)
#             dp['data'] = {
#                 'first_command': '',
#                 'second_command': '',
#                 'winner': '',
#                 'type': '',
#                 'score_first': 0,
#                 'score_second': 0,
#             }
#             return
#
#         if not dp['data']['second_command']:
#             dp['data']['second_command'] = callback_query.data
#             await bot.send_message(chat_id=callback_query.from_user.id, text="Какой счёт?",
#                                    reply_markup=kbr.score)
#
#         if 'first_command' == callback_query.data or 'second_command' == callback_query.data:
#             if dp['data']['winner'] == dp['data'][callback_query.data]:
#                 await bot.send_message(chat_id=callback_query.from_user.id, text="Уверен?",
#                                        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
#                                            [
#                                                InlineKeyboardButton(text='ДААА!!!',
#                                                                     callback_data='send_predict'),
#                                                InlineKeyboardButton(text='No.',
#                                                                     callback_data='clear_predict'),
#                                            ],
#                                        ]))
#             return


async def main() -> None:
    bot = Bot(token='7329630317:AAGHiwqcAhPoYpiqorDzY2hOLFjPZzP083U',
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp['bot'] = bot
    dp['data'] = {
        'first_command': '',
        'second_command': '',
        'winner': '',
        'type': '',
        'format': '',
        'score_first': 0,
        'score_second': 0,
        'map': 0,
        'rate_type': '',
        'rate': ''
    }
    dp.bot = bot
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
