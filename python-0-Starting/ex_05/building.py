import sys


def analyze_text(text):
    total_chars = len(text)
    upper_count = sum(1 for char in text if 'A' <= char <= 'Z')
    lower_count = sum(1 for char in text if 'a' <= char <= 'z')
    punctuation_characters = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    punctuation_cnt = sum(1 for char in text if char in punctuation_characters)
    space_count = sum(1 for char in text if char == ' ')
    digit_count = sum(1 for char in text if '0' <= char <= '9')

    print(f"The text contains {total_chars} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_cnt} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


def main():
    try:
        if len(sys.argv) < 2:
            print("What is the text to count?")
            exit()
        elif len(sys.argv) > 2:
            raise AssertionError("Too many arguments provided")
        text = sys.argv[1]
        analyze_text(text)
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()
