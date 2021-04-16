from PIL import Image

class Compression():
    def jaskal(self, file, compression = 4, RESULT_FILENAME = 'test.jpg'):
        (wight, height) = Image.open(file).size
        image = Image.open(file).convert('RGB').resize((round(wight / compression), round(height / compression)))

        image.save(RESULT_FILENAME)
        return "successful"

    def pixelate(self, file, compression = 4, RESULT_FILENAME = 'test.jpg'):
        file = Image.open(file).convert('RGB')

        file = file.resize((file.size[0] // compression, file.size[1] // compression), Image.NEAREST)
        file = file.resize((file.size[0] * compression, file.size[1] * compression), Image.NEAREST)

        file.save(RESULT_FILENAME)
        return "successful"