#!/usr/bin/env python
from complex import Complex

def test_add_complex():
    """Test function testing the add (+) fuction of the class Complex.

    The function is using multiple asserts to test different scenarios
    that the 'add' function inside of the class Complex could be facing.
    In this test, we go through different number-values (int), both
    non-zero and zero, both positive and negative values. The returned
    value gets compared with a given value, calculated in advance
    'hardcoded answer'. The Complex class also includes a comparison
    function, which is being used in this test.

    Args:
        No arguments given/taken

    Raises:
        AssertionError: If the assert-tests fail. If the comparison-tests
        fail.

    """
    assert Complex(1,1) + Complex(1,1) == Complex(2,2)
    assert Complex(0,5) + Complex(5,0) == Complex(5,5)
    assert Complex(3,6) + Complex(0,0) == Complex(3,6)
    assert Complex(-10,-10) + Complex(5,2) == Complex(-5,-8)

def test_sub_complex():
    """Test function testing the subtraction (-) function of the class
    Complex.

    The function is using multiple asserts to test different scenarios
    that the 'subtraction' function inside of the class Complex could
    be facing. In this test, we go through different number-values (int),
    both non-zero and zero, both positive and negative values. The
    returned value gets compared with a given value, calculated in
    advance 'hardcoded answer'. The Complex class also includes a compar-
    ison function, which is being used in this test.

    Args:
        No arguments given/taken

    Raises:
        AssertionError: If the assert-tests fail. If the comparison-tests
        fail.

    """
    assert Complex(1,0) - Complex(0,0) == Complex(1,0)
    assert Complex(9,7) - Complex(6,8) == Complex(3,-1)
    assert Complex(0,0) - Complex(0,0) == Complex(0,0)
    assert Complex(-2,8) - Complex(4,-5) == Complex(-6,13)

def test_mul_complex():
    """Test function testing the multiplication (*) function of the class
    Complex.

    The function is using multiple asserts to test different scenarios
    that the 'multiplication' function inside of the class Complex could
    be facing. In this test, we go through different number-values (int),
    both non-zero and zero, both positive and negative values. The
    returned value gets compared with a given value, calculated in
    advance 'hardcoded answer'. The Complex class also includes a compar-
    ison function, which is being used in this test.

    Args:
        No arguments given/taken

    Raises:
        AssertionError: If the assert-tests fail. If the comparison-tests
        fail.

    """
    assert Complex(1,0) * Complex(0,0) == Complex(0,0)
    assert Complex(9,7) * Complex(6,8) == Complex(-2,114)
    assert Complex(0,0) * Complex(0,0) == Complex(0,0)
    assert Complex(-2,8) * Complex(4,-5) == Complex(32,42)

def test_con_and_mod_complex():
    """Test function testing both conjugate and modulus function of the class
    Complex.

    The function is using multiple asserts to test different scenarios
    that the 'subtraction' function inside of the class Complex could
    be facing. In this test, we go through different number-values (int),
    both non-zero and zero, both positive and negative values. The
    returned value gets compared with a given value, calculated in
    advance 'hardcoded answer'. The Complex class also includes a compar-
    ison function, which is being used in this test.

    Args:
        No arguments given/taken

    Raises:
        AssertionError: If the assert-tests fail. If the comparison-tests
        fail.

    """
    assert Complex(0,-0).conjugate() == Complex(0,0)
    assert Complex(-13,4).conjugate() == Complex(-13,-4)
    assert Complex(0,-15).conjugate() == Complex(0,15)
    assert Complex(-4,-4).conjugate() == Complex(-4,4)
    assert Complex(0,0).modulus() == 0
    assert Complex(7,-0).modulus() == 7
    assert Complex(-7,0).modulus() == 7
    assert Complex(6,8).modulus() == 10

def test_eq_complex():
    """Test function testing the comparison (==) fuction of the class
    Complex.

    The function is using multiple asserts to test different scenarios
    that the 'comparison' function inside of the class Complex could
    be facing. In this test, we go through different number-values (int),
    both non-zero and zero, both positive and negative values. The
    returned value gets compared with a given value, calculated in
    advance 'hardcoded answer'.

    Args:
        No arguments given/taken

    Raises:
        AssertionError: If the assert-tests fail. If the comparison-tests
        fail.

    """
    assert Complex(1,1) == Complex(1,1)
    assert Complex(-1,0) == Complex(-1,0)
    assert Complex(0,-0) == Complex(0,-0)
    assert Complex(22,32) == Complex(22,32)

