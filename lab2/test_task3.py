from task3_nested import NestedStructure, get_color, render_nested, render_page


def test_get_color_levels() -> None:
    assert get_color(0) == "red"
    assert get_color(1) == "blue"
    assert get_color(2) == "green"
    assert get_color(3) == "purple"
    assert get_color(4) == "yellow"
    assert get_color(99) == "yellow"


def test_render_nested_leaf() -> None:
    html = render_nested("hello", depth=0)
    assert "<span style='color: red'>hello</span>" == html


def test_render_nested_list() -> None:
    html = render_nested(["a", ["b"]], depth=0)
    assert "color: red" in html
    assert "<span style='color: blue'>a</span>" in html
    assert "<span style='color: green'>b</span>" in html


def test_render_nested_five_levels() -> None:
    data: NestedStructure = ["1", ["2", ["3", ["4", ["5"]]]]]
    html = render_nested(data)
    assert "color: red" in html
    assert "color: blue" in html
    assert "color: green" in html
    assert "color: purple" in html
    assert "color: yellow" in html


def test_render_page_wraps_in_html() -> None:
    page = render_page("test")
    assert "<!doctype html>" in page
    assert "</html>" in page
    assert "<span style='color: red'>test</span>" in page
