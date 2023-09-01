from load_image import ft_load
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import sys
import os


def print_rows_firstelem(arr, int):
    """
    Print a formatted display of the first elements
    in each row of a given array.

    Parameters:
    arr (array-like): The input array containing elements to be displayed.
    int (int): An integer specifying the display format: 0 for single brackets,
               1 for triple brackets.

    Iterates through the rows of the input array and displays the first
    elements of each row in a formatted manner. The display format is
    determined by the 'int' parameter. For 'int' equal to 0, single
    brackets are used to enclose the elements, while for 'int' equal
    to 1, triple brackets are used.
    """
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
                    print("  [", row[0], "]]]", sep="")
                elif count < length - 1:
                    print("  [", row[0], "]", sep="")
            else:
                if count == length - 1:
                    print("  ", row[0], "]]", sep="")
                else:
                    print("  ", row[0], sep="")
        if count == 2:
            print("  ...")
        count += 1


def crop_image(image):
    """
    Crop the input image to form a square centered within the original image.

    Parameters:
    image (PIL.Image.Image): The input image to be cropped.

    Returns:
    PIL.Image.Image: The cropped image in the shape of a square.

    This function takes an input image and calculates the dimensions for
    cropping a square region that is centered within the original image.
    The calculated crop dimensions are applied to the input image using
    the `crop` method, and the resulting cropped image is returned.
    """
    crp_size = min(image.width, image.height)
    crp_left = (image.width - crp_size) // 2
    crp_top = (image.height - crp_size) // 2
    crp_right = crp_left + crp_size
    crp_bottom = crp_top + crp_size

    return image.crop((crp_left, crp_top, crp_right, crp_bottom))


def transpose_image(image):
    """
    Transpose the input image by swapping its width and height dimensions.

    Parameters:
    image (PIL.Image.Image): The input image to be transposed.

    Returns:
    PIL.Image.Image: The transposed image with swapped width and height
    dimensions.

    This function iterates through the pixels of the input image,
    swapping their x and y coordinates to transpose the image. A new
    image with the transposed dimensions is created, and the pixels
    are copied to the new image accordingly.
    """
    width, height = image.size
    transposed_image = Image.new("RGB", (height, width))

    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            transposed_image.putpixel((y, x), pixel)

    return transposed_image


def main():
    """
    Load, process, and display an image based on command-line arguments.

    This function serves as the main entry point of the script. It loads an
    image from the command-line argument, performs various image processing
    operations, and displays the resulting images. The script supports
    cropping, grayscale conversion, and transposing images. Errors related
    to file format and existence are caught and displayed.
    """
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
        square_crop.save("square_crop.jpg")
        ft_load("square_crop.jpg")
        print_rows_firstelem(np.array(square_crop.convert("L")), 1)

        transposed_image = transpose_image(square_crop)
        print(np.array(transposed_image.convert("L")))
        transposed_image.show()
        mirrored_image = transposed_image.transpose(Image.FLIP_LEFT_RIGHT)
        mirrored_image.show()
        print(f"New shape after Transpose: {transposed_image.size}")

        plt.imshow(transposed_image)
        plt.title("Transposed Image")
        plt.axis('on')
        plt.show()

    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()
