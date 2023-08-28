def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object\n
Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if function:
        return (item for item in iterable if function(item))
    return (item for item in iterable if item)
