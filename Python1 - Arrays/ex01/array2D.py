import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Takes a 2D array (list of lists) and two integer indices, prints the
    array's shape, then returns a truncated version of the array (using slicing
    along the first axis) while printing its new shape.

    Parameters:
        family (list): A 2D list (list of lists) with all rows of equal length.
        start (int): The starting index for slicing (inclusive).
        end (int): The ending index for slicing (exclusive).

    Returns:
        list: The sliced 2D list.

    Raises:
        AssertionError: If family is not a list of lists or if the rows are not
        the same size."""
    if not isinstance(family, list) or len(family) == 0:
        raise AssertionError("family must be a non-empty list")
    row_length = None
    for row in family:
        if not isinstance(row, list):
            raise AssertionError("family must be a list of lists")
        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise AssertionError("All rows must be the same size")

    arr = np.array(family)
    print("My shape is : {}".format(arr.shape))

    truncated = arr[start:end]
    print("My new shape is : {}".format(truncated.shape))

    return truncated.tolist()
