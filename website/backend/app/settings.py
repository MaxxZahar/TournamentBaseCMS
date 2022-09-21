from garpixcms.settings import *  # noqa

INSTALLED_APPS += [  # noqa
    'home',
    'tournaments',
    'api',
    'captcha',
]

RECAPTCHA_PUBLIC_KEY = '6LcJ5hoiAAAAAChq77yt-6l15YM9E-cgaUkLiuql'
RECAPTCHA_PRIVATE_KEY = '6LcJ5hoiAAAAANrBj3CorlxffQJKbcgVbX8iReM6'
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']

MENU_TYPE_HEADER_MENU = 'header_menu'

MENU_TYPES = {
    MENU_TYPE_HEADER_MENU: {
        'title': 'Верхнее меню',
    },
}

CHOICE_MENU_TYPES = [(k, v['title']) for k, v in MENU_TYPES.items()]
