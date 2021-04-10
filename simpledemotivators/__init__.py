import requests

from .demcreate import demcreate
from .arrangedem import arrangedem
from .quote import quote
from .text_gen import text_gen

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
        'demcreate',
        'arrangedem',
        'quote',
        'text_gen'
)