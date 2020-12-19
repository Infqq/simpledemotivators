<h1 align="center">SimpleDemotivators</h1>
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
2) С помощью установщика pip из pypi: 
   
   ```sh
   pip install simpledemotivators
   ```

### Использование
Сохраняет файл под названием - demresult.jpg

```python
from simpledemotivators import demcreate

dem = demcreate('Эй', 'что?') #2 строчки, если вы хотите только одну, то оставьте вторые кавчки пустыми
dem.makeImage('filename.jpg') #Название изображения, которое будет взято за основу демотиватора
```

или

```python
from simpledemotivators import prodemoty

dem = prodemoty('советский', 'союз?')
dem.setimg(TEMPLATE_COORDS=(75, 45, 499, 373), TEMPLATE_WIDTH = 574, TEMPLATE_HEIGHT = 522, PADDING=10)
dem.setfont(UPPER_FONT = 'times.ttf', UPPER_SIZE = 45, UPPER_FONT_Y = 390, LOWER_FONT = 'arialbd.ttf', LOWER_SIZE = 14, LOWER_FONT_Y = 450)
dem.makeImage('filename.jpg')
```

### Документация
* [Произвольные демотиваторы](./docs/prodemoty.md)

[![Stargazers over time](https://starchart.cc/Infqq/simpledemotivators.svg)](https://starchart.cc/Infqq/simpledemotivators)
