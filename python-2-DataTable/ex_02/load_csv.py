import pandas as pd


def load(path: str):
    """
    Load a CSV dataset from the specified path and return it as a pandas
    DataFrame.

    Parameters:
    path (str): The path to the CSV file to be loaded.

    Returns:
    pd.DataFrame or None: The loaded dataset as a pandas DataFrame, or
    None if there was an error.

    This function loads a CSV dataset from the given path using the
    pandas library.
    It prints the dimensions of the loaded dataset and returns the
    dataset as a DataFrame.
    If there is an error (e.g., bad path, bad format), None is returned.
    """
    try:
        dataset = pd.read_csv(path)
        print(f"Loading dataset of dimensions {dataset.shape}")
        return dataset
    except Exception as error:
        print("Error:", error)
        return None
