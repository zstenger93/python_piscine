def callLimit(limit: int):
    """
    Takes an integer 'limit' as input and returns a decorator that restricts
    the number of times a decorated function can be called.
    When the decorated function is called, its execution is allowed only up
    to the specified 'limit'. If the function is called more times than the
    limit, a 'AssertionError' is raised.

    Parameters:
    limit (int): Number of times the function can be called.

    Returns:
    function: A decorator that restricts the number of times
    a function can be called.
    """

    count = 0

    def callLimiter(function):
        """
        Decorator:
        This inner function is used to wrap around the target function.
        It tracks the number of times the target function is called
        using the 'count' variable. If the function has been called
        less than or equal to the specified 'limit', it allows the
        function's execution.
        If the limit is exceeded, it raises a 'ValueError'.

        Parameters:
        function (function): The function to be decorated.

        Returns:
        function: The wrapped function that enforces the call limit.
        """

        def limit_function(*args, **kwds):
            """
            Wrapper:
            Used as a wrapper around the decorated function.
            It increments the 'count' variable each time the wrapped
            function is called. If the 'count' is within the limit,
            the wrapped function is executed. Otherwise, an 'AssertionError'
            is raised indicating that the function has been called too
            many times.

            Returns:
            Any: The result of executing the decorated function, if
            the call limit is not exceeded.

            Raises:
            AssertionError: If the call limit has been exceeded.
            """
            try:
                nonlocal count
                count += 1
                if count <= limit:
                    return function(*args, **kwds)
                else:
                    raise AssertionError(f"{function} call too many times")
            except AssertionError as error:
                print("Error:", error)
        return limit_function

    return callLimiter
