import cv2
import numpy as np


def run(src):
    """
    Blur will be made from numpy-vectorization of arrays to calculate.

    args:
        src(numpy-array): image to be blurred

    returns:
        dst(numpy-array): blurred image
    """
    src = src.astype("uint32")  # Converts to 32-bit integers, 8-bit as standard
    src = np.pad(src, 1, mode="edge")[:, :, 1:4]  # Add padding so all neighboring pixels exist along edges

    # Convolution using vectorized implementation
    dst = (src[:-2, :-2] + src[:-2, 1:-1]
           + src[:-2, 2:] + src[1:-1, :-2]
           + src[1:-1, 2:] + src[2:, :-2]
           + src[2:, 1:-1] + src[2:, 2:]
           + src[1:-1, 1:-1]) / 9

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


if __name__ == '__main__':
    """
    To measure CPU time, and generate a report, run the script from terminal:
    > blur_2.py
    Note that no image will be written to disk.
    """
    import timeit
    import os

    input_filename = os.path.join(os.pardir, "beatles.jpg")
    image = cv2.imread(input_filename)

    print("running...")
    times_blur_1 = timeit.repeat(stmt="blur_1.run(image)",
                                 setup="from blur1 import blur_1; from __main__ import image",
                                 repeat=5, number=1)
    time_blur_1 = min(times_blur_1)

    times_blur_2 = timeit.repeat(stmt="run(image)",
                          setup="from __main__ import run, image",
                          repeat=5, number=1)
    time_blur_2 = min(times_blur_2)
    print("done!")

    with open(f"report2.txt", "w+") as report:
        report.write(f"THIS IS THE REPORT FOR BLUR_2.PY.\n")
        report.write(f"Dimensions of image used for testing: {np.shape(image)}")
        report.write(f"\nTime spent with vectorized numpy array-blur: {time_blur_2:.3f} s\n")
        report.write(f"\nTime spent with manual python array-blur: {time_blur_1:.3f} s")
        report.write(f"\nThats a {(time_blur_1 - time_blur_2):.3f} s difference!\n")
