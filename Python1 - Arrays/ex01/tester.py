from array2D import slice_me


def run_test(
    test_name, func, args, expected_value=None, expected_exception=None
):
    """
    Helper to run a test case.

    Parameters:
      - test_name (str): A description of the test.
      - func (callable): The function to test.
      - args (tuple): The arguments to pass to the function.
      - expected_value: The expected return value (if no exception is expected).
      - expected_exception (Exception type): The type of exception expected.
    """
    try:
        result = func(*args)
        if expected_exception:
            print(
                f"{test_name}: FAIL (expected exception {expected_exception.__name__}, got result {result})"
            )
        else:
            if result == expected_value:
                print(f"{test_name}: PASS")
            else:
                print(
                    f"{test_name}: FAIL (expected {expected_value}, got {result})"
                )
    except Exception as e:
        if expected_exception and isinstance(e, expected_exception):
            print(f"{test_name}: PASS")
        else:
            print(f"{test_name}: FAIL (unexpected exception: {e})")


def main():
    print("Running tests for slice_me...\n")

    # Test 1: Valid input; slice (0,2)
    family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
    expected1 = [[1.80, 78.4], [2.15, 102.7]]
    run_test(
        "Test 1 (slice 0 to 2)",
        slice_me,
        (family, 0, 2),
        expected_value=expected1,
    )

    # Test 2: Valid input; slice (1,-2)
    expected2 = [[2.15, 102.7]]
    run_test(
        "Test 2 (slice 1 to -2)",
        slice_me,
        (family, 1, -2),
        expected_value=expected2,
    )

    # Test 3: Valid input; slice indices that produce an empty array (e.g., beyond range)
    expected3 = []
    run_test(
        "Test 3 (slice 10 to 20, returns empty)",
        slice_me,
        (family, 10, 20),
        expected_value=expected3,
    )

    # Test 4: Error: family is not a list (string instead)
    run_test(
        "Test 4 (family not a list)",
        slice_me,
        ("not a list", 0, 2),
        expected_exception=AssertionError,
    )

    # Test 5: Error: family is an empty list
    run_test(
        "Test 5 (empty family list)",
        slice_me,
        ([], 0, 2),
        expected_exception=AssertionError,
    )

    # Test 6: Error: family is a list but elements are not lists
    run_test(
        "Test 6 (elements not lists)",
        slice_me,
        ([1, 2, 3], 0, 2),
        expected_exception=AssertionError,
    )

    # Test 7: Error: family is a list of lists with different sizes
    family_inconsistent = [[1, 2], [3, 4, 5]]
    run_test(
        "Test 7 (inconsistent row sizes)",
        slice_me,
        (family_inconsistent, 0, 1),
        expected_exception=AssertionError,
    )

    print("\nAll tests completed.")


if __name__ == "__main__":
    main()
