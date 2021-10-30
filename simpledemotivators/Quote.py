from PIL import Image, ImageDraw, ImageFont
import textwrap
import requests
import os


class Quote:
    def __init__(self, quote_text, author_name):
        self._quote_text = quote_text
        self._author_name = author_name

    def get(self, file, result_filename='qresult.jpg', use_url=False,
            headline_text_font='verdana.ttf', headline_text_size=50,
            headline_text='Цитаты великих людей', author_name_font='times.ttf',
            author_name_size=40, quote_text_font='arial.ttf', quote_text_size=40) \
            -> bool:  # Returns True if method executed successfully

        text = ''
        lines = textwrap.wrap(self._quote_text, width=24)

        for i in lines:
            text = text + i + '\n'

        if len(text.splitlines()) > 9:
            lines = text.splitlines()[0:9]
            text = ''
            for i in lines:
                text = text + i + '\n'

        user_img = Image.new('RGB', (1155, 600), color='#000000')

        drawer = ImageDraw.Draw(user_img)
        font_1 = ImageFont.truetype(font=quote_text_font, size=quote_text_size, encoding='UTF-8')
        font_2 = ImageFont.truetype(font=headline_text_font, size=headline_text_size, encoding='UTF-8')
        font_3 = ImageFont.truetype(font=author_name_font, size=author_name_size, encoding='UTF-8')

        size_headline = drawer.textsize(headline_text, font=font_2)

        drawer.text((529, 120), text, fill='white', font=font_1)
        drawer.text((529, 490), '© ' + self._author_name, fill='white', font=font_3)
        drawer.text(((1155 - size_headline[0]) / 2, 25), headline_text, fill='white', font=font_2)

        if use_url:
            p = requests.get(file)
            out = open(r'quote_picture.jpg', "wb")
            out.write(p.content)
            out.close()

            file = 'quote_picture.jpg'

        img = Image.open(file).convert("RGBA").resize((400, 400))
        user_img.paste(img, (100, 130))

        user_img.save(result_filename)

        if use_url:
            os.remove('quote_picture.jpg')

        return True
