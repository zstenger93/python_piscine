import sys

def main():
	 """
    The program accepts two arguments:
    - A string (S): The input text containing words separated by spaces.
    - An integer (N): The threshold length for filtering words.
    
    The function processes the input text and filters out words whose length is greater
    than the specified integer N. It then prints the list of filtered words.
    
    If the number of arguments is different from 2, or if the type of any argument is wrong,
    the program prints an AssertionError.
    """
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