# Demotivator() - Подробная документация

# Пример использования
```python 
from simpledemotivators import Demotivator

dem = Demotivator('Эй', 'что?')
dem.create('your_photo.jpg', fill_color='black', font_name='arialbd.ttf', line='демотиватор.com', arrange=True)
```

### Аргументы функции .create()
| Переменная | Пример | Описание |
| -------- | --------- | ---------|
| result_filename | 'test.png' | Название сохраняемого файла
| color_name | 'white' | Цвет шрифта
| fill_color | 'black' | Цвет заднего фона
| font_name | 'times.ttf' | Название шрифта
| line | 'демотиватор.com' | Вотемарка (только в Demotivator)
| arrange | True/False | Демотиватор регулирует рамки под фотографию
| use_url | True/False | Если у вас картинка берется с другого ресурса (сайт), то бот сам парсит с этой ссылки картинку. (Вместо файла придется вставлять ссылку)
| delete_file | True/False | После создания демотиватора, ваш файл (который взят за основу демотиватора) будет удален.
