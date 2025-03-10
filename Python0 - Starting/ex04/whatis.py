import sys

if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            sys.exit()
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        arg = sys.argv[1]
        if not arg.lstrip("-").isdigit():
            raise AssertionError("argument is not an integer")
        number = int(arg)
        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except AssertionError as e:
        print(f"AssertionError: {e}")
