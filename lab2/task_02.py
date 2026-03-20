"""Generate an HTML table with a given number of rows."""

import sys


def generate_table(rows: int) -> str:
    lines = [
        "<!doctype html>",
        "<html>",
        "<head><meta charset='utf-8'><title>Table</title></head>",
        "<body>",
        "<table border='1'>",
        "  <tr><th>Row number</th></tr>",
    ]
    for i in range(1, rows + 1):
        lines.append(f"  <tr><td>{i}</td></tr>")
    lines.append("</table>")
    lines.append("</body>")
    lines.append("</html>")
    return "\n".join(lines)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <number_of_rows>", file=sys.stderr)
        sys.exit(1)
    print(generate_table(int(sys.argv[1])))
