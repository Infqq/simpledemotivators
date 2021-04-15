from PIL import Image, ImageDraw, ImageFont, ImageOps

class Demcreate:
    def __init__(
            self, text1='', text2='') -> str:

        self._text1 = text1
        self._text2 = text2

    def makeImage(
            self, file, line = None, RESULT_FILENAME='demresult.jpg', colortext='white',
            colorfill='black', fonttext='times.ttf', size2=80, size3=60
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

        while textWidth >= (width + 250) - 20:
            font_1 = ImageFont.truetype(font=fonttext, size=size2, encoding='UTF-8')
            textWidth = font_1.getsize(self._text1)[0]
            size2 -= 1

        font_2 = ImageFont.truetype(font=fonttext, size=size3, encoding='UTF-8')
        textWidth = font_2.getsize(self._text2)[0]

        while textWidth >= (width + 250) - 20:
            font_2 = ImageFont.truetype(font=fonttext, size=size3, encoding='UTF-8')
            textWidth = font_2.getsize(self._text2)[0]
            size3 -= 1

        size_1 = drawer.textsize(self._text1, font=font_1)
        drawer.text(((1280 - size_1[0]) / 2, 840), self._text1, fill=colortext, font=font_1)
        size_2 = drawer.textsize(self._text2, font=font_2)
        drawer.text(((1280 - size_2[0]) / 2, 930), self._text2, fill=colortext, font=font_2)

        if line != None:
            (width, height) = img.size
            idraw = ImageDraw.Draw(img)

            idraw.line((1000 - len(line) * 5, 817, 1008 + len(line) * 5, 817), fill=0, width=4)

            font_2 = ImageFont.truetype(font=fonttext, size=20, encoding='UTF-8')
            size_2 = idraw.textsize(line.lower(), font=font_2)
            idraw.text((((width + 729) - size_2[0]) / 2, ((height - 192) - size_2[1])), line.lower(), font=font_2)

        img.save(RESULT_FILENAME)
