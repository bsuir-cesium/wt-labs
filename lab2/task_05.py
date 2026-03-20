"""Find the longest word(s) among CLI arguments."""

import sys


def find_longest(words: list[str]) -> list[str]:
    if not words:
        return []
    max_len = max(len(w) for w in words)
    return [w for w in words if len(w) == max_len]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <word1> <word2> ...", file=sys.stderr)
        sys.exit(1)
    result = find_longest(sys.argv[1:])
    print(", ".join(result))
