import cv2
import numpy as np


def run(src):
    """
    Function to run manual blur with python-only (numpy to store array)
    calculations on a three-dimensional numpy-array with three for-loops.
    Loops representing depth, rows, and columns.

    args:
        src (numpy-array): image to be blurred

    returns:
        dst (numpy-array): blurred image
    """
    src = src.astype("uint32")  # Converts to 32-bit integers, 8-bit as standard
    dst = np.zeros(src.shape)  # Creates empty placeholder for blurred image
    src = np.pad(src, 1, mode="edge")[:, :, 1:4]  # Adds padding so all neighboring pixels exist along edges

    # Manual convolution
    for h in range(1, dst.shape[0] + 1):
        for w in range(1, dst.shape[1] + 1):
            for c in range(dst.shape[2]):
                dst[h-1,w-1,c] = (src[h,w,c] + src[h-1,w,c] + src[h+1,w,c]
                                  + src[h,w-1,c] + src[h,w+1,c]
                                  + src[h-1,w-1,c] + src[h-1,w+1,c]
                                  + src[h+1,w-1,c] + src[h+1,w+1,c])/9

    dst = dst.astype("uint8")  # If floats after convolution, converts to integers
    return dst


def main(input_filename):
    """
    Passing image array to the run-function to blur the image.

    args:
        input_filename(string): path of image to be blurred

    returns:
        blurred_image (numpy-array): The blurred image
    """
    image = cv2.imread(input_filename)
    blurred_image = run(image)
    return blurred_image
