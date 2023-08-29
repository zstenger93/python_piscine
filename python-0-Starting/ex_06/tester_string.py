from ft_filter import ft_filter


def test_filter():
    test_cases = [
        ("Hello World", 4, ["Hello", "World"]),
        ("Python is fun", 2, ["Python", "fun"]),
        ("", 0, []),
        ("abc def ghi", 1, ["abc", "def", "ghi"]),
        ("One Two Three", 4, ["Three"]),
        ("Zero Nani Three", 5, []),
    ]
    passed_tests = 0
    for text, n, expected_result in test_cases:
        filtered_words = \
            list(ft_filter(lambda word: len(word) > n, text.split()))
        if filtered_words == expected_result:
            passed_tests += 1
            print("\033[32m       ok\033[0m")
        else:
            print("\033[31mTest failed for input '{}', {}: Expected {}, \
            got {}\033[0m".format(text, n, expected_result, filtered_words))
    print("\033[32m{} out of {} \
    tests passed\033[0m".format(passed_tests, len(test_cases)))


if __name__ == "__main__":
    test_filter()
