from give_bmi import give_bmi, apply_limit


def almost_equal_list(list1, list2, tol=1e-6):
    """
    Checks if two lists of numbers are equal within a given tolerance.
    """
    if len(list1) != len(list2):
        return False
    return all(abs(a - b) < tol for a, b in zip(list1, list2))


def test_give_bmi_valid():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    expected = [165.3 / (2.71**2), 38.4 / (1.15**2)]
    result = give_bmi(height, weight)
    assert almost_equal_list(
        result, expected
    ), f"Expected {expected}, got {result}"
    print("test_give_bmi_valid: PASS")


def test_apply_limit_valid():
    bmi = [22.507863455018317, 29.0359168241966]
    expected = [False, True]
    result = apply_limit(bmi, 26)
    assert result == expected, f"Expected {expected}, got {result}"
    print("test_apply_limit_valid: PASS")


def test_give_bmi_different_lengths():
    try:
        give_bmi([1.7, 1.8], [70])
    except AssertionError:
        print("test_give_bmi_different_lengths: PASS")
    else:
        print("test_give_bmi_different_lengths: FAIL (no AssertionError)")


def test_give_bmi_non_list():
    try:
        give_bmi("1.7", [70])
    except AssertionError:
        print("test_give_bmi_non_list: PASS")
    else:
        print("test_give_bmi_non_list: FAIL (no AssertionError)")


def test_give_bmi_non_numeric():
    try:
        give_bmi([1.7, "a"], [70, 80])
    except AssertionError:
        print("test_give_bmi_non_numeric: PASS")
    else:
        print("test_give_bmi_non_numeric: FAIL (no AssertionError)")


def test_give_bmi_height_zero():
    try:
        give_bmi([0, 1.8], [70, 80])
    except AssertionError:
        print("test_give_bmi_height_zero: PASS")
    else:
        print("test_give_bmi_height_zero: FAIL (no AssertionError)")


def test_apply_limit_non_list():
    try:
        apply_limit("not a list", 26)
    except AssertionError:
        print("test_apply_limit_non_list: PASS")
    else:
        print("test_apply_limit_non_list: FAIL (no AssertionError)")


def test_apply_limit_non_numeric():
    try:
        apply_limit([22.5, "not numeric"], 26)
    except AssertionError:
        print("test_apply_limit_non_numeric: PASS")
    else:
        print("test_apply_limit_non_numeric: FAIL (no AssertionError)")


def test_apply_limit_non_int_limit():
    try:
        apply_limit([22.5, 29.0], "26")
    except AssertionError:
        print("test_apply_limit_non_int_limit: PASS")
    else:
        print("test_apply_limit_non_int_limit: FAIL (no AssertionError)")


def main():
    print("Testing give_bmi and apply_limit functions...")
    test_give_bmi_valid()
    test_apply_limit_valid()
    test_give_bmi_different_lengths()
    test_give_bmi_non_list()
    test_give_bmi_non_numeric()
    test_give_bmi_height_zero()
    test_apply_limit_non_list()
    test_apply_limit_non_numeric()
    test_apply_limit_non_int_limit()
    print("All tests completed.")


if __name__ == "__main__":
    main()
