# Самостоятельная настройка демотиватора
## Пример кода
```python
from simpledemotivators import prodemoty

dem = prodemoty('советский', 'союз?')
dem.setimg(TEMPLATE_COORDS=(75, 45, 499, 373), TEMPLATE_WIDTH = 574, TEMPLATE_HEIGHT = 522, PADDING=10)
dem.setfont(UPPER_FONT = 'times.ttf', UPPER_SIZE = 45, UPPER_FONT_Y = 390, LOWER_FONT = 'arialbd.ttf', LOWER_SIZE = 14, LOWER_FONT_Y = 450)
dem.makeImage('filename')
```

### Разбор аргументов
| Переменная | Описание |
| -------- | ---------|
| TEMPLATE_COORDS | Координаты шаблона (4 значения)
| TEMPLATE_WIDTH  | Ширина шаблона
| TEMPLATE_HEIGHT | Высота шаблона
| PADDING | Грунтование
| UPPER_FONT | Название шрифта сверху
| UPPER_SIZE | Размер шрифта сверху
| UPPER_FONT_Y | Координаты текста сверху (1 значение)
| LOWER_FONT | Название шрифта снизу
| LOWER_SIZE | Размер шрифта снизу
| LOWER_FONT_Y | Координаты текста снизу (1 значение)
