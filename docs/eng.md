<h1 align="center">SimpleDemotivators</h1>
    <blockquote>Create a demotivators? Its easy!</blockquote>
</p>
<hr>

![prikol1](demresult.jpg)

## Installing
1) By installer "pip" from GitHub
   
   ```sh
   pip3 install https://github.com/Infqq/simpledemotivators/archive/main.zip --upgrade
   ```
2) By installer pip from pypi
   
   ```sh
   pip install simpledemotivators
   ```

### Using
Saving file with tittle - demresult.jpg

1. demcreate() - Create simple demotivator
```python
from simpledemotivators import demcreate

dem = demcreate('Эй', 'что?')
dem.makeImage('filename.jpg')
```

2. arrangedem() - creating a demotivator with movable frames
```python 
from simpledemotivators import arrangedem

dem = arrangedem('чего?', 'того')
dem.makeImage('filename.png')
```

3. quote() - creating a quote
```python 
from simpledemotivators import quote

a = quote('text', "name")
a.get('filename.png')
```

### Arguments (demcreate и arrangedem)
| variable | example | description |
| -------- | --------- | ---------|
| RESULT_FILENAME | 'test.png' | saved file tiitle
| colortext | 'white' | text color
| colorfill | 'black' | fill color
| fonttext | 'times.ttf' | Font color

Example of using
```python 
from simpledemotivators import demcreate

dem = demcreate('Эй', 'что?')
dem.makeImage('A-lbiRuxv_k.jpg', colorfill='black', fonttext='arialbd.ttf')
```

### Watermark - setline (Only in demcreate!)
Adding watermark in demotivator

```python 
from simpledemotivators import demcreate

dem = demcreate('Ежжи', 'Сынок, ты с ума сошел.')
dem.makeImage('your_pic.png')
dem.setline('демотиватор.com')
```
![prikol2](setline_example.jpg)

[![Stargazers over time](https://starchart.cc/Infqq/simpledemotivators.svg)](https://starchart.cc/Infqq/simpledemotivators)
