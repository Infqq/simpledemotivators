<h1 align="center">SimpleDemotivators</h1>
<p align="center">
    <img alt="Made with Python" src="https://img.shields.io/badge/Made%20with-Python-%23FFD242?logo=python&logoColor=white">
    <img alt="Repo size" src="https://img.shields.io/github/repo-size/Infqq/simpledemotivators">
    <img alt="issues" src="https://img.shields.io/github/issues/Infqq/simpledemotivators">
    <img alt="release" src="https://img.shields.io/github/v/release/Infqq/simpledemotivators">
</p>
    <blockquote>Создать демотиватор? Легко!</blockquote>
</p>

![prikol1](demresult.jpg)

## Установка
1) С помощью установщика pip из GitHub: 
   
   ```sh
   pip3 install https://github.com/Infqq/simpledemotivators/archive/main.zip --upgrade
   ```
2) С помощью установщика pip из pypi: 
   
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
a.create('filename.png') # Файл аватарки юзера, сохраняет с названием qresult.jpg
```

### Пример использования фотографии со стороннего веб ресурса
Допустим, вам нужно спарсить изображение для демотиватора/цитаты с сервера ВК/Дискорда. Чтобы не нагружать ваш код get реквестами, библиотека все сделает за вас.
```python 
from simpledemotivators import Demotivator

dem = Demotivator('Эй', 'что?')
dem.create('https://link_to_picture.ru/', url=True)
```

### Документация
* [Возможные ошибки](./docs/errors.md)
