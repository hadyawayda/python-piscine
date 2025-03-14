from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """Loads an image from the given path, prints its shape, and returns its
    pixel content as a NumPy array in RGB format.

    Supported formats: JPG and JPEG.

    Parameters:
        path (str): The file path to the image.

    Returns:
        np.ndarray: The image's pixel data in RGB format.

    Error Handling:
        If the file is not found, the format is unsupported, or another error
        occurs, a clear error message is printed and None is returned."""
    try:
        if not path.lower().endswith((".jpg", ".jpeg")):
            raise ValueError(
                "Unsupported file format. Only JPG and JPEG are supported."
            )

        img = Image.open(path)

        if img.mode != "RGB":
            img = img.convert("RGB")

        arr = np.array(img)

        print(f"The shape of image is: {arr.shape}")

        return arr
    except Exception as e:
        print(f"Error loading image: {e}")
        return None
