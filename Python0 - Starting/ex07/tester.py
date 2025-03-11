import subprocess


def run_test(cmd, expected):
    """
    Runs the given command in a subprocess and compares its stdout to the expected output.

    Parameters:
        cmd (list): Command and its arguments, e.g. ["python", "sos.py", "sos"].
        expected (str): The expected output (with no trailing newline).

    If the actual output matches the expected output, it prints that the test passed.
    Otherwise, it prints details of the failure.
    """
    try:
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )
        # Combine stdout and stderr, in case the program prints errors to stdout
        output = result.stdout.rstrip("\n")
    except Exception as e:
        output = f"Exception: {e}"

    if output == expected:
        print("Test {} PASSED".format(" ".join(cmd)))
    else:
        print("Test {} FAILED".format(" ".join(cmd)))
        print("Expected: {!r}".format(expected))
        print("Got:      {!r}".format(output))


def main():
    """
    Runs multiple tests for the sos.py Morse Code encoder.

    Test cases include:
      - Valid Morse code conversion for lowercase and uppercase letters.
      - Handling of spaces (converted to '/ ').
      - Conversion of numbers.
      - Detection of invalid characters (which should output an AssertionError).
      - Incorrect number of arguments.
    """
    tests = [
        # Valid input tests
        (["python", "sos.py", "sos"], "... --- ..."),
        (["python", "sos.py", "SOS"], "... --- ..."),
        (
            ["python", "sos.py", "Hello World"],
            ".... . .-.. .-.. --- / .-- --- .-. .-.. -..",
        ),
        (["python", "sos.py", "123"], ".---- ..--- ...--"),
        (["python", "sos.py", "HELLO"], ".... . .-.. .-.. ---"),
        (["python", "sos.py", "Test 123"], "- . ... - / .---- ..--- ...--"),
        (["python", "sos.py", "A B C"], ".- / -... / -.-."),
        # Input with trailing space (space is encoded as '/ ')
        (["python", "sos.py", "sos "], "... --- ... /"),
        # Edge case: empty string
        (["python", "sos.py", ""], ""),
        # Invalid input tests
        (
            ["python", "sos.py", "Hello$World"],
            "AssertionError: the arguments are bad",
        ),
        (["python", "sos.py", "Hi!"], "AssertionError: the arguments are bad"),
        (
            ["python", "sos.py", "Test@Test"],
            "AssertionError: the arguments are bad",
        ),
        # Incorrect number of arguments
        (["python", "sos.py"], "AssertionError: the arguments are bad"),
        (
            ["python", "sos.py", "One", "Two"],
            "AssertionError: the arguments are bad",
        ),
    ]

    for cmd, expected in tests:
        run_test(cmd, expected)


if __name__ == "__main__":
    main()
