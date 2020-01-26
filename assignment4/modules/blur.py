#!/usr/bin/env python3
"""
'main'-file of this package. Here you will be able to run the three different
blurs, blur_1, blur_2, blur_3. The only argument that is needed is the
blurtype, choose between (1,2,3). If no other input is given, the blur will
use the 'beatles.jpg'-file as standard and not save the file. It will only
save the blurred image if output-name or output-path with name is given.
Remember to use '.jpg' in the end of filename

    args:
        --blurtype(int:[1,2,3]): blurtype to use.
        --input(optional:string): path of file to use blur.
        --output(optional:string): path of output-file.
"""
import argparse as ap
import cv2
from blur1 import blur_1
from blur2 import blur_2
from blur3 import blur_3


def blur_image(input_filename, output_filename, blurtype):
    """
    Blurs an image using a 3x3 averaging kernel.
    If an output filename is given, the blurred image is written to disk.
    The implementation for blurring can be specified using the 'method' argument.

    Args:
        input_filename(string): path of image to be blurred
        output_filename(string): path/name of the created blurred image
        blurtype : method used for blurring.

    Returns:
        a numpy (unsigned) integer 3D array of a blurred image
    """
    if blurtype == 1:
        blurred_image = blur_1.main(input_filename)
    elif blurtype == 2:
        blurred_image = blur_2.main(input_filename)
    elif blurtype == 3:
        blurred_image = blur_3.main(input_filename)

    if output_filename:
        cv2.imwrite(output_filename, blurred_image)

    return blurred_image


if __name__ == "__main__":
    parser = ap.ArgumentParser(formatter_class=ap.RawTextHelpFormatter)
    parser.add_argument("--blurtype", help="""select wanted blurtype '1-3'
                        1: Python (with some help from numpy-arrays for storing)
                        2: Numpy with vectorizing the arrays
                        3: Numba with the jit-decorator with the exact same code as
                        the code used in the Python-version""",
                        type=int, choices=[1, 2, 3], required=True)
    parser.add_argument("--input", default="beatles.jpg",
                        help="""path of file. If the file is in same the folder only the name is needed.""")
    parser.add_argument("--output", default=None, help="name of the output-file.")
    args = parser.parse_args()
    blur_image(args.input, args.output, args.blurtype)
