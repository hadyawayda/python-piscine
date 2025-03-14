import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def main():
    """Loads the image "animal.jpeg", prints its original information, performs
    azoom operation by cropping a centered 400x400 region, converts that region
    to grayscale (1 channel), prints the new shape and pixel content, and then
    displays the zoomed image with scale labels on the x and y axes."""
    try:
        # Load the image using ft_load
        img_arr = ft_load("animal.jpeg")
        print(img_arr)
        if img_arr is None:
            return

        # Get original image dimensions (height, width, channels)
        height, width, channels = img_arr.shape

        # Determine the starting indices for a centered 400x400 crop
        crop_size = 400
        if height < crop_size or width < crop_size:
            raise ValueError(
                "Image is smaller than the cropping size of 400x400 pixels."
            )
        start_y = (height - crop_size) // 2
        start_x = (width - crop_size) // 2

        # Crop the center of the image
        cropped = img_arr[
            start_y: start_y + crop_size, start_x: start_x + crop_size
        ]

        # Convert the cropped region to grayscale using
        # the standard luminance formula:
        # Gray = 0.299 * R + 0.587 * G + 0.114 * B
        gray = np.dot(cropped[..., :3], [0.299, 0.587, 0.114])
        # Expand dims if you prefer a shape (400, 400, 1)
        gray_expanded = np.expand_dims(gray, axis=2)

        print("New shape after slicing:", gray_expanded.shape)
        print(gray_expanded)

        # Display the zoomed grayscale image with axis scales
        plt.imshow(gray, cmap="gray")
        plt.xlabel("X axis (pixels)")
        plt.ylabel("Y axis (pixels)")
        plt.title("Zoomed Image (Center Crop)")
        plt.colorbar()  # Optionally display the intensity scale
        plt.show()

    except Exception as e:
        print("Error in zooming process:", e)


if __name__ == "__main__":
    main()
