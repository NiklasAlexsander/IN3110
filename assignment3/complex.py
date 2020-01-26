from math import sqrt

class Complex:
    """Class to represent a custom complex number, not pythons verison.

    The class contains functions and variables to support operations
    on our custom complex number. The complex number will be an
    object which can be modified.

    __init__ takes two arguments to create a Complex object. The
    arguments represents the real number and imaginary number of
    an complex number respectively.

    Args:
        a (int): Integer representing the real number of an complex
                number.
        b (int): Integer representing the imaginary number of an
                complex number.

    Attributes:
        a (int): Integer representing the real number of an complex
                number.
        b (int): Integer representing the imaginary number of an
                complex number.
        complexStr (string): A complex number formatted as a readable
                string. Used with comparison.

    """

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.complexStr = f'{a}+{b}i'



    # Assignment 3.3

    def conjugate(self):
        """Function to conjugate a complex number.

        Takes the complex number-object that the function got cast upon,
        using the real and imaginary numbers stored and conjugate.

        Returns:
            A new Complex-object with values representing the complex number
            the function is cast upon, only conjugated.

        """
        return Complex(self.a,self.b *-1)

    def modulus(self):
        """Function to take modulus of a complex number.

        Takes the complex number-object that the function got cast upon,
        using the real and imaginary numbers stored and modulus. The
        modulus function will use the sqrt function from math to
        calculate the square-root in the right manner.

        Returns:
            A new Complex-object with values representing the complex number
                the function is cast upon, only modulus.

        """
        return sqrt((self.a**2)+(self.b**2))

    def __add__(self, add):
        """Function to do the operation of addition on two complex
        numbers.

        The addition function will use the object it is cast upon and take
        and arg which it will retrive the values it need to perform its
        task. It will check if the arg is an instance of complex or int,
        so the values gets extracted in the correct manner.

        Args:
            add (:obj:complex, 'int', optional): Expecting either be an object
                of pythons complex number or an int as argument.

        Attributes:
            newx (int): temporary variable to store the new calculated
                real number.
            newy (int): temporary variable to store the new calculated
                imaginary number.

        Returns:
            A new Complex-object with values representing the
                complex number gotten from applying the addition-formula on
                the given complex number-objects.

        """
        newx=0
        newy=0
        if (isinstance(add, (complex, int))):
            newx = self.a + int(add.real)
            newy = self.b + int(add.imag)
        else:
            newx = self.a + add.a
            newy = self.b + add.b
        return Complex(newx, newy)

    def __sub__(self, sub):
        """Function to do the operation of subtraction on two complex
        numbers.

        The subtraction function will use the object it is cast upon and take
        and arg which it will retrive the values it need to perform its
        task. It will check if the arg is an instance of complex or int,
        so the values gets extracted in the correct manner.

        Args:
            sub (:obj:complex, 'int', optional): Expecting either be an
                object of pythons complex number or an int as argument.

        Attributes:
            newx (int): temporary variable to store the new calculated
                real number.
            newy (int): temporary variable to store the new calculated
                imaginary number.

        Returns:
            A new Complex-object with values representing the complex number
            gotten from applying the subtraction-formula on the given complex 
            number-objects.

        """
        newx=0
        newy=0
        if (isinstance(sub, (complex, int))):
            newx = self.a - int(sub.real)
            newy = self.b - int(sub.imag)
        else:
            newx = self.a - sub.a
            newy = self.b - sub.b
        return Complex(newx, newy)

    def __mul__(self, mul):
        """Function to do the operation of multiplication on two complex
        numbers.

        The multiplication function will use the object it is cast upon and take
        and arg which it will retrive the values it need to perform its
        task. It will check if the arg is an instance of complex or int,
        so the values gets extracted in the correct manner.

        Args:
            mul (:obj:complex, 'int', optional): Expecting either be an object
                of pythons complex number or an int as argument.

        Attributes:
            newx (int): temporary variable to store the new calculated
                real number.
            newy (int): temporary variable to store the new calculated
                imaginary number.

        Returns:
            (:obj:Complex): A new Complex-object with values representing
                the complex number gotten from applying the
                multiplication-formula on the given complex number-objects.

        """
        newx=0
        newy=0
        if(isinstance(mul, (complex, int))):
            newx = ((self.a*int(mul.real)) - (self.b*int(mul.imag)))
            newy = +((self.a*int(mul.imag)) + (int(mul.real)*self.b))
        else:
            newx = ((self.a*mul.a) - (self.b*mul.b))
            newy = +((self.a*mul.b) + (mul.a*self.b))
        return Complex(newx, newy)

    def __eq__(self, eq):
        """Function to do the operation of equality of two complex numbers.

        The equality function will use the object it is cast upon and take
        and arg which it will retrive the values it need to perform its
        task. The function will check the string representing the complex
        number of the object the function it is cast upon, and compare it
        to the equivalent string value in the arg-object.

        Args:
            eq (:obj:Complex): Complex object as argument.

        Returns:
            Boolean value, True if successful, False otherwise

        """
        return self.complexStr == eq.complexStr

    # Assignment 3.4
    def __radd__(self, radd):
        """Function to take the __radd__ check if __add__ does not support
        the Complex-object as argument.

        __radd__ will 'kick in' if the object the add (+) is casted upon does not
        support usage of objects by the class of Complex. This could happen
        if you try to add an integer with an Complex-object in this order,
        '4 + Complex(2,3)'. The integer-class does not have support for the
        class Complex, therefore python will try to cast __radd__ if it
        exists. __radd__ function will then "flip" the arguments around the
        addition sign (+), and run the arithmetic, while casting the real
        and imaginary number of the argument 'radd' as integers, in case of
        float value.

        Returns:
            (obj:Complex): The object given from the __add__ function.

        """
        return self + Complex(int(radd.real),int(radd.imag))


    def __rsub__(self, rsub):
        """Function to take the __rsub__ check if __sub__ does not support
        the Complex-object as argument.

        __rsub__ will 'kick in' if the object the add (-) is casted upon does not
        support usage of objects by the class of Complex. This could happen
        if you try to perform subtraction on an integer with an Complex-object
        in this order, '4 - Complex(2,3)'. The integer-class does not have
        support for the class Complex, therefore python will try to cast
        __rsub__ if it exists. __rsub__ function will then "flip" the arguments
        around the subtraction sign (-), and run the arithmetic, while casting the
        real and imaginary number of the argument 'radd' as integers, in case of
        float value.

        Returns:
            (obj:Complex): The object given from the __sub__ function.

        """
        return Complex(int(rsub.real),int(rsub.imag)) - self

    def __rmul__(self, rmul):
        """Function to take the __rsub__ check if __mul__ does not support
        the Complex-object as argument.

        __rmul__ will 'kick in' if the object the multiplication (*) is casted
        upon does not support usage of objects by the class of Complex. This
        could happen if you try to performe multiplication on an integer with
        an Complex-object in this order, '4 * Complex(2,3)'. The integer-class
        does not have support for the class Complex, therefore python will try
        to cast __rmul__ if it exists. __rmul__ function will then "flip" the
        arguments around the multiplication sign (*), and run the arithmetic,
        while casting the real and imaginary number of the argument 'rmul' as
        integers, in case of float value.

        Returns:
            (obj:Complex): The object given from the __mul__ function.

        """
        return self * Complex(int(rmul.real),int(rmul.imag))


    # Optional, possibly useful methods

    # Allows you to write `-a`
    def __neg__(self):
        pass

    # Make the `complex` function turn this into Python's version of a complex number
    def __complex__(self):
        pass
