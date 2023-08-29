from load_image import ft_load
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import sys
import os


def print_rows_firstelem(arr, int):
    count = 0
    for row in arr:
        count += 1
    length = count
    count = 0
    for row in arr:
        if count == 0:
            if int == 1:
                print("[[[", row[0], "]", sep="")
            else:
                print("[[", row[0], sep="")
        if count > 0 and count < 3 or count > length - 4:
            if int == 1:
                if count == length - 1:
                    print("  [" ,row[0], "]]]", sep="")
                elif count < length - 1:
                    print("  [" ,row[0], "]", sep="")
            else:
                if count == length - 1:
                    print("  " ,row[0], "]]", sep="")
                else:
                    print("  " ,row[0], sep="")
        if count == 2:
            print("  ...")
        count += 1


def crop_image(image):
    crp_size = min(image.width, image.height)
    crp_left = (image.width - crp_size) // 2
    crp_top = (image.height - crp_size) // 2
    crp_right = crp_left + crp_size
    crp_bottom = crp_top + crp_size

    return image.crop((crp_left, crp_top, crp_right, crp_bottom))


def transpose_image(image):
    width, height = image.size
    transposed_image = Image.new("RGB", (height, width))

    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            transposed_image.putpixel((y, x), pixel)

    return transposed_image


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
        image.show()

        square_crop = crop_image(image)
        print_rows_firstelem(np.array(square_crop.convert("L")), 1)
        square_crop.save("square_crop.jpg")

        transposed_image = transpose_image(square_crop)
        transposed_image.show()
        print(f"New shape after Transpose: {transposed_image.size}")
        print(np.array(transposed_image.convert("L")))

        plt.imshow(transposed_image)
        plt.title("Transposed Image")
        plt.axis('on')
        plt.show()

    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()