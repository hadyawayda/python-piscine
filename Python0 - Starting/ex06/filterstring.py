import sys
from ft_filter import ft_filter


def main():
    """
    Main function that processes command-line arguments and prints words from
    the given string whose length is greater than the specified length.

    Usage:
        python filterstring.py "<string>" <length>

    Behavior:
        - Expects exactly two arguments: a string and an integer.
        - Filters the words of the given string, keeping only words longer than
        the provided integer.
        - Prints the resulting filtered list.
        - Raises AssertionError with message "the arguments are bad" if input
        validation fails.

    Raises:
        AssertionError: if arguments are missing, incorrect in number, or
        improperly formatted.
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        text = sys.argv[1]

        try:
            length = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        words = text.split()
        result = [word for word in ft_filter(lambda w: len(w) > length, words)]
        print(result)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
