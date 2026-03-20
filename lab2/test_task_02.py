from task_02 import generate_table


def test_table_rows_are_numbered() -> None:
    html = generate_table(5)
    for i in range(1, 6):
        assert f"<td>{i}</td>" in html


def test_table_zero_rows() -> None:
    html = generate_table(0)
    assert "<tr><td>" not in html
    assert "<table" in html


def test_table_is_valid_html() -> None:
    html = generate_table(1)
    assert html.startswith("<!doctype html>")
    assert "</html>" in html
