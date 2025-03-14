import numpy as np


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the colors of the image received.

    Each pixel value is replaced by 255 minus its value.
    Allowed operators: =, +, -, *

    Parameters:
        array (np.ndarray): The input image array with shape
        (height, width, 3).

    Returns:
        np.ndarray: The color-inverted image array."""
    result = 255 - array
    return result


def ft_red(array: np.ndarray) -> np.ndarray:
    """Keeps only the red channel of the image.

    The green and blue channels are set to 0 by multiplying with [1, 0, 0].
    Allowed operators: =, *

    Parameters:
        array (np.ndarray): The input image array with shape
        (height, width, 3).

    Returns:
        np.ndarray: The image array with only the red channel preserved."""
    mask = np.array([1, 0, 0], dtype=array.dtype)
    result = array * mask
    return result


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Keeps only the green channel of the image.

    The red and blue channels are set to 0 using subtraction.
    Allowed operators: =, -

    Parameters:
        array (np.ndarray): The input image array with shape
        (height, width, 3).

    Returns:
        np.ndarray: The image array with only the green channel preserved.
    """
    result = array.copy()
    # Set red channel to 0: x - x = 0.
    result[:, :, 0] = result[:, :, 0] - result[:, :, 0]
    # Set blue channel to 0.
    result[:, :, 2] = result[:, :, 2] - result[:, :, 2]
    return result


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Keeps only the blue channel of the image.

    The red and green channels are set to 0 using assignment.
    Allowed operator: =

    Parameters:
        array (np.ndarray): The input image array with shape
        (height, width, 3).

    Returns:
        np.ndarray: The image array with only the blue channel preserved.
    """
    result = array.copy()
    result[:, :, 0] = 0
    result[:, :, 1] = 0
    return result


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Converts the image to grayscale.

    The function computes the average of the three channels along the third
    axis. Allowed operators: =, /

    Parameters:
        array (np.ndarray): The input image array with shape
        (height, width, 3).

    Returns:
        np.ndarray: A 2D array representing the grayscale image.
    """
    # Use numpy's mean (allowed as a function call) to compute the average.
    grey = np.mean(array, axis=2)
    return grey
