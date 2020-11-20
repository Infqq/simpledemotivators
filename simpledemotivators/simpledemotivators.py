import PIL
from PIL import Image, ImageDraw, ImageFont


str1 = ''
str2 = ''

TEMPLATE_FILENAME = 'template.jpg'
EXTENSIONS = ['.jpg', '.png']

RESULT_FILENAME = 'demresult.jpg'

UPPER_FONT = 'times.ttf'
UPPER_SIZE = 45
UPPER_FONT_Y = 390
LOWER_FONT = 'arialbd.ttf'
LOWER_SIZE = 14
LOWER_FONT_Y = 450

TEMPLATE_WIDTH = 574
TEMPLATE_HEIGHT = 522
TEMPLATE_COORDS = (75, 45, 499, 373)
PADDING = 10

class demcreate:
        def __init__(self, str1: str, str2: str):
                self._str1 = str1
                self._str2 = str2

        def isValidExtension(filename):
            for extension in EXTENSIONS:
                if filename.endswith(extension):
                    return True
            return False


        def drawXAxisCenteredText(image, text, font, size, pos_y):
            draw = ImageDraw.Draw(image)
            textFont = ImageFont.truetype(font, size)
            textWidth = textFont.getsize(text)[0]

            while textWidth >= TEMPLATE_WIDTH - PADDING * 2:
                textFont = ImageFont.truetype(font, size)
                textWidth = textFont.getsize(text)[0]
                size -= 1
            
            draw.text(((TEMPLATE_WIDTH - textWidth) / 2, pos_y), text, font = textFont)

        def getSizeFromArea(self, area):
            return (area[2] - area[0], area[3] - area[1])

        def makeImage(self, file):
            frame = Image.open(TEMPLATE_FILENAME)
            demot = Image.open(file+".jpg")
            demot = demot.resize(self.getSizeFromArea(TEMPLATE_COORDS), Image.ANTIALIAS)
            frame.paste(demot, TEMPLATE_COORDS)

            demcreate.drawXAxisCenteredText(frame, self._str1,
                                  UPPER_FONT, UPPER_SIZE,
                                  UPPER_FONT_Y)
            demcreate.drawXAxisCenteredText(frame, self._str2,
                                  LOWER_FONT, LOWER_SIZE,
                                  LOWER_FONT_Y)
            frame = frame.convert("RGB")
            frame.save(RESULT_FILENAME)
            frame.show()
