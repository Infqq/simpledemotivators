from PIL import Image, ImageDraw, ImageFont, ImageOps


class Image_manager:
    def __init__(self, arrange, fill_color, filename):
        self._arrange = arrange
        self._fill_color = fill_color
        self._filename = filename

    def create_template(self):
        if not self._arrange:
            demotivator_image = Image.new('RGB', (1280, 1024), color=self._fill_color)
            image_border = Image.new('RGB', (1060, 720), color='#000000')
            demotivator_border = ImageOps.expand(image_border, border=2, fill='#ffffff')

            user_image = Image.open(self._filename).convert("RGBA").resize((1050, 710))
            (self._width, self._height) = user_image.size

            demotivator_image.paste(demotivator_border, (111, 96))
            demotivator_image.paste(user_image, (118, 103))

        return (demotivator_image, self._width, self._height)

    def get_optimal_font_size(self, font_name, optimal_size, text):
        font = ImageFont.truetype(font=font_name, size=optimal_size, encoding='UTF-8')
        text_width = font.getsize(text)[0]

        while text_width >= (self._width + 250) - 20:
            font = ImageFont.truetype(font=font_name, size=optimal_size, encoding='UTF-8')
            text_width = font.getsize(text)[0]
            optimal_size -= 1

        return font