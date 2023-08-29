import numpy as np
from PIL import Image


def ft_invert(array):
    """
    Inverts the color of the image received.
    """
    image = 255 - array
    Image.fromarray(image).show()


def ft_red(array):
    """
    Keeps only the red color channel of the image.
    """
    red_channel = array[:, :, 0]
    image = np.stack([red_channel, np.zeros_like(red_channel),
                      np.zeros_like(red_channel)], axis=2)
    Image.fromarray(image).show()


def ft_green(array):
    """
    Keeps only the green color channel of the image.
    """
    green_channel = array[:, :, 1]
    image = np.stack([np.zeros_like(green_channel), green_channel,
                      np.zeros_like(green_channel)], axis=2)
    Image.fromarray(image).show()


def ft_blue(array):
    """
    Keeps only the blue color channel of the image.
    """
    blue_channel = array[:, :, 2]
    image = np.stack([np.zeros_like(blue_channel),
                      np.zeros_like(blue_channel), blue_channel], axis=2)
    Image.fromarray(image).show()


def ft_grey(array):
    """
    Converts the image to grayscale.
    """
    image = np.mean(array, axis=2, keepdims=True).astype(array.dtype)
    Image.fromarray(image.squeeze(), mode='L').show()
