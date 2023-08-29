from load_image import ft_load
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import sys
import os


def main():
    try:
        path = sys.argv[1]
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("Only JPG and JPEG formats are supported.")
        if not os.path.exists(path):
            raise AssertionError("File not found:", path)
        image = Image.open(path)
        if image is None:
            raise AssertionError("Failed to load image.")

        print(ft_load(path))
        image.show()

        zoomed_image = image.crop((400, 100, 800, 600))
        zoomed_image.save("zoomed_image.jpg")
        print(f"New shape after Transpose: {zoomed_image.size}")
        rotated_image = zoomed_image.rotate(90)
        grayscale_image = zoomed_image.convert("L")
        print(np.array(grayscale_image))

        plt.imshow(zoomed_image)
        plt.title("Zoomed Image")
        plt.axis('on')
        plt.show()
        plt.imshow(rotated_image)
        plt.title("Zoomed Image")
        plt.axis('on')
        plt.show()

    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()
