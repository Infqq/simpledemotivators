<h1 align="center">SimpleDemotivators</h1>
    <blockquote>Создать демотиватор? Легко!</blockquote>
</p>
<hr>

## Установка
1) С помощью установщика pip из GitHub: 
   
   ```sh
   pip3 install https://github.com/Infqq/simpledemotivators/archive/main.zip --upgrade
   ```

### Использование
Сохраняет файл под названием - demresult.jpg

```python
from simpledemotivators import demcreate

dem = demcreate('Эй', 'что?') #2 строчки, если вы хотите только одну, то оставьте вторые кавчки пустыми
dem.makeImage('filename') #Название изображения, которое будет взято за основу демотиватора
```
