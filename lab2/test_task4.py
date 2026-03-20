from task4_digits import digit_sum


def test_digit_sum_positive() -> None:
    assert digit_sum("123") == 6


def test_digit_sum_large() -> None:
    assert digit_sum("9999") == 36


def test_digit_sum_single_digit() -> None:
    assert digit_sum("0") == 0
    assert digit_sum("7") == 7


def test_digit_sum_negative_number() -> None:
    assert digit_sum("-123") == 6


def test_digit_sum_with_decimal() -> None:
    assert digit_sum("12.34") == 10