def test_radd_complex():
    """Test function testing the __radd__ function of the class
    Complex, if the first argument does not support an argument of
    the Complex class.

    The function is using multiple asserts to test different scenarios
    that the 'add' function inside of the class Complex could
    be facing. In this test, we go through different number-values (int),
    both non-zero and zero, both positive and negative values. The
    returned value gets compared with a given value, calculated in
    advance 'hardcoded answer'. The Complex class also includes a compar-
    ison function, which is being used in this test. Both integers and
    python's integrated complex number-object is being used in the
    testing. Both as the first and as the second argument given to the
    addition-function

    Args:
        No arguments given/taken

    Raises:
        AssertionError: If the assert-tests fail. If the comparison-tests
        fail.

    """
    assert Complex(1,1) + (1+2j) == Complex(2,3)
    assert Complex(-14,1) + (0+8j) == Complex(-14,9)
    assert 4 + Complex(6,-7) == Complex(10,-7)
    assert Complex(2,3) + (2+2j) == Complex(4,5)
    assert Complex (5,7) + 4 == Complex(9,7)
    assert Complex (5,7) + 0 == Complex(5,7)
    assert Complex (5,7) + -4 == Complex(1,7)
    assert (3+7j) + Complex(5,-3) == Complex(8,4)
    assert (0-0j) + Complex(1,-1) == Complex(1,-1)
    assert (9-4j) + Complex(0,0) == Complex(9,-4)

def test_rsub_complex():
    """Test function testing the __rsub__ function of the class
    Complex, if the first argument does not support an argument of
    the Complex class.

    The function is using multiple asserts to test different scenarios
    that the 'subtraction' function inside of the class Complex could
    be facing. In this test, we go through different number-values (int),
    both non-zero and zero, both positive and negative values. The
    returned value gets compared with a given value, calculated in
    advance 'hardcoded answer'. The Complex class also includes a compar-
    ison function, which is being used in this test. Both integers and
    python's integrated complex number-object is being used in the
    testing. Both as the first and as the second argument given to the
    subtraction-function

    Args:
        No arguments given/taken

    Raises:
        AssertionError: If the assert-tests fail. If the comparison-tests
        fail.

    """
    assert Complex(1,0) - (0+0j) == Complex(1,0)
    assert Complex(9,7) - (6-8j) == Complex(3,15)
    assert Complex(0,0) - (0+0j) == Complex(0,0)
    assert Complex(3,2) - 1 == Complex(2,2)
    assert -7 - Complex(-2,8) == Complex(-5,-8)
    assert +-7 - Complex(-2,8) == Complex(-5,-8)
    assert (2+6j) - Complex(1,-3) == Complex(1,9)
    assert (0+1j) - Complex(1,0) == Complex(-1,1)
    assert (2-9j) - Complex(0,-6) == Complex(2,-3)


def test_rmul_complex():
    """Test function testing the __rmul__ function of the class
    Complex, if the first argument does not support an argument of
    the Complex class.

    The function is using multiple asserts to test different scenarios
    that the 'multiplication' function inside of the class Complex could
    be facing. In this test, we go through different number-values (int),
    both non-zero and zero, both positive and negative values. The
    returned value gets compared with a given value, calculated in
    advance 'hardcoded answer'. The Complex class also includes a compar-
    ison function, which is being used in this test. Both integers and
    python's integrated complex number-object is being used in the
    testing. Both as the first and as the second argument given to the
    multiplication-function

    Args:
        No arguments given/taken

    Raises:
        AssertionError: If the assert-tests fail. If the comparison-tests
        fail.

    """
    assert Complex(0,5) * (5+5j) == Complex(-25,25)
    assert Complex(-3,6) * (4-0j) == Complex(-12,24)
    assert Complex(7,-2) * (0+0j) == Complex(0,0)
    assert Complex(7,-2) * (-7-2j) == Complex(-53,0)
    assert (2+6j) * Complex(1,-3) == Complex(20,0)
    assert (0+5j) * Complex(0,-6) == Complex(30,0)
    assert (2-3j) * Complex(2,3) == Complex(13,0)
    assert (1+3j) * Complex(2,3) == Complex(-7,9)

def test_multiple_useage():
    """Test function testing the different functions of the class
    Complex. Using multiple functions in one test-line, pythons
    complex number-object and integers.

    The function is using multiple asserts to test different scenarios
    that the functions inside of the class Complex could be facing.
    In this test, we go through different number-values (int),
    both non-zero and zero, both positive and negative values. The
    returned value gets compared with a given value, calculated in
    advance 'hardcoded answer'. The Complex class also includes a compar-
    ison function, which is being used in this test. Both integers and
    python's integrated complex number-object is being used in the
    testing. Both as the first and as the second argument given to the
    addition-function.

    Args:
        No arguments given/taken

    Raises:
        AssertionError: If the assert-tests fail. If the comparison-tests
        fail.

    """
    assert 4 * Complex(3,4) - 2 == Complex(10,16)
    assert 0 * Complex(4,-4) - 9 == Complex(-9,0)
    assert Complex(4,4) * Complex(4,-4) - (2+8j) == Complex(30,-8)
    assert (3-7j) + (2+8j) - 4 + Complex(3,8) * (7-2j) == Complex(38,51)
