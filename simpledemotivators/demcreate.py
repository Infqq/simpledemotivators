from PIL import Image, ImageDraw, ImageFont, ImageOps

class demcreate:
    def __init__(
            self, text1='', text2='', line = None):

        self._text1 = text1
        self._text2 = text2
        self._line = line

    def makeImage(
            self, file, RESULT_FILENAME='demresult.jpg', width = 1280, height = 1024, colortext='white',
            colorfill='black', fonttext='times.ttf', size2=80, size3=60
    ):
        # 1280 1024
        self._file = file
        """Создаем шаблон для демотиватора

        Вставляем фотографию в рамку

        """
        # 1280/1060 = 320/265 = 64/53
        # 1024/720 = 256/180 = 64/45 = 16/11
        img = Image.new('RGB', (width, height), color=colorfill)

        # по принципу пропорции уменьшаем размеры соблюдая,, пропорции. И округляем
        img_border = Image.new('RGB', (round((width * 53) / 64), round((height * 11) / 16)), color=('#000000'))
        border = ImageOps.expand(img_border, border=2, fill='#ffffff')

        # 1280/1050 = 256/210
        # 1024/720 = 256/180 = 64/45
        user_img = Image.open(file).convert("RGBA").resize((img_border.width - 5, img_border.height - 5))

        # 1024/96 = 256/24 = 64/6 = 32/3
        img.paste(border, (round((img.width -  border.width) / 2), round((img.height * 3) / 32)))

        # 1280/118 = 620/59
        img.paste(user_img, (round((img.width -  user_img.width) / 2), round((img.height * 3) / 32) + 5))

        img.save("RESULT_FILENAME.jpg")


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

        if self._line != None:
            (width, height) = img.size
            idraw = ImageDraw.Draw(img)

            idraw.line((1000 - len(self._line) * 5, 817, 1008 + len(self._line) * 5, 817), fill=0, width=4)

            font_2 = ImageFont.truetype(font=fonttext, size=20, encoding='UTF-8')
            size_2 = idraw.textsize(self._line.lower(), font=font_2)
            idraw.text((((width + 729) - size_2[0]) / 2, ((height - 192) - size_2[1])), self._line.lower(), font=font_2)

        img.save(RESULT_FILENAME)