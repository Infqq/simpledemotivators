from PIL import Image, ImageDraw, ImageFont
from . import settings
import os


str1 = ''
str2 = ''
path = os.path.dirname(__file__)
path = os.path.dirname(__file__)
img_folder = os.path.join(path, "simpledemotivators")


class demcreate:
        def __init__(self, str1: str, str2: str) -> str:
                self._str1 = str1
                self._str2 = str2

        def isValidExtension(filename):
            for extension in EXTENSIONS:
                if settings.filename.endswith(extension):
                    return True
            return False


        def drawXAxisCenteredText(image, text, font, size, pos_y):
            draw = ImageDraw.Draw(image)
            textFont = ImageFont.truetype(font, size)
            textWidth = textFont.getsize(text)[0]

            while textWidth >= settings.TEMPLATE_WIDTH - settings.PADDING * 2:
                textFont = ImageFont.truetype(font, size)
                textWidth = textFont.getsize(text)[0]
                size -= 1
            
            draw.text(((settings.TEMPLATE_WIDTH - textWidth) / 2, pos_y), text, font = textFont)

        def getSizeFromArea(self, area):
            return (area[2] - area[0], area[3] - area[1])

        def makeImage(self, file):
            frame = Image.open(f"{img_folder}/{settings.TEMPLATE_FILENAME}")
            demot = Image.open(file+".jpg")
            demot = demot.resize(self.getSizeFromArea(settings.TEMPLATE_COORDS), Image.ANTIALIAS)
            frame.paste(demot, settings.TEMPLATE_COORDS)

            demcreate.drawXAxisCenteredText(frame, self._str1,
                                  settings.UPPER_FONT, settings.UPPER_SIZE,
                                  settings.UPPER_FONT_Y)
            demcreate.drawXAxisCenteredText(frame, self._str2,
                                  settings.LOWER_FONT, settings.LOWER_SIZE,
                                  settings.LOWER_FONT_Y)
            frame = frame.convert("RGB")
            frame.save(settings.RESULT_FILENAME)
            frame.show()

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
