from PIL import Image, ImageDraw, ImageFont
import settings


str1 = ''
str2 = ''


class demcreate:
        def __init__(self, str1: str, str2: str):
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
            frame = Image.open(settings.TEMPLATE_FILENAME)
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
            frame.save(settings.PADDINGRESULT_FILENAME)
            frame.show()
