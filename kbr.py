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

bo1_kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Победа 1', callback_data='__format_bo1__ first_win'),
            InlineKeyboardButton(text='Победа 2', callback_data='__format_bo1__ second_win'),
        ],
    ]
)

bo2_kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Победа 1', callback_data='__format_bo2__ first_win'),
            InlineKeyboardButton(text='Ничья', callback_data='__format_bo2__ draw'),
            InlineKeyboardButton(text='Победа 2', callback_data='__format_bo2__ second_win'),
        ],
    ]
)

bo3_kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Победа 1', callback_data='__format_bo3__ first_win'),
            InlineKeyboardButton(text='Победа 2', callback_data='__format_bo3__ second_win'),
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