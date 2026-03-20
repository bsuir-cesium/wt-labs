"""Generate an HTML table with rows fading from white to black."""

import sys


def row_color(row: int, total: int) -> str:
    """Return a hex color interpolated from white (#ffffff) to black (#000000)."""
    if total <= 1:
        return "#ffffff"
    gray = 255 - round(255 * row / (total - 1))
    return f"#{gray:02x}{gray:02x}{gray:02x}"


def generate_gradient_table(rows: int) -> str:
    lines = [
        "<!doctype html>",
        "<html>",
        "<head><meta charset='utf-8'><title>Gradient Table</title></head>",
        "<body>",
        "<table border='1' style='border-collapse: collapse; width: 300px;'>",
    ]
    for i in range(rows):
        bg = row_color(i, rows)
        text_color = "#ffffff" if i >= rows // 2 else "#000000"
        lines.append(
            f"  <tr style='background: {bg}; color: {text_color};'>"
            f"<td style='padding: 4px;'>{i + 1}</td></tr>"
        )
    lines.append("</table>")
    lines.append("</body>")
    lines.append("</html>")
    return "\n".join(lines)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <number_of_rows>", file=sys.stderr)
        sys.exit(1)
    print(generate_gradient_table(int(sys.argv[1])))
