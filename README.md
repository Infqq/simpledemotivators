<h1 align="center">SimpleDemotivators</h1>
<p align="center">
    <img alt="Made with Python" src="https://img.shields.io/badge/Made%20with-Python-%23FFD242?logo=python&logoColor=white">
    <img alt="Repo size" src="https://img.shields.io/github/repo-size/Infqq/simpledemotivators">
    <img alt="issues" src="https://img.shields.io/github/issues/Infqq/simpledemotivators">
    <img alt="release" src="https://img.shields.io/github/v/release/Infqq/simpledemotivators">
    <blockquote>Создать демотиватор? Легко!</blockquote>

![prikol1](demresult.jpg)

## Установка
1) Стабильная версия через GitHub: 
   
   ```sh
   pip3 install https://github.com/Infqq/simpledemotivators/archive/main.zip --upgrade
   ```
2) Стабильная версия из PyPi:

   ```sh
   pip3 install simpledemotivators
   ```
3) Версия в разработке через GitHub (данная версия может быть с багами и вообще неработоспособной!):

   ```sh
   pip3 install https://github.com/Infqq/simpledemotivators/archive/dev.zip --upgrade
   ```

На Windows: pip

На Linux/MacOS - pip3

### Примеры использования
1. Demotivator() - создает простой демотиватор с дефолтным шаблоном.
```python
from simpledemotivators import Demotivator

dem = Demotivator('Эй', 'что?') # 2 строчки
dem.create('filename.jpg') # Название изображения, которое будет взято за основу демотиватора
```

2. Quote() - создает цитату
```python 
from simpledemotivators import Quote

a = Quote('text', "name")
a.create('filename.png') # Файл аватарки юзера, сохраняет с названием qresult.jpg
```

### Документация
* [Demotivator() - подробная документация](./docs/demotivator.md)
* [Quote() - подробная документация](./docs/quote.md)
* [Возможные ошибки](./docs/errors.md)
