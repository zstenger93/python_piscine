from ft_filter import ft_filter


def is_even(num):
    return num % 2 == 0


def test_filter():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    strings = ["apple", "banana", "cherry", "date", "elderberry"]
    mixed_types = [1, "apple", 2.5, "banana", 3, "cherry", 4.7]

    even_numbers = ft_filter(is_even, numbers)
    assert list(even_numbers) == [2, 4, 6, 8, 10], \
        "\033[31mTest 1 failed\033[0m"
    print("\033[32m       ok\033[0m")

    odd_numbers = ft_filter(lambda x: x % 2 != 0, numbers)
    assert list(odd_numbers) == [1, 3, 5, 7, 9], "\033[31mTest 2 failed\033[0m"
    print("\033[32m       ok\033[0m")

    greater_than_5 = ft_filter(lambda x: x > 5, numbers)
    assert list(greater_than_5) == [6, 7, 8, 9, 10], \
        "\033[31mTest 3 failed\033[0m"
    print("\033[32m       ok\033[0m")

    long_strings = ft_filter(lambda s: len(s) > 5, strings)
    assert list(long_strings) == ["banana", "cherry", "elderberry"], \
        "\033[31mTest 4 failed\033[0m"
    print("\033[32m       ok\033[0m")

    integers = ft_filter(lambda x: isinstance(x, int), mixed_types)
    assert list(integers) == [1, 3], "\033[31mTest 5 failed\033[0m"
    print("\033[32m       ok\033[0m")

    floats = ft_filter(lambda x: isinstance(x, float), mixed_types)
    assert list(floats) == [2.5, 4.7], "\033[31mTest 6 failed\033[0m"
    print("\033[32m       ok\033[0m")

    print("\033[32mAll tests passed\033[0m")


test_filter()
