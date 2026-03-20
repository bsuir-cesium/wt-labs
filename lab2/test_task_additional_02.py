from task_additional_02 import generate_gradient_table, row_color


def test_row_color_first_is_white() -> None:
    assert row_color(0, 10) == "#ffffff"


def test_row_color_last_is_black() -> None:
    assert row_color(9, 10) == "#000000"


def test_row_color_single_row() -> None:
    assert row_color(0, 1) == "#ffffff"


def test_row_color_two_rows() -> None:
    assert row_color(0, 2) == "#ffffff"
    assert row_color(1, 2) == "#000000"


def test_gradient_table_row_count() -> None:
    html = generate_gradient_table(5)
    assert html.count("<tr") == 5


def test_gradient_table_contains_first_and_last_color() -> None:
    html = generate_gradient_table(3)
    assert "background: #ffffff" in html
    assert "background: #000000" in html


def test_gradient_table_zero_rows() -> None:
    html = generate_gradient_table(0)
    assert "<tr" not in html
