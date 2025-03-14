from PIL import Image
import numpy as np


def ft_load(path: str):
    """Loads the image from the provided path, crops a centered 400x400 region,
    converts it to grayscale (a single channel), prints its shape and pixel
    data, and returns the image as a 2D list of pixel values.

    Supported formats: JPG and JPEG.

    Parameters:
        path (str): The file path to the image.

    Returns:
        list[list[int]]: A 2D list (400x400) of pixel values (0-255) in
        grayscale. If an error occurs, prints a clear error message and returns
        None."""
    try:
        if not path.lower().endswith((".jpg", ".jpeg")):
            raise ValueError(
                "Unsupported file format. Only JPG and JPEG are supported."
            )
        img = Image.open(path)
        # Convert to grayscale (mode 'L' gives one channel)
        if img.mode != "L":
            img = img.convert("L")
        width, height = img.size
        crop_size = 400
        if width < crop_size or height < crop_size:
            raise ValueError("Image is smaller than 400x400.")
        # Compute centered crop coordinates
        left = (width - crop_size) // 2
        top = (height - crop_size) // 2
        right = left + crop_size
        bottom = top + crop_size
        cropped = img.crop((left, top, right, bottom))
        # Convert cropped image to numpy array
        arr = np.array(cropped)
        print(f"The shape of image is: {arr.shape}")
        print(arr)
        return arr.tolist()
    except Exception as e:
        print("Error loading image:", e)
        return None
