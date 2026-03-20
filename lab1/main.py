#!/usr/bin/env python3
import platform
import sys


def get_os_info() -> tuple[str, str, str]:
    return platform.system(), platform.release(), platform.version()


def render_html(system: str, release: str, version: str) -> str:
    return f"""<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>CGI OS Info</title>
</head>
<body style="font-family: Arial, sans-serif;">
  <h1>Python CGI works!</h1>
  <p><b>Operating System:</b> {system} {release}</p>
  <p><b>Version:</b> {version}</p>
</body>
</html>
"""


def run_cgi() -> None:
    system, release, version = get_os_info()
    body = render_html(system, release, version).encode("utf-8")
    sys.stdout.write("Content-Type: text/html; charset=utf-8\r\n")
    sys.stdout.write(f"Content-Length: {len(body)}\r\n\r\n")
    sys.stdout.flush()
    sys.stdout.buffer.write(body)
    sys.stdout.buffer.flush()


if __name__ == "__main__":
    run_cgi()
