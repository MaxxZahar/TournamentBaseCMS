from garpixcms.settings import *  # noqa

INSTALLED_APPS += [  # noqa
    'home',
    'tournaments',
    'api',
]

MENU_TYPE_HEADER_MENU = 'header_menu'

MENU_TYPES = {
    MENU_TYPE_HEADER_MENU: {
        'title': 'Верхнее меню',
    },
}

CHOICE_MENU_TYPES = [(k, v['title']) for k, v in MENU_TYPES.items()]
