import subprocess


def test_morse_encoder(input_text, expected_output):
    try:
        output = subprocess.check_output(["python3.10", "sos.py", input_text],
                                         stderr=subprocess.STDOUT, text=True)
        assert output.strip() == expected_output.strip()
        print(f"Test passed: Input: '{input_text}'")
        print(f"Expected: '{expected_output}', \nOutput: '{output.strip()}'\n")
    except subprocess.CalledProcessError as e:
        print(f"Test failed: Input: '{input_text}'")
        print(f"Expected: '{expected_output}', \nError: {e.output.strip()}\n")


if __name__ == "__main__":
    test_cases = [
        ("Hello World", ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."),
        ("123", ".---- ..--- ...--"),
        ("Python", ".--. -.-- - .... --- -."),
        ("%", "Unsupported character: %"),
        ("Hello?123", "Unsupported character: ?"),
        ("   ", "/ / /"),
        ("", "Usage: python3.10 morse_encoder.py <text>"),
    ]
    passed_tests = 0
    for input_text, expected_output in test_cases:
        test_morse_encoder(input_text, expected_output)
        print("\033[32m       ok\033[0m")
        passed_tests += 1
    print("\033[32m{} out of {} \
    tests passed\033[0m".format(passed_tests, len(test_cases)))
