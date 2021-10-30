import requests

from .Demotivator import Demotivator
from .Quote import Quote
from .Text_gen import Text_gen

try:
    version = requests.get(
        'https://raw.githubusercontent.com/infqq/simpledemotivators/master/simpledemotivators/version.txt'
    ).text.splitlines()

    if version[0] != '2.0.1':
        print(
            f'[SimpleDemotivators] Данная версия библиотеки устарела, обновитесь до v{version[0]} с GitHub\n',
            'Изменения: {version[1]}')
except:
    print('[SimpleDemotivators] Не удалось проверить версию библиотеки на актуальность')

__all__ = (
    'Demotivator',
    'Quote'
)
