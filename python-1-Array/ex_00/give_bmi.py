def give_bmi(
        height: list[int | float], weight: list[int | float]
        ) -> list[int | float]:
    """
    Calculate BMI values based on given heights and weights.

    Args:
        height (list[int | float]): List of heights in meters.
        weight (list[int | float]): List of weights in kilograms.

    Returns:
        list[int | float]: List of calculated BMI values.
    """
    try:
        # if not isinstance(height, list) or not isinstance(weight, list):
        #     raise TypeError("Height and weight must be provided as lists.")
        if len(height) != len(weight):
            raise ValueError(
                "Lists of height and weight must have the same length.")
        bmi_values = []
        for h, w in zip(height, weight):
            if not isinstance(h, (int, float)) \
                    or not isinstance(w, (int, float)):
                raise TypeError(
                    "Height and weight must be integers or floats.")
            if h <= 0 or w <= 0:
                raise ValueError("Height and weight values must be positive.")
            bmi = w / (h ** 2)
            bmi_values.append(bmi)
        return bmi_values
    except Exception as error:
        print("An error occurred:", error)
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Determine whether BMI values are above a given limit.

    Args:
        bmi (list[int | float]): List of BMI values.
        limit (int): Limit to compare BMI values against.

    Returns:
        list[bool]: List of booleans indicating whether
        each BMI value is above the limit.
    """
    try:
        if not isinstance(limit, float) and not isinstance(limit, int):
            raise TypeError("Limit must be provided as int or float.")
        above_limit = []
        for value in bmi:
            if not isinstance(value, (int, float)):
                raise TypeError("BMI values must be integers or floats.")
            above_limit.append(value > limit)
        return above_limit
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
