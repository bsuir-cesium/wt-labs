from task_additional_01 import classify, classify_query


def test_classify_int() -> None:
    assert classify("42") == "int"
    assert classify("-7") == "int"


def test_classify_float() -> None:
    assert classify("3.14") == "float"
    assert classify("1e10") == "float"


def test_classify_str() -> None:
    assert classify("hello") == "str"
    assert classify("") == "str"


def test_classify_query_mixed() -> None:
    result = classify_query("a=10&b=3.14&c=hello")
    by_name = {name: (val, kind) for name, val, kind in result}
    assert by_name["a"] == ("10", "int")
    assert by_name["b"] == ("3.14", "float")
    assert by_name["c"] == ("hello", "str")


def test_classify_query_empty() -> None:
    assert classify_query("") == []


def test_classify_query_multiple_values() -> None:
    result = classify_query("x=1&x=abc")
    assert len(result) == 2
    assert result[0] == ("x", "1", "int")
    assert result[1] == ("x", "abc", "str")
