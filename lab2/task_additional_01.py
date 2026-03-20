#!/usr/bin/env python3
"""Determine data types of GET query parameters (CGI: reads QUERY_STRING)."""

import os
import sys
from urllib.parse import parse_qs


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


def classify_query(query_string: str) -> list[tuple[str, str, str]]:
    """Parse query string and classify each parameter's value.

    Returns list of (name, value, type) tuples.
    """
    params = parse_qs(query_string, keep_blank_values=True)
    result: list[tuple[str, str, str]] = []
    for name, values in params.items():
        for val in values:
            result.append((name, val, classify(val)))
    return result


def run_cgi() -> None:
    query = os.environ.get("QUERY_STRING", "")
    classified = classify_query(query)

    rows = "".join(
        f"  <tr><td>{name}</td><td>{value}</td><td>{kind}</td></tr>\n"
        for name, value, kind in classified
    )
    body = (
        "<!doctype html>\n<html>\n"
        "<head><meta charset='utf-8'><title>GET Params</title></head>\n"
        "<body>\n"
        "<table border='1'>\n"
        "  <tr><th>Parameter</th><th>Value</th><th>Type</th></tr>\n"
        f"{rows}"
        "</table>\n"
        "</body>\n</html>"
    )
    encoded = body.encode("utf-8")
    sys.stdout.write("Content-Type: text/html; charset=utf-8\r\n")
    sys.stdout.write(f"Content-Length: {len(encoded)}\r\n\r\n")
    sys.stdout.flush()
    sys.stdout.buffer.write(encoded)
    sys.stdout.buffer.flush()


if __name__ == "__main__":
    run_cgi()
