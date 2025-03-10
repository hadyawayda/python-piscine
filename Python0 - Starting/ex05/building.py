import sys
import string

def count_characters(text: str) -> dict:
    punctuation_chars = string.punctuation + "-"
    return {
        "upper": sum(1 for c in text if c.isupper()),
        "lower": sum(1 for c in text if c.islower()),
        "punctuation": sum(1 for c in text if c in punctuation_chars),
        "spaces": sum(1 for c in text if c.isspace()),
        "digits": sum(1 for c in text if c.isdigit())
    }

def main():
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
