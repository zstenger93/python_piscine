class calculator:
    """
    A calculator class for performing arithmetic operations between a vector and a scalar.
    
    Attributes:
        vector (list): The vector on which operations will be performed.
        
    Methods:
        __init__(self, vector): Initializes the calculator with the provided vector.
        
        __add__(self, scalar): Adds a scalar value to each element of the vector.
        
        __mul__(self, scalar): Multiplies each element of the vector by a scalar value.
        
        __sub__(self, scalar): Subtracts a scalar value from each element of the vector.
        
        __truediv__(self, scalar): Divides each element of the vector by a scalar value.
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
        Adds a scalar value to each element of the vector.
        
        Args:
            scalar: The scalar value to be added.
            
        Returns:
            list: The resulting vector after addition.
        """
        self.vector = [x + scalar for x in self.vector]
        return [x for x in self.vector]
    
    def __mul__(self, scalar):
        """
        Multiplies each element of the vector by a scalar value.
        
        Args:
            scalar: The scalar value to be multiplied.
            
        Returns:
            list: The resulting vector after multiplication.
        """
        self.vector = [x * scalar for x in self.vector]
        return [x for x in self.vector]
    
    def __sub__(self, scalar):
        """
        Subtracts a scalar value from each element of the vector.
        
        Args:
            scalar: The scalar value to be subtracted.
            
        Returns:
            list: The resulting vector after subtraction.
        """
        self.vector = [x - scalar for x in self.vector]
        return [x for x in self.vector]
    
    def __truediv__(self, scalar):
        """
        Divides each element of the vector by a scalar value.
        
        Args:
            scalar: The scalar value to be used for division.
            
        Returns:
            list: The resulting vector after division.
            
        Raises:
            ZeroDivisionError: If the scalar value is 0.
        """
        if scalar == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        self.vector = [x / scalar for x in self.vector]
        return [x for x in self.vector]