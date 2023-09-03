import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Truncate a 2D array based on the provided start and end arguments.

    Args:
        family (list): 2D array to be truncated.
        start (int): Index to start truncation from.
        end (int): Index to end truncation at.

    Returns:
        list: Truncated version of the array.
    My shape:
        Calculates the shape of the original family array
        using NumPy's np.array() function and then retrieves its
        shape using the .shape attribute. The shape of a 2D array is
        a tuple representing the number of rows and columns.
        This line prints the shape of the original array.
    New shape:
        Calculates the shape of the truncated array.
        It first creates a NumPy array from the family list,
        then slices it from the start index to the end+1 index.
        The .shape attribute is used to retrieve the shape of the
        truncated array, which represents the number of rows and
        columns after the truncation.
    """
    try:
        if not isinstance(family, list) \
                or not isinstance(start, int) or not isinstance(end, int):
            raise AssertionError("Input must be a list and 2 integer.")
        if not all(len(item) == len(family[0]) for item in family):
            raise AssertionError("Input list with different sizes.")
        print(f"My shape is : {np.array(family).shape}")
        print(f"My new shape is : {np.array(family)[start:end+1].shape}")
        return np.array(family)[start:end].tolist()
    except AssertionError as error:
        print("\033[31m", AssertionError.__name__ + ":", error, "\033[0m")
        return ""
