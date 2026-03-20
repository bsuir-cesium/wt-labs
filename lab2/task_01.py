"""Determine the data type of each CLI argument: int, float, or str."""

import sys


def classify(value: str) -> str:
    """Return 'int', 'float', or 'str' for a given string."""
    try:
        int(value)
        return "int"
    except ValueError:
        pass
    try:
        float(value)
        return "float"
    except ValueError:
        return "str"


def main(args: list[str]) -> list[tuple[str, str]]:
    return [(arg, classify(arg)) for arg in args]


if __name__ == "__main__":
    for value, kind in main(sys.argv[1:]):
        print(f"{value} -> {kind}")
