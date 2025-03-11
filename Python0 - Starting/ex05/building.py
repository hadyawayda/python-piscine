import sys


def count_characters(text: str) -> dict:
    """
    Counts different types of characters within the given text.

    Parameters:
        text (str): The input text to analyze.

    Returns:
        dict: A dictionary containing the counts of the following character
        types:
            - upper (int): Count of uppercase letters (A-Z).
            - lower (int): Count of lowercase letters.
            - punctuation marks include standard punctuation plus '-'.
            - spaces (including regular spaces and carriage returns/newlines).
            - digits (0-9).
    """

    punctuation_chars = """!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"""

    return {
        "upper": sum(1 for c in text if c.isupper()),
        "lower": sum(1 for c in text if c.islower()),
        "punctuation": sum(1 for c in text if c in punctuation_chars),
        "spaces": sum(1 for c in text if c.isspace()),
        "digits": sum(1 for c in text if c.isdigit()),
    }


def main():
    """
    Main function to handle command-line arguments, read user input if needed,
    count characters, and display the character statistics.

    Behavior:
        - If exactly one argument is provided, analyzes that argument.
        - If no argument is provided, prompts the user to input text.
        - If more than one argument is provided, raises an AssertionError.
    """
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")

        if len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            print("What is the text to count?")
            text = sys.stdin.readline()

        counts = count_characters(text)
        total_chars = len(text)

        print(f"The text contains {total_chars} characters:")
        print(f"{counts['upper']} upper letters")
        print(f"{counts['lower']} lower letters")
        print(f"{counts['punctuation']} punctuation marks")
        print(f"{counts['spaces']} spaces")
        print(f"{counts['digits']} digits")

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
