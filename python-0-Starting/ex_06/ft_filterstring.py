import sys

def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError("Exactly two arguments (string and integer) are required.")

        text = sys.argv[1]
        n = int(sys.argv[2])

        if not isinstance(text, str) or not isinstance(n, int):
            raise AssertionError("Invalid argument types.")

        filter_words = lambda text, n: [word for word in text.split() if len(word) > n]
        filtered_words = filter_words(text, n)
        
        print(filtered_words)

    except ValueError as error:
        print("ValueError:", error)
    except AssertionError as error:
        print("AssertionError:", error)

if __name__ == "__main__":
    main()