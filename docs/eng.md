<h1 align="center">SimpleDemotivators</h1>
    <blockquote>Create a demotivators? Its easy!</blockquote>
</p>
<hr>

## Installing
1) By installer "pip" from GitHub
   
   ```sh
   pip3 install https://github.com/Infqq/simpledemotivators/archive/main.zip --upgrade
   ```
2) For heroku (Also from GitHub): 
   
   ```sh
   pip3 install https://github.com/Infqq/simpledemotivators/archive/heroku-fix.zip --upgrade
   ```
2) By installer pip from pypi
   
   ```sh
   pip install simpledemotivators
   ```

### Using
Saving file with tittle - demresult.jpg

1. Demcreate() - Create simple demotivator
```python
from simpledemotivators import Demcreate

dem = Demcreate('text1', 'text2')
dem.makeImage('filename.jpg')
```

2. Arrangedem() - creating a demotivator with movable frames
```python 
from simpledemotivators import Arrangedem

dem = Arrangedem('text1', 'text2')
dem.makeImage('filename.png')
```

3. Quote() - creating a quote
```python 
from simpledemotivators import Quote

a = Quote('text', "name")
a.get('filename.png')
```

4. Text_gen() - generates random text
```python 
from simpledemotivators import Text_gen

rnd_sent = Text_gen('Hi all, I was born')
result = rnd_sent.get_text(min_words=1, max_words=4)
print(result)
```

### Arguments (demcreate и arrangedem)
| variable | example | description |
| -------- | --------- | ---------|
| RESULT_FILENAME | 'test.png' | saved file tiitle
| colortext | 'white' | text color
| colorfill | 'black' | fill color
| fonttext | 'times.ttf' | Font color
| line | 'demotivator.com' | watermark (only in demcreate)

Example of using
```python 
from simpledemotivators import Demcreate

dem = Demcreate('text1', 'text2')
dem.makeImage('A-lbiRuxv_k.jpg', colorfill='black', fonttext='arialbd.ttf', line='demotivator.com')
```

![prikol2](setline_example.jpg)

[![Stargazers over time](https://starchart.cc/Infqq/simpledemotivators.svg)](https://starchart.cc/Infqq/simpledemotivators)
