from PIL import Image, ImageDraw, ImageFont
from simpledemotivators import settings


str1 = ''
str2 = ''


class demcreate:
        def __init__(self, text1: str, text2: str) -> str:
                self._text1 = text1
                self._text2 = text2

        def makeImage(self, file):
                img = Image.new('RGB', (1280, 1024), color=('#000000'))
                img_border = Image.new('RGB', (1060, 720), color=('#000000'))
                border = ImageOps.expand(img_border, border=2, fill='#ffffff')
                user_img = Image.open(file+'.jpg').convert("RGBA").resize((1050, 710))
                img.paste(border, (111, 96))
                img.paste(user_img, (118, 103))
                drawer = ImageDraw.Draw(img)
                font_1 = ImageFont.truetype(font='times.ttf', size=60, encoding='UTF-8')
                font_2 = ImageFont.truetype(font='arialbd.ttf', size=30, encoding='UTF-8')
                size_1 = drawer.textsize(self._text1, font=font_1)
                drawer.text(((1280 - size_1[0]) / 2, 850), self._text1, fill=(240, 230, 210), font=font_1)
                size_2 = drawer.textsize(self._text2, font=font_2)
                drawer.text(((1280 - size_2[0]) / 2, 950), self._text2, fill=(240, 230, 210), font=font_2)
                img.save(settings.RESULT_FILENAME)

class prodemoty:
        def __init__(self, str1: str, str2: str) -> str:
                self._str1 = str1
                self._str2 = str2
                
        def setimg(self, TEMPLATE_COORDS: str, TEMPLATE_WIDTH: str, TEMPLATE_HEIGHT: str, PADDING: str):
                self._TEMPLATE_COORDS = TEMPLATE_COORDS
                self._TEMPLATE_WIDTH = TEMPLATE_WIDTH
                self._TEMPLATE_HEIGHT = TEMPLATE_HEIGHT
                self._PADDING = PADDING

        def setfont(self, UPPER_FONT: str, UPPER_SIZE: str, UPPER_FONT_Y: str, LOWER_FONT: str, LOWER_SIZE: str, LOWER_FONT_Y: str):
                self._UPPER_FONT = UPPER_FONT
                self._UPPER_SIZE = UPPER_SIZE
                self._UPPER_FONT_Y = UPPER_FONT_Y
                self._LOWER_FONT = LOWER_FONT
                self._LOWER_SIZE = LOWER_SIZE
                self._LOWER_FONT_Y = LOWER_FONT_Y
                
        def isValidExtension(filename):
            for extension in EXTENSIONS:
                if settings.filename.endswith(extension):
                    return True
            return False


        def drawXAxisCenteredText(image, text, font, size, pos_y):
            draw = ImageDraw.Draw(image)
            textFont = ImageFont.truetype(font, size)
            textWidth = textFont.getsize(text)[0]

            while textWidth >= self._TEMPLATE_WIDTH - self._PADDING * 2:
                textFont = ImageFont.truetype(font, size)
                textWidth = textFont.getsize(text)[0]
                size -= 1
            
            draw.text(((self._TEMPLATE_WIDTH - textWidth) / 2, pos_y), text, font = textFont)

        def getSizeFromArea(self, area):
            return (area[2] - area[0], area[3] - area[1])

        def makeImage(self, file):
            frame = Image.open(settings.TEMPLATE_FILENAME)
            demot = Image.open(file+".jpg")
            demot = demot.resize(self.getSizeFromArea(self._TEMPLATE_COORDS), Image.ANTIALIAS)
            frame.paste(demot, self._TEMPLATE_COORDS)

            demcreate.drawXAxisCenteredText(frame, self._str1,
                                  self._UPPER_FONT, self._UPPER_SIZE,
                                  self._UPPER_FONT_Y)
            demcreate.drawXAxisCenteredText(frame, self._str2,
                                  self._LOWER_FONT, self._LOWER_SIZE,
                                  self._LOWER_FONT_Y)
            frame = frame.convert("RGB")
            frame.save(settings.RESULT_FILENAME)
            frame.show()
