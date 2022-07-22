from PIL import Image, ImageDraw, ImageFont, ImageOps
import requests
import os
from .image_drawer import Drawer

class Demotivator:
    def __init__(self, top_text='', bottom_text=''):
        self._top_text = top_text
        self._bottom_text = bottom_text

    def create(self, file: str, watermark=None, result_filename='demresult.jpg',
               font_color='white', fill_color='black',
               font_name='times.ttf', top_size=80, bottom_size=60,
               arrange=False, use_url=False, delete_file=False) \
            -> bool:  # Returns True if method executed successfully

        if use_url:
            p = requests.get(file)
            out = open(r'demotivator_picture.jpg', "wb")
            out.write(p.content)
            out.close()

            file = 'demotivator_picture.jpg'

        drawer = Drawer(file, fill_color, arrange)

        drawer.draw_centered_text(self._top_text, top_size, font_name, font_color, 840)
        drawer.draw_centered_text(self._bottom_text, bottom_size, font_name, font_color, 930)

        drawer._img.save(result_filename)

        if delete_file:
            os.remove(file)

        return True
