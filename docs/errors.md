# Ошибки и их решение

| Ошибка | Описание |
| -------- | ---------|
| oserror: cannot open resource | Не найдены шрифты, необходимо установить. (Ubuntu - sudo apt-get install msttcorefonts)
| Не отображаются эмоджи в демотиваторе | Установите шрифт Symbola.ttf, после укажите данный шрифт в кастомизации. (В основной документации это есть)
| Не могу установить шрифт на Heroku | Скачайте в ВАШ репозиторий нужный шрифт (по дефолту times.ttf), после установите: pip3 install https://github.com/Infqq/simpledemotivators/archive/heroku-fix.zip --upgrade

# Не работает библиотека, что делать?
1. Запускаем код:
```python
from simpledemotivators import *

namefile = 'namefile.png'

try:
    dem = demcreate('Эй', 'что?')
    dem.makeImage(namefile)
    
    dem = arrangedem('чего?', 'того')
    dem.makeImage(namefile)
    
    a = quote('text', "name")
    a.get(namefile)
    
    rnd_sent = text_gen('Всем привет, я родился')
    result = rnd_sent.get_text(min_words=1, max_words=4)
    
    print('Библиотека полностью работает.')
except Exception as e:
    print(e)
```
Создаем Issue с ошибкой, если она есть.
