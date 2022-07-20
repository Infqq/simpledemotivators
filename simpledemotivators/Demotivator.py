from re import template
from PIL import ImageDraw, ImageFont
import requests
import os
from .image_drawer import Drawer
from .image_manager import Image_manager

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

        img_manager = Image_manager(arrange, fill_color, file)
        template = img_manager.create_template()
        demotivator_image = template[0]

        drawer = Drawer(demotivator_image)
        width, height = template[1], template[2]

        font_1 = img_manager.get_optimal_font_size(font_name, top_size, self._top_text)
        font_2 = img_manager.get_optimal_font_size(font_name, bottom_size, self._bottom_text)

        size_1 = drawer.get_text_size(self._top_text, font_1)
        size_2 = drawer.get_text_size(self._bottom_text, font_2)
        
        if arrange:
            drawer.write_text((((width + 250) - size_1[0]) / 2, ((height + 190) - size_1[1])), 
                                self._top_text, font_color, font_1)
        else:
            drawer.write_text(((1280 - size_1[0]) / 2, 840), self._top_text, font_color, font_1)
            drawer.write_text(((1280 - size_2[0]) / 2, 930), self._bottom_text, font_color, font_2)

        # Thats i not refactored!
        if watermark is not None:
            (width, height) = demotivator_image.size
            idraw = ImageDraw.Draw(demotivator_image)

            idraw.line((1000 - len(watermark) * 5, 817, 1008 + len(watermark) * 5, 817), fill=0, width=4)

            font_2 = ImageFont.truetype(font=font_name, size=20, encoding='UTF-8')
            size_2 = idraw.textsize(watermark.lower(), font=font_2)
            idraw.text((((width + 729) - size_2[0]) / 2, ((height - 192) - size_2[1])),
                       watermark.lower(), font=font_2)

        demotivator_image.save(result_filename)

        if delete_file:
            os.remove(file)

        return True
