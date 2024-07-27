from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Предсказания'),
            KeyboardButton(text='Статы'),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выбери нужную функцию'
)

type_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Прематч', callback_data='__type__ prematch'),
        InlineKeyboardButton(text='Лайф', callback_data='__type__ live'),
    ]
]
)

format_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='BO1', callback_data='__format__ bo1'),
        InlineKeyboardButton(text='BO2', callback_data='__format__ bo2'),
    ],
    [
        InlineKeyboardButton(text='BO3', callback_data='__format__ bo3'),
        InlineKeyboardButton(text='BO5', callback_data='__format__ bo5'),
    ]
]
)

map_list = [
    InlineKeyboardButton(text='MAP1', callback_data='__map__ map1'),
    InlineKeyboardButton(text='MAP2', callback_data='__map__ map2'),
    InlineKeyboardButton(text='MAP3', callback_data='__map__ map3'),
    InlineKeyboardButton(text='MAP4', callback_data='__map__ map3'),
    InlineKeyboardButton(text='MAP5', callback_data='__map__ map5'),
]

board = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Победа 1', callback_data='__rates__ first_command'),
        InlineKeyboardButton(text='Победа 2', callback_data='__rates__ second_command'),
    ],
    [
        InlineKeyboardButton(text='Продолжительность карты', callback_data='__rates__ map_duration'),
        InlineKeyboardButton(text='Тотал убийств', callback_data='__rates__ total_kills'),
    ],
    [
        InlineKeyboardButton(text='Фора по убийствам', callback_data='__rates__ kill_handicap'),
        InlineKeyboardButton(text='Гонка убийств', callback_data='__rates__ killing_race'),
    ]
])

map_duration = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Меньше 34', callback_data='__map_duration__ less34'),
        InlineKeyboardButton(text='Больше 34', callback_data='__map_duration__ more34'),
    ],
    [
        InlineKeyboardButton(text='Меньше 35', callback_data='__map_duration__ less35'),
        InlineKeyboardButton(text='Больше 35', callback_data='__map_duration__ more35'),
    ],
[
        InlineKeyboardButton(text='Меньше 36', callback_data='__map_duration__ less36'),
        InlineKeyboardButton(text='Больше 36', callback_data='__map_duration__ more36'),
    ],
[
        InlineKeyboardButton(text='Меньше 37', callback_data='__map_duration__ less37'),
        InlineKeyboardButton(text='Больше 37', callback_data='__map_duration__ more37'),
    ],
[
        InlineKeyboardButton(text='Меньше 38', callback_data='__map_duration__ less38'),
        InlineKeyboardButton(text='Больше 38', callback_data='__map_duration__ more38'),
    ],
[
        InlineKeyboardButton(text='Меньше 39', callback_data='__map_duration__ less39'),
        InlineKeyboardButton(text='Больше 39', callback_data='__map_duration__ more39'),
    ],
[
        InlineKeyboardButton(text='Меньше 40', callback_data='__map_duration__ less40'),
        InlineKeyboardButton(text='Больше 40', callback_data='__map_duration__ more40'),
    ],
])

