import matplotlib.pyplot as plt
from load_image import ft_load


def manual_transpose(matrix: list[list[int]]) -> list[list[int]]:
    """
    Manually transposes a 2D list (matrix).

    Parameters:
        matrix (list[list[int]]): The original 2D list.

    Returns:
        list[list[int]]: The transposed 2D list.
    """
    rows = len(matrix)
    cols = len(matrix[0])
    # Create an empty transposed matrix with dimensions (cols x rows)
    transposed = [[None for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    return transposed


def main():
    """
    Loads "animal.jpeg", crops a centered 400×400 region in grayscale,
    prints its shape and pixel data, manually transposes the matrix,
    prints the new shape and data, and displays the transposed image.
    """
    img = ft_load("animal.jpeg")
    if img is None:
        return
    # Manually transpose the 2D image array
    transposed = manual_transpose(img)
    new_rows, new_cols = len(transposed), len(transposed[0])
    print(f"New shape after Transpose: ({new_rows}, {new_cols})")
    print(transposed)

    # Display the transposed image using matplotlib
    plt.imshow(transposed, cmap="gray")
    plt.title("Transposed Image")
    plt.xlabel("X axis (pixels)")
    plt.ylabel("Y axis (pixels)")
    plt.show()


if __name__ == "__main__":
    main()
