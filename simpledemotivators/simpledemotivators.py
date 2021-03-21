from PIL import Image, ImageDraw, ImageFont, ImageOps
import textwrap
import requests


version = requests.get(
        'https://raw.githubusercontent.com/infqq/simpledemotivators/master/version.txt'
        ).text.splitlines()[0] # Ужасный код по причине лишнего пробела при парсинге.

if version != '1.5.0':
        print(
                f'[SimpleDemotivators] Данная версия библиотеки устарела, обновитесь до v{version} с GitHub')
else:
        print(
                f'SimpleDemotivators v{version} started, version actual.')


class demcreate:
        def __init__(self, text1: str, text2: str) -> str:
                self._text1 = text1
                self._text2 = text2

        def makeImage(
                self, file, RESULT_FILENAME='demresult.jpg', colortext = 'white',
                colorfill = 'black', fonttext='times.ttf', size2 = 80, size3 = 60
                ):
                
                self._file = file
                """Создаем шаблон для демотиватора

                Вставляем фотографию в рамку
                
                """
                
                img = Image.new('RGB', (1280, 1024), color=colorfill)
                img_border = Image.new('RGB', (1060, 720), color=('#000000'))
                border = ImageOps.expand(img_border, border=2, fill='#ffffff')
                user_img = Image.open(file).convert("RGBA").resize((1050, 710))
                (width, height) = user_img.size
                img.paste(border, (111, 96))
                img.paste(user_img, (118, 103))
                drawer = ImageDraw.Draw(img)
                """Подбираем оптимальный размер шрифта

                Добавляем текст в шаблон для демотиватора
                
                """
                font_1 = ImageFont.truetype(font=fonttext, size=size2, encoding='UTF-8')
                textWidth = font_1.getsize(self._text1)[0]
                
                while textWidth >= (width+250) - 20:
                        font_1 = ImageFont.truetype(font=fonttext, size=size2, encoding='UTF-8')
                        textWidth = font_1.getsize(self._text1)[0]
                        size2 -= 1
                    
                font_2 = ImageFont.truetype(font=fonttext, size=size3, encoding='UTF-8')
                textWidth = font_2.getsize(self._text2)[0]
                
                while textWidth >= (width+250) - 20:
                        font_2 = ImageFont.truetype(font=fonttext, size=size3, encoding='UTF-8')
                        textWidth = font_2.getsize(self._text2)[0]
                        size3 -= 1
                        
                size_1 = drawer.textsize(self._text1, font=font_1)
                drawer.text(((1280 - size_1[0]) / 2, 820), self._text1, fill=colortext, font=font_1)
                size_2 = drawer.textsize(self._text2, font=font_2)
                drawer.text(((1280 - size_2[0]) / 2, 920), self._text2, fill=colortext, font=font_2)
                
                img.save(RESULT_FILENAME)

        def setline(self, text, RESULT_FILENAME='demresult.jpg'): # Лучше не использовать
                if len(text) > 12:
                        photo1 = Image.open(self._file)
                        (width, height) = photo1.size
                        idraw = ImageDraw.Draw(photo1)
                        idraw.line((780,815, 1020, 815), fill=0, width=4)
                        font_2 = ImageFont.truetype(font=fonttext, size=25, encoding='UTF-8')
                        size_2 = idraw.textsize(text, font=font_2)
                        idraw.text((((width+520) - size_2[0]) / 2, ((height-195) - size_2[1])), text, font=font_2)
                        photo1.save(RESULT_FILENAME)
                else:
                        photo1 = Image.open(RESULT_FILENAME)
                        (width, height) = photo1.size
                        idraw = ImageDraw.Draw(photo1)
                        idraw.line((940,817, 1065, 817), fill=0, width=4)
                        font_2 = ImageFont.truetype(font=fonttext, size=20, encoding='UTF-8')
                        size_2 = idraw.textsize(text, font=font_2)
                        idraw.text((((width+729) - size_2[0]) / 2, ((height-192) - size_2[1])), text, font=font_2)
                        photo1.save(RESULT_FILENAME)

class arrangedem:
        def __init__(self, text1: str, text2: str) -> str:
                self._text1 = text1
                self._text2 = text2

        def makeImage(self, file, RESULT_FILENAME='demresult.jpg'):
                size2 = 80
                size3 = 60
                user_img = Image.open(file).convert("RGBA")
                (width, height) = user_img.size
                img = Image.new('RGB', (width+250, height+240), color=('#000000'))
                img_border = Image.new('RGB', (width+10, height+10), color=('#000000'))
                border = ImageOps.expand(img_border, border=2, fill='#ffffff')
                img.paste(border, (111, 96))
                img.paste(user_img, (118, 103))
                drawer = ImageDraw.Draw(img)
                font_1 = ImageFont.truetype(font='times.ttf', size=50, encoding='UTF-8')
                textWidth = font_1.getsize(self._text1)[0]
                while textWidth >= (width+250) - 20:
                        font_1 = ImageFont.truetype(font='times.ttf', size=size2, encoding='UTF-8')
                        textWidth = font_1.getsize(self._text1)[0]
                        size2 -= 1
                font_2 = ImageFont.truetype(font='times.ttf', size=30, encoding='UTF-8')
                textWidth = font_2.getsize(self._text2)[0]
                while textWidth >= (width+250) - 20:
                        font_2 = ImageFont.truetype(font='times.ttf', size=size3, encoding='UTF-8')
                        textWidth = font_2.getsize(self._text2)[0]
                        size3 -= 1
                size_1 = drawer.textsize(self._text1, font=font_1)
                drawer.text((((width+250) - size_1[0]) / 2, ((height+170) - size_1[1])), self._text1, fill=(240, 230, 210), font=font_1)
                size_2 = drawer.textsize(self._text2, font=font_2)
                drawer.text((((width+250) - size_2[0]) / 2, ((height+215) - size_2[1])), self._text2, fill=(240, 230, 210), font=font_2)
                img.save(RESULT_FILENAME)

class quote:
        def __init__(self, text: str, name: str) -> str:
                self._text = text
                self._name = name

        def get(self, file, RESULT_FILENAME='qresult.jpg'):
                text = ''
                lines = textwrap.wrap('"' + self._text + '"', width=24)

                for i in lines:
                        text = text + i + '\n'
                user_img = Image.new('RGB', (1155, 600), color=('#000000'))

                drawer = ImageDraw.Draw(user_img)
                font_1 = ImageFont.truetype(font='arialbd.ttf', size=40, encoding='UTF-8')
                font_2 = ImageFont.truetype(font='times.ttf', size=60, encoding='UTF-8')

                drawer.text((529, 90), text[:292], fill='white', font=font_1)

                drawer.text((112, 510), self._name, fill='white', font=font_1)
                drawer.text((270, 5), 'Цитаты великих людей', fill='white', font=font_2)

                img = Image.open(file).convert("RGBA").resize((400, 400))
                user_img.paste(img, (100, 100))
                    
                user_img.save(RESULT_FILENAME)
