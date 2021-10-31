import requests

from .Demotivator import Demotivator
from .Quote import Quote

try:
    is_dev = True

    version = requests.get(
        'https://raw.githubusercontent.com/infqq/simpledemotivators/master/simpledemotivators/version.txt'
    ).text.splitlines()

    if is_dev:
        print("[SimpleDemotivators] Вы используете версию для разработчиков!",
              "\nПожалуйста не используйте эту версию при разработке реального проекта.")
    elif version[0] != '2.1.0':
        print(f'[SimpleDemotivators] Данная версия библиотеки устарела, обновитесь до v{version[0]} с GitHub',
              f'\nИзменения: {version[1]}')
except requests.exceptions.RequestException:
    print('[SimpleDemotivators] Не удалось проверить версию библиотеки на актуальность')

__all__ = (
    'Demotivator',
    'Quote'
)
