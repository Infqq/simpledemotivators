from PIL import Image, ImageDraw, ImageFont, ImageOps

class arrangedem:
    def __init__(
            self, text1, text2) -> str:

        self._text1 = text1
        self._text2 = text2

    def makeImage(
            self, file, RESULT_FILENAME='demresult.jpg', colortext='white',
            colorfill='black', fonttext='times.ttf', size2=80, size3=60
    ):

        """Создаем основу демотиватора

        Регулируем края демотиватора и вставляем изображение

        """
        user_img = Image.open(file).convert("RGBA")
        (width, height) = user_img.size
        img = Image.new('RGB', (width + 250, height + 240), color=colorfill)
        img_border = Image.new('RGB', (width + 10, height + 10), color=('#000000'))
        border = ImageOps.expand(img_border, border=2, fill='#ffffff')
        img.paste(border, (111, 96))
        img.paste(user_img, (118, 103))
        drawer = ImageDraw.Draw(img)

        """Определяем оптимальный размер шрифта"""

        font_1 = ImageFont.truetype(font=fonttext, size=50, encoding='UTF-8')
        textWidth = font_1.getsize(self._text1)[0]

        while textWidth >= (width + 250) - 20:
            font_1 = ImageFont.truetype(font=fonttext, size=size2, encoding='UTF-8')
            textWidth = font_1.getsize(self._text1)[0]
            size2 -= 1

        font_2 = ImageFont.truetype(font=fonttext, size=30, encoding='UTF-8')
        textWidth = font_2.getsize(self._text2)[0]

        while textWidth >= (width + 250) - 20:
            font_2 = ImageFont.truetype(font=fonttext, size=size3, encoding='UTF-8')
            textWidth = font_2.getsize(self._text2)[0]
            size3 -= 1

        """Перемещаем текст в демотиватор"""

        size_1 = drawer.textsize(self._text1, font=font_1)
        drawer.text((((width + 250) - size_1[0]) / 2, ((height + 170) - size_1[1])), self._text1, fill=colortext,
                    font=font_1)
        size_2 = drawer.textsize(self._text2, font=font_2)
        drawer.text((((width + 250) - size_2[0]) / 2, ((height + 215) - size_2[1])), self._text2, fill=colortext,
                    font=font_2)

        img.save(RESULT_FILENAME)
