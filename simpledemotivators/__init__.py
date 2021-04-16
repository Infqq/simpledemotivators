import requests

from .Demotivator import Demotivator
from .Quote import Quote
from .Text_gen import Text_gen

version = requests.get(
        'https://raw.githubusercontent.com/infqq/simpledemotivators/master/simpledemotivators/version.txt'
        ).text.splitlines()

if version[0] != '2.0.0':
        print(
                f'[SimpleDemotivators] Данная версия библиотеки устарела, обновитесь до v{version[0]} с GitHub\nИзменения: {version[1]}')
        
__all__ = (
        'Demotivator',
        'Quote',
        'Text_gen'
)