total_kills = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Меньше 42.5', callback_data='__total_kills__ less42.5'),
        InlineKeyboardButton(text='Больше 42.5', callback_data='__total_kills__ more42.5'),
    ],
    [
        InlineKeyboardButton(text='Меньше 43.5', callback_data='__total_kills__ less43.5'),
        InlineKeyboardButton(text='Больше 43.5', callback_data='__total_kills__ more43.5'),
    ],
    [
        InlineKeyboardButton(text='Меньше 44.5', callback_data='__total_kills__ less44.5'),
        InlineKeyboardButton(text='Больше 44.5', callback_data='__total_kills__ more44.5'),
    ],
    [
        InlineKeyboardButton(text='Меньше 45.5', callback_data='__total_kills__ less45.5'),
        InlineKeyboardButton(text='Больше 45.5', callback_data='__total_kills__ more45.5'),
    ],
    [
        InlineKeyboardButton(text='Меньше 46.5', callback_data='__total_kills__ less46.5'),
        InlineKeyboardButton(text='Больше 46.5', callback_data='__total_kills__ more46.5'),
    ],
    [
        InlineKeyboardButton(text='Меньше 47.5', callback_data='__total_kills__ less47.5'),
        InlineKeyboardButton(text='Больше 47.5', callback_data='__total_kills__ more47.5'),
    ],
    [
        InlineKeyboardButton(text='Меньше 48.5', callback_data='__total_kills__ less48.5'),
        InlineKeyboardButton(text='Больше 48.5', callback_data='__total_kills__ more48.5'),
    ],
    [
        InlineKeyboardButton(text='Меньше 49.5', callback_data='__total_kills__ less49.5'),
        InlineKeyboardButton(text='Больше 49.5', callback_data='__total_kills__ more49.5'),
    ],
    [
        InlineKeyboardButton(text='Меньше 50.5', callback_data='__total_kills__ less50.5'),
        InlineKeyboardButton(text='Больше 50.5', callback_data='__total_kills__ more50.5'),
    ],
    [
        InlineKeyboardButton(text='Меньше 51.5', callback_data='__total_kills__ less51.5'),
        InlineKeyboardButton(text='Больше 51.5', callback_data='__total_kills__ more51.5'),
    ],
    [
        InlineKeyboardButton(text='Меньше 52.5', callback_data='__total_kills__ less52.5'),
        InlineKeyboardButton(text='Больше 52.5', callback_data='__total_kills__ more52.5'),
    ],
    [
        InlineKeyboardButton(text='Меньше 53.5', callback_data='__total_kills__ less53.5'),
        InlineKeyboardButton(text='Больше 53.5', callback_data='__total_kills__ more53.5'),
    ],[
        InlineKeyboardButton(text='Меньше 54.5', callback_data='__total_kills__ less54.5'),
        InlineKeyboardButton(text='Больше 54.5', callback_data='__total_kills__ more54.5'),
    ],
])

