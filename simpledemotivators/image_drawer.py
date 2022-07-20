from PIL import ImageDraw


class Drawer:
    def __init__(self, image):
        self._drawer = ImageDraw.Draw(image)

    def write_text(self, text_location, text, fill_color, text_font):
        self._drawer.text(text_location, text, fill=fill_color, font=text_font)
    
    def get_text_size(self, text, text_font):
        return self._drawer.textsize(text, font=text_font)