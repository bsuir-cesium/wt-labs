"""Calculate the sum of digits of a number passed via CLI."""

import sys


def digit_sum(number: str) -> int:
    return sum(int(ch) for ch in number if ch.isdigit())


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <number>", file=sys.stderr)
        sys.exit(1)
    print(digit_sum(sys.argv[1]))
