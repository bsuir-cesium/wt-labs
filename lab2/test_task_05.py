from task_05 import find_longest


def test_single_longest() -> None:
    assert find_longest(["cat", "elephant", "dog"]) == ["elephant"]


def test_multiple_longest() -> None:
    result = find_longest(["abc", "def", "gh"])
    assert result == ["abc", "def"]


def test_all_same_length() -> None:
    result = find_longest(["aa", "bb", "cc"])
    assert result == ["aa", "bb", "cc"]


def test_single_word() -> None:
    assert find_longest(["hello"]) == ["hello"]


def test_empty_list() -> None:
    assert find_longest([]) == []
