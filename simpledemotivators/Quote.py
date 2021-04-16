from PIL import Image, ImageDraw, ImageFont
import textwrap
import requests
import os


class Quote:
    def __init__(
            self, text, name) -> str:

        self._text = text
        self._name = name

    def get(
            self, file, RESULT_FILENAME='qresult.jpg', url=False):

        text = ''
        lines = textwrap.wrap(self._text, width=24)

        for i in lines: text = text + i + '\n'

        if len(text.splitlines()) > 9:
            lines = text.splitlines()[0:9]
            text = ''
            for i in lines: text = text + i + '\n'

        user_img = Image.new('RGB', (1155, 600), color=('#000000'))

        drawer = ImageDraw.Draw(user_img)
        font_1 = ImageFont.truetype(font='arialbd.ttf', size=40, encoding='UTF-8')
        font_2 = ImageFont.truetype(font='times.ttf', size=60, encoding='UTF-8')
        font_3 = ImageFont.truetype(font='times.ttf', size=40, encoding='UTF-8')

        drawer.text((529, 90), text, fill='white', font=font_1)

        drawer.text((529, 460), '© ' + self._name, fill='white', font=font_3)
        drawer.text((270, 5), 'Цитаты великих людей', fill='white', font=font_2)

        if url:
            p = requests.get(file)
            out = open(r'quote_picture.jpg', "wb")
            out.write(p.content)
            out.close()

            file = 'quote_picture.jpg'
        
        img = Image.open(file).convert("RGBA").resize((400, 400))
        user_img.paste(img, (100, 100))

        user_img.save(RESULT_FILENAME)
        
        if url:
            os.remove('quote_picture.jpg')
