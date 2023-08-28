def ft_filter(function, iterable):
	"""
	Returns an iterator over the items of iterable for which function(item) is True.
    :param function:
    :param iterable:"""
    return (item for item in iterable if function(item))


def main():
	print(ft_filter.__doc__)
	print(ft_filter.__doc__)


if __name__ == "__main__":
    main()