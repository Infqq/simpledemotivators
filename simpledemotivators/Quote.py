from PIL import Image, ImageDraw, ImageFont
import textwrap
import requests
import os


class Quote:
    def __init__(self, quote_text, author_name):
        """
        Инициализирует объект Цитата

        :param quote_text: текст цитаты
        :param author_name: имя автора цитаты
        """
        self._quote_text = quote_text
        self._author_name = author_name

    def create(self, file, result_filename='qresult.png', use_url=False,
            headline_text_font='verdana.ttf', headline_text_size=50,
            headline_text='Цитаты великих людей', author_name_font='ariali.ttf',
            author_name_size=50, quote_text_font='ariali.ttf', quote_text_size=40) \
            -> bool:  # Returns True if method executed successfully

        """
        Создает изображение с цитатой

        :param file: путь к файлу фотографии автора цитаты
        :param result_filename: имя файла результата
        :param use_url: True, если file - это URL
        :param headline_text_font: путь к файлу шрифта для заголовка
        :param headline_text_size: размер шрифта для заголовка
        :param headline_text: текст заголовка
        :param author_name_font: путь к файлу шрифта для имени автора
        :param author_name_size: размер шрифта для имени автора
        :param quote_text_font: путь к файлу шрифта для текста цитаты
        :param quote_text_size: размер шрифта для текста цитаты
        :return: True, если метод выполнился успешно
        """
        text = ''
        lines = textwrap.wrap(self._quote_text, width=40)

        for i in lines:
            text = text + i + '\n'

        if len(text.splitlines()) > 5:
            lines = text.splitlines()[0:5]
            text = ''
            for i in lines:
                text = text + i + '\n'

        user_img = Image.new('RGBA', (1000, 550), color='#000000')

        drawer = ImageDraw.Draw(user_img)
        font_1 = ImageFont.truetype(font=quote_text_font, size=quote_text_size, encoding='UTF-8')
        font_2 = ImageFont.truetype(font=headline_text_font, size=headline_text_size, encoding='UTF-8')
        font_3 = ImageFont.truetype(font=author_name_font, size=author_name_size, encoding='UTF-8')

        size_headline = drawer.textsize(headline_text, font=font_2)

        drawer.text((50, 120), f"«{text[:-1]}»", fill='white', font=font_1)
        drawer.text((230, 410), '© ' + self._author_name, fill='white', font=font_3)
        drawer.text(((1000 - size_headline[0]) / 2, 25), headline_text, fill='white', font=font_2)

        if use_url:
            p = requests.get(file)
            out = open(r'quote_picture.jpg', "wb")
            out.write(p.content)
            out.close()

            file = 'quote_picture.jpg'

        """
        Сглаживаем в форме круга фотографию автора цитаты
        """

        user_photo = Image.open(file).resize((150, 150)).convert("RGBA")
        width, height = user_photo.size
        user_photo.crop(((width - height) / 2, 0, (width + height) / 2, height))
        user_photo.resize((150, 150), Image.ANTIALIAS)
        mask = Image.new('L', (150 * 2, 150 * 2), 0)
        ImageDraw.Draw(mask).ellipse((0, 0) + mask.size, fill=255)
        user_photo.putalpha(mask.resize((150, 150), Image.ANTIALIAS))
        user_img.paste(user_photo, (50, 370), mask=user_photo)

        user_img.save(result_filename)

        if use_url:
            os.remove('quote_picture.jpg')

        return True
