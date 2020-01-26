from numba import jit
import numpy as np
import cv2


def run(src):
    """
    Function to run manual blur with python-only (numpy to store array)
    calculations on a three-dimensional numpy-array with three for-loops.
    Loops representing depth, rows, and columns. The function convolution()
    is being run with the decorator '@jit' from numba.

    args:
        src (numpy-array): image to be blurred

    returns:
        dst (numpy-array): blurred image
    """
    src = src.astype("uint32")  # Converts to 32-bit integers, 8-bit as standard
    dst = np.zeros(src.shape)  # Creates empty placeholder for blurred image
    src = np.pad(src, 1, mode="edge")[:, :, 1:4]  # Adds padding so all neighboring pixels exist along edges
    #Manual convolution
    @jit
    def convolution(dst,src):
        """
        Calculations of blur with standard python with numpy-arrays, but
        using the decorator '@jit'.

        args:
            dst (numpy-array): copy of original array of image to be blurred.
            src (numpy-array): original array of image.
        """
        for h in range(1, dst.shape[0] + 1):
            for w in range(1, dst.shape[1] + 1):
                for c in range(dst.shape[2]):
                    dst[h-1,w-1,c] = (src[h,w,c] + src[h-1,w,c] + src[h+1,w,c]
                                  + src[h,w-1,c] + src[h,w+1,c]
                                  + src[h-1,w-1,c] + src[h-1,w+1,c]
                                  + src[h+1,w-1,c] + src[h+1,w+1,c])/9

    convolution(dst,src)
    dst = dst.astype("uint8") #If floats after convolution, converts to integers
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


def subsectBlur(src,x,y,wi,he):
    """
    Function to blur a subsection of an image

    Args:
        src : a numpy integer 3D array of the image to be blurred
        x, y (int): start coordinates for rectangle (x, y)
        w, h (int): width and height to blur

    returns:
        dst (numpy-array): blurred image
    """
    src = src.astype("uint32") #Converts to 32-bit integers, 8-bit as standard
    #Make copy of image
    dst = np.copy(src)
    @jit
    def convolution(dst,src):
        """
        Calculations of blur with standard python with numpy-arrays, but
        using the decorator '@jit'.

        args:
            dst,(numpy-array): copy of original array of image to be blurred.
            src,(numpy-array): original array of image.
        """
        for h in range(y,he+y):
            for w in range(x,wi+x):
                for c in range(dst.shape[2]):
                    dst[h,w,c] = (src[h,w,c] + src[h-1,w,c] + src[h+1,w,c]
                                    + src[h,w-1,c] + src[h,w+1,c]
                                    + src[h-1,w-1,c] + src[h-1,w+1,c]
                                    + src[h+1,w-1,c] + src[h+1,w+1,c])/9

    convolution(dst,src)
    dst = dst.astype("uint8") #If floats after convolution, converts to integers
    return dst


if __name__ == '__main__':
    """
    To measure CPU time, and generate a report, run the script from terminal:
    > blur_3.py
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

    times_blur_3 = timeit.repeat(stmt="run(image)",
                          setup="from __main__ import run, image",
                          repeat=5, number=1)
    time_blur_3 = min(times_blur_3)
    print("done!")

    with open(f"report3.txt", "w+") as report:
        report.write(f"THIS IS THE REPORT FOR BLUR_3.PY.\n")
        report.write(f"Dimensions of image used for testing: {np.shape(image)}")
        report.write(f"\nTime spent with jit numpy array-blur: {time_blur_3:.3f} s\n")
        report.write(f"\nTime spent with manual python array-blur: {time_blur_1:.3f} s")
        report.write(f"\nThats a {(time_blur_1 - time_blur_3):.3f} s difference!\n")
        report.write("""As a disadvantage for the use of numba instead of numpy
        would be a tiny difference in performance where numpy gets ahead,
        ca 0.05s difference after multiple runs. However a great advantage of
        the use of numba would be the ease of use. The decorator is something
        close to being 'magical'. But then again, this could lead to some weird
        error-messages if anything goes wrong. This is something I experienced
        when I tried to use jit on a function which included cv2-operations.
        This made jit fail, and therefore I had to exclude the cv2-operations
        from the targeted function.""")