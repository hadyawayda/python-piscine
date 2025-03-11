import matplotlib.pyplot as plt
from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey


def display_image(array, title="Image", cmap=None):
    """Displays the image array using matplotlib."""
    plt.figure()
    plt.imshow(array, cmap=cmap)
    plt.title(title)
    plt.axis("off")
    plt.show()


def main():
    # Load the image
    img = ft_load("landscape.jpg")
    print(img)
    if img is None:
        return

    print("Original image shape:", img.shape)
    display_image(img, "Original Image")

    # Invert filter
    inverted = ft_invert(img)
    print("Inverted image shape:", inverted.shape)
    display_image(inverted, "Inverted Image")

    # Red filter
    red_img = ft_red(img)
    print("Red image shape:", red_img.shape)
    display_image(red_img, "Red Channel Image")

    # Green filter
    green_img = ft_green(img)
    print("Green image shape:", green_img.shape)
    display_image(green_img, "Green Channel Image")

    # Blue filter
    blue_img = ft_blue(img)
    print("Blue image shape:", blue_img.shape)
    display_image(blue_img, "Blue Channel Image")

    # Grey filter (grayscale)
    grey_img = ft_grey(img)
    print("Grey image shape:", grey_img.shape)
    display_image(grey_img, "Grayscale Image", cmap="gray")

    # Print the documentation for ft_invert (as expected)
    print("ft_invert docstring:")
    print(ft_invert.__doc__)


if __name__ == "__main__":
    main()