kill_handicap = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='-20,5', callback_data='__kill_handicap__ first -20,5'),
        InlineKeyboardButton(text='+20,5', callback_data='__kill_handicap__ second +20,5'),
    ],
    [
        InlineKeyboardButton(text='-18,5', callback_data='__kill_handicap__ first -18,5'),
        InlineKeyboardButton(text='+18,5', callback_data='__kill_handicap__ second +18,5'),
    ],
    [
        InlineKeyboardButton(text='-16,5', callback_data='__kill_handicap__ first -16,5'),
        InlineKeyboardButton(text='+16,5', callback_data='__kill_handicap__ second +16,5'),
    ],
    [
        InlineKeyboardButton(text='-14,5', callback_data='__kill_handicap__ first -14,5'),
        InlineKeyboardButton(text='+14,5', callback_data='__kill_handicap__ second +14,5'),
    ],
    [
        InlineKeyboardButton(text='-12,5', callback_data='__kill_handicap__ first -12,5'),
        InlineKeyboardButton(text='+12,5', callback_data='__kill_handicap__ second +12,5'),
    ],
    [
        InlineKeyboardButton(text='-10,5', callback_data='__kill_handicap__ first -10,5'),
        InlineKeyboardButton(text='+10,5', callback_data='__kill_handicap__ second +10,5'),
    ],
    [
        InlineKeyboardButton(text='-8,5', callback_data='__kill_handicap__ first -8,5'),
        InlineKeyboardButton(text='+8,5', callback_data='__kill_handicap__ second +8,5'),
    ],
    [
        InlineKeyboardButton(text='-6,5', callback_data='__kill_handicap__ first -6,5'),
        InlineKeyboardButton(text='+6,5', callback_data='__kill_handicap__ second +6,5'),
    ],
    [
        InlineKeyboardButton(text='-4,5', callback_data='__kill_handicap__ first -4,5'),
        InlineKeyboardButton(text='+4,5', callback_data='__kill_handicap__ second +4,5'),
    ],
    [
        InlineKeyboardButton(text='-2,5', callback_data='__kill_handicap__ first -2,5'),
        InlineKeyboardButton(text='+2,5', callback_data='__kill_handicap__ second +2,5'),
    ],
    [
        InlineKeyboardButton(text='-0,5', callback_data='__kill_handicap__ first -0,5'),
        InlineKeyboardButton(text='+0,5', callback_data='__kill_handicap__ second +0,5'),
    ],
    [
        InlineKeyboardButton(text='+0,5', callback_data='__kill_handicap__ first +0,5'),
        InlineKeyboardButton(text='-0,5', callback_data='__kill_handicap__ second -0,5'),
    ],
    [
        InlineKeyboardButton(text='+2,5', callback_data='__kill_handicap__ first +2,5'),
        InlineKeyboardButton(text='-2,5', callback_data='__kill_handicap__ second -2,5'),
    ],
    [
        InlineKeyboardButton(text='+4,5', callback_data='__kill_handicap__ first +4,5'),
        InlineKeyboardButton(text='-4,5', callback_data='__kill_handicap__ second -4,5'),
    ],
    [
        InlineKeyboardButton(text='+6,5', callback_data='__kill_handicap__ first +6,5'),
        InlineKeyboardButton(text='-6,5', callback_data='__kill_handicap__ second -6,5'),
    ],
    [
        InlineKeyboardButton(text='+8,5', callback_data='__kill_handicap__ first +8,5'),
        InlineKeyboardButton(text='-8,5', callback_data='__kill_handicap__ second -8,5'),
    ],
    [
        InlineKeyboardButton(text='+10,5', callback_data='__kill_handicap__ first +10,5'),
        InlineKeyboardButton(text='-10,5', callback_data='__kill_handicap__ second -10,5'),
    ],
    [
        InlineKeyboardButton(text='+12,5', callback_data='__kill_handicap__ first +12,5'),
        InlineKeyboardButton(text='-12,5', callback_data='__kill_handicap__ second -12,5'),
    ],
    [
        InlineKeyboardButton(text='+14,5', callback_data='__kill_handicap__ first +14,5'),
        InlineKeyboardButton(text='-14,5', callback_data='__kill_handicap__ second -14,5'),
    ],
    [
        InlineKeyboardButton(text='+16,5', callback_data='__kill_handicap__ first +16,5'),
        InlineKeyboardButton(text='-16,5', callback_data='__kill_handicap__ second -16,5'),
    ],
    [
        InlineKeyboardButton(text='+18,5', callback_data='__kill_handicap__ first +18,5'),
        InlineKeyboardButton(text='-18,5', callback_data='__kill_handicap__ second -18,5'),
    ],
    [
        InlineKeyboardButton(text='+20,5', callback_data='__kill_handicap__ first +20,5'),
        InlineKeyboardButton(text='-20,5', callback_data='__kill_handicap__ second -20,5'),
    ],
])

killing_race = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='5', callback_data='__killing_race__ first 5'),
        InlineKeyboardButton(text='5', callback_data='__killing_race__ second 5'),
    ],
    [
        InlineKeyboardButton(text='10', callback_data='__killing_race__ first 10'),
        InlineKeyboardButton(text='10', callback_data='__killing_race__ second 10'),
    ],
    [
        InlineKeyboardButton(text='15', callback_data='__killing_race__ first 15'),
        InlineKeyboardButton(text='15', callback_data='__killing_race__ second 15'),
    ],
    [
        InlineKeyboardButton(text='20', callback_data='__killing_race__ first 20'),
        InlineKeyboardButton(text='20', callback_data='__killing_race__ second 20'),
    ],
])


bo1_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Победа 1', callback_data='__format_bo1__ first_win'),
        InlineKeyboardButton(text='Победа 2', callback_data='__format_bo1__ second_win'),
    ],
    [
        InlineKeyboardButton(text='Статистика', callback_data='__statistic__ statistic_bo1'),
        InlineKeyboardButton(text='Другое', callback_data='__other__ other_bo1'),
    ],
])

bo2_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Победа 1', callback_data='__format_bo2__ first_win'),
        InlineKeyboardButton(text='Ничья', callback_data='__format_bo2__ draw'),
        InlineKeyboardButton(text='Победа 2', callback_data='__format_bo2__ second_win'),
    ],
    [
        InlineKeyboardButton(text='Статистика', callback_data='__statistic__ statistic_bo2'),
        InlineKeyboardButton(text='Другое', callback_data='__other__ other_bo2'),
    ],
]
)

