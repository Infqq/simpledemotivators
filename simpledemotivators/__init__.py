import requests

from .Demcreate import Demcreate
from .Arrangedem import Arrangedem
from .Quote import Quote
from .Text_gen import Text_gen

version = requests.get(
        'https://raw.githubusercontent.com/infqq/simpledemotivators/master/simpledemotivators/version.txt'
        ).text.splitlines()

if version[0] != '1.8.0':
        print(
                f'[SimpleDemotivators] Данная версия библиотеки устарела, обновитесь до v{version[0]} с GitHub\nИзменения: {version[1]}')
else:
        print(
                f'SimpleDemotivators v{version[0]} started, version actual.')

__all__ = (
        'Demcreate',
        'Arrangedem',
        'Quote',
        'Text_gen'
)
