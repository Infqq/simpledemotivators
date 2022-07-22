from PIL import Image, ImageDraw, ImageFont, ImageOps

class Drawer:
    def __init__(self, filename, fill_color, arrange):
        self._img = Image.new('RGB', (1280, 1024), color=fill_color)
        img_border = Image.new('RGB', (1060, 720), color='#000000')
        border = ImageOps.expand(img_border, border=2, fill='#ffffff')
        self._img.paste(border, (111, 96))

        user_img = Image.open(filename).convert("RGBA").resize((1050, 710))
        self._img.paste(user_img, (118, 103))

        (self._width, self._height) = user_img.size

        self._arrange = arrange
        self._drawer = ImageDraw.Draw(self._img)

    def draw_centered_text(self, text, font_size, font_name, font_color, size_height):
        if self._arrange:
            pass
        else:
            font = ImageFont.truetype(font=font_name, size=font_size, encoding='UTF-8')
            text_width = font.getsize(text)[0]

            while text_width >= (self._width + 250) - 20:
                font = ImageFont.truetype(font=font_name, size=font_size, encoding='UTF-8')
                text_width = font.getsize(text)[0]
                font_size -= 1

            size = self._drawer.textsize(text, font=font)

            self._drawer.text(((1280 - size[0]) / 2, size_height), text, fill=font_color, font=font)