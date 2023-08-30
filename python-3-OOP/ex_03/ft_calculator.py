class calculator:
    """
    A calculator class for performing arithmetic operations between
    a vector and a scalar.

    Attributes:
        vector (list): The vector on which operations will be performed.

    Methods:
        __init__(self, vector): Init the calculator with the provided vector.

        __add__(self, scalar): + a scalar value to each element of the vec.

        __mul__(self, scalar): * each element of the vector by a scalar value.

        __sub__(self, scalar): - a scalar value from each element of the vector

        __truediv__(self, scalar): / each element of the vector by a scalar val
    """

    def __init__(self, vector):
        """
        Initializes the calculator with the provided vector.

        Args:
            vector (list): The vector on which operations will be performed.
        """
        self.vector = vector

    def __add__(self, scalar):
        """
        Returns:
            The resulting vector after addition.
        """
        self.vector = [x + scalar for x in self.vector]
        print(self.vector)
        return [x for x in self.vector]

    def __mul__(self, scalar):
        """
        Returns:
            The resulting vector after multiplication.
        """
        self.vector = [x * scalar for x in self.vector]
        print(self.vector)
        return [x for x in self.vector]

    def __sub__(self, scalar):
        """
        Returns:
            The resulting vector after subtraction.
        """
        self.vector = [x - scalar for x in self.vector]
        print(self.vector)
        return [x for x in self.vector]

    def __truediv__(self, scalar):
        """
        Returns:
            The resulting vector after division.

        Raises:
            ZeroDivisionError: If the scalar value is 0.
        """
        if scalar == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        self.vector = [x / scalar for x in self.vector]
        print(self.vector)
        return [x for x in self.vector]
