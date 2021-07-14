import requests

from .Demotivator import Demotivator
from .Quote import Quote
from .TextGen import TextGen

try:
    version = requests.get(
        'https://raw.githubusercontent.com/infqq/simpledemotivators/master/simpledemotivators/version.txt'
    ).text.splitlines()

    if version[0] != '2.0.1':
        print(f'[SimpleDemotivators] Данная версия библиотеки устарела,'
              f' обновитесь до v{version[0]} с GitHub\nИзменения: {version[1]}')

except requests.exceptions.RequestException:
    print('[SimpleDemotivators] Не удалось проверить версию библиотеки на актуальность')

__all__ = (
    'Demotivator',
    'Quote',
    'TextGen'
)
