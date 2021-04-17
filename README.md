<h1 align="center">SimpleDemotivators</h1>
<p align="center">
    <img alt="Made with Python" src="https://img.shields.io/badge/Made%20with-Python-%23FFD242?logo=python&logoColor=white">
    <img alt="Repo size" src="https://img.shields.io/github/repo-size/Infqq/simpledemotivators">
    <img alt="issues" src="https://img.shields.io/github/issues/Infqq/simpledemotivators">
    <img alt="release" src="https://img.shields.io/github/v/release/Infqq/simpledemotivators">
</p>
    <blockquote>Создать демотиватор? Легко!</blockquote>
</p>
<hr>

![prikol1](demresult.jpg)

* [English documentation here](./docs/eng.md)

## Установка
1) С помощью установщика pip из GitHub: 
   
   ```sh
   pip3 install https://github.com/Infqq/simpledemotivators/archive/main.zip --upgrade
   ```
2) Для heroku (Тоже с GitHub'а): 
   
   ```sh
   pip3 install https://github.com/Infqq/simpledemotivators/archive/heroku-fix.zip --upgrade
   ```
3) С помощью установщика pip из pypi: 
   
   ```sh
   pip install simpledemotivators
   ```

### Использование
Сохраняет файл под названием - demresult.jpg

1. Demotivator() - создает простой демотиватор с дефолтным шаблоном.
```python
from simpledemotivators import Demotivator

dem = Demotivator('Эй', 'что?') #2 строчки, если вы хотите только одну, то оставьте вторые кавчки пустыми
dem.create('filename.jpg') #Название изображения, которое будет взято за основу демотиватора
```

2. Quote() - создает цитату "Цитаты великих людей"
```python 
from simpledemotivators import Quote

a = Quote('text', "name")
a.get('filename.png') # Файл аватарки юзера, сохраняет с названием qresult.jpg
```

3. Text_gen() - генерирует рандомный текст
```python 
from simpledemotivators import Text_gen

rnd_sent = Text_gen('Всем привет, я родился')

result = rnd_sent.get_text(min_words=1, max_words=4)

print(result) # Printed: привет, всем
```

### Аргументы функции .create() (Demotivator () )
| Переменная | Пример | Описание |
| -------- | --------- | ---------|
| RESULT_FILENAME | 'test.png' | Название сохраняемого файла
| colortext | 'white' | Цвет шрифта
| colorfill | 'black' | Цвет заднего фона
| fonttext | 'times.ttf' | Название шрифта
| line | 'демотиватор.com' | Вотемарка (только в Demotivator)
| arrange | True/False | Демотиватор регулирует рамки под фотографию
| url | True/False | Если у вас картинка берется с другого ресурса (сайт), то бот сам парсит с этой ссылки картинку. (Вместо файла придется вставлять ссылку)
| delete_file | True/False | После создания демотиватора, ваш файл (который взят за основу демотиватора) будет удален.

Пример использования:
```python 
from simpledemotivators import Demotivator

dem = Demotivator('Эй', 'что?')
dem.create('A-lbiRuxv_k.jpg', colorfill='black', fonttext='arialbd.ttf', line='демотиватор.com', arrange=True)
```

### Пример использования фотографии со стороннего веб ресурса
Допустим, вам нужно спарсить изображение для демотиватора/цитаты с сервера ВК/Дискорда. Чтобы не нагружать ваш код get реквестами, библиотека все сделает за вас.
```python 
from simpledemotivators import Demotivator

dem = Demotivator('Эй', 'что?')
dem.create('https://link_to_picture.ru/', url = True)
```

### Документация
* [Возможные ошибки](./docs/errors.md)

[![Stargazers over time](https://starchart.cc/Infqq/simpledemotivators.svg)](https://starchart.cc/Infqq/simpledemotivators)
