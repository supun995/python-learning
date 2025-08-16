import os
import hashlib

from PIL import Image, ImageFilter


class InvalidImageError(Exception): ...


def file_id(file_as_bytes: bytes):
    ''' Calculate the hash for the provided bytes. Used to name image files. '''
    return hashlib.sha224(file_as_bytes).hexdigest()


def save(image: Image, file_type: str, save_dir: str):
    name = file_id(image.tobytes())
    image.save(f"{os.path.join(save_dir, name)}.{file_type}")
    return f'{name}.{file_type}'


def blur(fp, radius=None):
    radius = radius or 20
    try:
        img = Image.open(fp)
    except:
        raise InvalidImageError("invalid image file.")

    return img.filter(ImageFilter.BoxBlur(radius))


def mode(fp, size=None):
    size = size or 10
    try:
        img = Image.open(fp)
    except:
        raise InvalidImageError("invalid image file.")

    return img.filter(ImageFilter.ModeFilter(size))
