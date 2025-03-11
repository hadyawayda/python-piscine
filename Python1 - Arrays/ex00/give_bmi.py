def give_bmi(
    height: list[int | float], weight: list[int | float]
) -> list[float]:
    """
    Calculates BMI values given lists of heights (in meters) and weights (in
    kilograms).

    The BMI is computed using the formula: BMI = weight / (height ** 2).

    Parameters:
        height (list[int | float]): A list of heights (in meters).
        weight (list[int | float]): A list of weights (in kilograms).

    Returns:
        list[float]: A list of BMI values corresponding to each pair of height
        and weight.

    Raises:
        AssertionError: If height and weight are not both lists, have different
        lengths, or contain non-numeric (non-int/non-float) values.
    """
    if not isinstance(height, list) or not isinstance(weight, list):
        raise AssertionError("height and weight must be lists")
    if len(height) != len(weight):
        raise AssertionError("height and weight must be of the same size")

    bmi_list = []
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise AssertionError(
                "Elements of height and weight must be int or float"
            )
        if h == 0:
            raise AssertionError("Height cannot be zero")
        bmi_list.append(w / (h * h))
    return bmi_list


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Applies a limit to a list of BMI values, returning a list of booleans
    indicating whether each BMI is above the specified limit.

    Parameters:
        bmi (list[int | float]): A list of BMI values.
        limit (int): The BMI threshold.

    Returns:
        list[bool]: A list of booleans, where each element is True if the
                corresponding BMI is greater than the limit, otherwise False.

    Raises:
        AssertionError: If bmi is not a list or its elements are not numeric,
                        or if limit is not an integer.
    """
    if not isinstance(bmi, list):
        raise AssertionError("bmi must be a list")
    if not all(isinstance(x, (int, float)) for x in bmi):
        raise AssertionError("Elements of bmi must be int or float")
    if not isinstance(limit, int):
        raise AssertionError("limit must be an integer")

    return [x > limit for x in bmi]
