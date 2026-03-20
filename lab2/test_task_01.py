from task_01 import classify, main


def test_classify_int() -> None:
    assert classify("42") == "int"
    assert classify("-7") == "int"
    assert classify("0") == "int"


def test_classify_float() -> None:
    assert classify("3.14") == "float"
    assert classify("-0.5") == "float"
    assert classify("1e10") == "float"


def test_classify_str() -> None:
    assert classify("hello") == "str"
    assert classify("") == "str"
    assert classify("12abc") == "str"


def test_main_mixed() -> None:
    result = main(["10", "3.14", "hello"])
    assert result == [("10", "int"), ("3.14", "float"), ("hello", "str")]


def test_main_empty() -> None:
    assert main([]) == []
