import numpy as np
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, "modules"))
from blur1 import blur_1
from blur2 import blur_2
from blur3 import blur_3


def test_of_blurs_size():
    """
    Test of the different blurs to see if the maximum value of each blurred
    array has decreased after blurring compared to the original array.
    Generates an 3d-numpy-array containing randomly generated numbers in the
    span of (0,255), with a dimension of (480,640,3)
    """
    np.random.seed(1)
    array_3d = np.random.randint(0, 256, size=(480, 640, 3))  # draws from “half-open” interval [0, 256)
    assert np.amax(array_3d) > np.amax(blur_1.run(array_3d))
    assert np.amax(array_3d) > np.amax(blur_2.run(array_3d))
    assert np.amax(array_3d) > np.amax(blur_3.run(array_3d))


def test_of_blurs_mean():
    """
    Test of the different blurs to check that calculations are correct.
    Generates an 3d-numpy-array containing randomly generated numbers in the
    span of (0,255), with a dimension of (50, 50, 3))
    """
    np.random.seed(1)
    test = np.random.randint(0, 256, size=(50, 50, 3))  # draws from “half-open” interval [0, 256)

    blurred_pixel = (test[39, 39, 0] + test[40, 39, 0] + test[41, 39, 0] +
                     test[39, 40, 0] + test[40, 40, 0] + test[41, 40, 0] +
                     test[39, 41, 0] + test[40, 41, 0] + test[41, 41, 0]) / 9

    test_blur_1 = blur_1.run(test)
    test_blur_2 = blur_2.run(test)
    test_blur_3 = blur_3.run(test)

    assert int(blurred_pixel) == int(test_blur_1[40, 40, 0])
    assert int(blurred_pixel) == int(test_blur_2[40, 40, 0])
    assert int(blurred_pixel) == int(test_blur_3[40, 40, 0])
