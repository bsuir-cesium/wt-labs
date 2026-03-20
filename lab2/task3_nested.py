"""Render a nested structure as colored HTML (depth >= 5 levels)."""

LEVEL_COLORS = ["red", "blue", "green", "purple", "yellow"]

NestedStructure = str | list["NestedStructure"]


def get_color(depth: int) -> str:
    if depth < len(LEVEL_COLORS) - 1:
        return LEVEL_COLORS[depth]
    return LEVEL_COLORS[-1]


def render_nested(data: NestedStructure, depth: int = 0) -> str:
    color = get_color(depth)
    if isinstance(data, str):
        return f"<span style='color: {color}'>{data}</span>"
    items = "\n".join(f"<li>{render_nested(item, depth + 1)}</li>" for item in data)
    return f"<ul style='color: {color}'>\n{items}\n</ul>"


def render_page(data: NestedStructure) -> str:
    return (
        "<!doctype html>\n<html>\n"
        "<head><meta charset='utf-8'><title>Nested</title></head>\n"
        f"<body>\n{render_nested(data)}\n</body>\n</html>"
    )


SAMPLE_DATA: NestedStructure = [
    "Level 1 - A",
    [
        "Level 2 - B",
        [
            "Level 3 - C",
            [
                "Level 4 - D",
                ["Level 5 - E", ["Level 6 - F"]],
            ],
        ],
    ],
    "Level 1 - G",
]

if __name__ == "__main__":
    print(render_page(SAMPLE_DATA))
