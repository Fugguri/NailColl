from PIL import Image, ImageDraw
from io import BytesIO


def create(rgb):
    rgb_code = tuple(map(int, rgb.split(' ')))
    image = Image.new('RGB', (250, 250), rgb_code)
    byte_io = BytesIO()
    image.save(byte_io, 'PNG')
    image = byte_io.getvalue()
    byte_io.close()
    return image
