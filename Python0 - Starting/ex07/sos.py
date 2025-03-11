import sys


def encode_to_morse(text: str) -> str:
    """
    Encodes the provided text into Morse Code.

    The function uses a dictionary to map each allowed character
    (alphanumeric and space) to its Morse code representation.
    If the text contains any disallowed character, it raises an
    AssertionError.

    Parameters:
        text (str): The input text to encode.

    Returns:
        str: The Morse code representation of the text, with each
        Morse symbol separated by a single space.
    """
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
    }

    for char in text:
        if not (char.isalnum() or char == " "):
            raise AssertionError("the arguments are bad")

    morse = "".join(NESTED_MORSE[char.upper()] for char in text).rstrip()
    return morse


def main():
    """
    Main function: Validates arguments, encodes the given string into Morse
    Code, and prints the result. The try/except block catches any errors
    and prints an error message.

    Usage:
        python sos.py "<string>"

    If the number of arguments is not exactly one or if the input contains
    any invalid characters, the program prints 'AssertionError: the arguments
    are bad'.
    """
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")

        text = sys.argv[1]
        print(encode_to_morse(text))
    except Exception as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
