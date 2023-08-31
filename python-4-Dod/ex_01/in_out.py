def square(x: int | float) -> int | float:
    """
    Calculate the square of a given number.

    Parameters:
    x (int | float): The number for which the square needs to be calculated.

    Returns:
    int | float: The square of the input number.
    """
    return x * x


def pow(x: int | float) -> int | float:
    """
    Calculate the exponentiation of a given number to itself.

    Parameters:
    x (int | float): The base number for the exponentiation.

    Returns:
    int | float: The result of raising the input number to the power of itself.
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Create a counter function that performs calculations and
    updates its input value.

    This function takes a number and a function as input.
    It returns a callable object that acts as a counter function.
    Each time the counter function is called, it calculates the result of the
    provided function applied to the input number, updates the input number
    with the result, and returns the calculated result.
    Additionally, it keeps track of the number of times it's been called.

    Parameters:
    x (int | float): The initial input value.
    function (function): The function to be applied for calculations.

    Returns:
    object: A callable object (counter function) that
    calculates and updates the value.
    """
    def inner() -> float:
        """
        Execute the provided function, update the value, and return the result.

        This inner function performs the following steps:
        1. Execute the provided function using the current input value.
        2. Update the input value with the result of the calculation.
        3. Increment the internal counter to keep track of the number of calls.
        4. Return the result of the calculation.

        Nonlocal:
        Used to modify a variable in the nearest enclosing scope that's
        not the global scope. It allows you to work with variables from
        a parent (enclosing) function's scope.

        Returns:
        float: The result of the calculation performed by the provided function
        """
        nonlocal x
        result = function(x)
        x = result
        return result
    return inner