bo3_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='2:0', callback_data='__format_bo3__ two_zero'),
        InlineKeyboardButton(text='2:1', callback_data='__format_bo3__ two_one'),
        InlineKeyboardButton(text='1:2', callback_data='__format_bo5__ one_two'),
        InlineKeyboardButton(text='0:2', callback_data='__format_bo5__ zero_two'),
    ],
    [
        InlineKeyboardButton(text='Статистика', callback_data='__statistic__ statistic_bo3'),
        InlineKeyboardButton(text='Другое', callback_data='__other__ other_bo3'),
    ],
]
)

bo5_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='3:0', callback_data='__format_bo5__ tree_zero'),
        InlineKeyboardButton(text='3:1', callback_data='__format_bo5__ tree_one'),
        InlineKeyboardButton(text='3:2', callback_data='__format_bo5__ tree_two'),
        InlineKeyboardButton(text='2:3', callback_data='__format_bo5__ two_three'),
        InlineKeyboardButton(text='1:3', callback_data='__format_bo5__ one_three'),
        InlineKeyboardButton(text='0:3', callback_data='__format_bo5__ zero_three'),
    ],
    [
        InlineKeyboardButton(text='Статистика', callback_data='__statistic__ statistic_bo5'),
        InlineKeyboardButton(text='Другое', callback_data='__other__ other_bo5'),
    ],
]
)

succ_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Подтверждаю', callback_data='__succecc__ confirm'),
        InlineKeyboardButton(text='Отмена', callback_data='__succecc__ cancel'),
    ],
]
)

commands_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Tundra', callback_data='__command__ Tundra'),
        InlineKeyboardButton(text='Gaimin Gladiators', callback_data='__command__ Gaimin Gladiators'),
    ],
    [
        InlineKeyboardButton(text='PSG.Quest', callback_data='__command__ PSG.Quest'),
        InlineKeyboardButton(text='Team Spirit', callback_data='__command__ Team Spirit'),
    ],
    [
        InlineKeyboardButton(text='BetBoom Team', callback_data='__command__ BetBoom Team'),
        InlineKeyboardButton(text='LGD', callback_data='__command__ LGD'),
    ],
    [
        InlineKeyboardButton(text='OG', callback_data='__command__ OG'),
        InlineKeyboardButton(text='Virtus.pro', callback_data='__command__ Virtus.pro')
    ],
    [
        InlineKeyboardButton(text='Xtreme Gaming', callback_data='__command__ Xtreme Gaming'),
        InlineKeyboardButton(text='Mouz', callback_data='__command__ Mouz')
    ],
    [
        InlineKeyboardButton(text='Beastcoast', callback_data='__command__ Beastcoast'),
        InlineKeyboardButton(text='Entity Gaming', callback_data='__command__ Entity Gaming')
    ],
    [
        InlineKeyboardButton(text='G2 IG', callback_data='__command__ G2 IG'),
        InlineKeyboardButton(text='Azure Ray', callback_data='__command__ Azure Ray')
    ],
    [
        InlineKeyboardButton(text='Aurora', callback_data='__command__ Aurora'),
        InlineKeyboardButton(text='Blacklist International', callback_data='__command__ Blacklist International')
    ],
    [
        InlineKeyboardButton(text='Nouns', callback_data='__command__ Nouns'),
        InlineKeyboardButton(text='Heroic', callback_data='__command__ Heroic')
    ]
])

score = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='+1', callback_data='first +1'),
        InlineKeyboardButton(text='+1', callback_data='second +1'),
    ],
    [
        InlineKeyboardButton(text='-1', callback_data='first -1'),
        InlineKeyboardButton(text='-1', callback_data='second -1'),
    ],
    [
        InlineKeyboardButton(text='Подтвердить', callback_data='success'),
        InlineKeyboardButton(text='Вернуться', callback_data='cancel'),
    ],
])
