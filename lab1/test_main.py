import io
import sys
from unittest.mock import patch

from main import get_os_info, render_html, run_cgi


class FakeStdout(io.StringIO):
    """StringIO with a binary buffer, mimicking sys.stdout."""

    def __init__(self) -> None:
        super().__init__()
        self.buffer: io.BytesIO = io.BytesIO()


def test_get_os_info_returns_three_strings() -> None:
    result = get_os_info()
    assert isinstance(result, tuple)
    assert len(result) == 3
    assert all(isinstance(s, str) for s in result)


def test_render_html_contains_os_info() -> None:
    html = render_html("Linux", "6.1.0", "Debian 6.1")
    assert "<b>Operating System:</b> Linux 6.1.0" in html
    assert "<b>Version:</b> Debian 6.1" in html


def test_run_cgi_headers_and_body() -> None:
    fake = FakeStdout()

    with patch.object(sys, "stdout", fake):
        with patch("main.get_os_info", return_value=("MockOS", "1.0", "mock-version")):
            run_cgi()

    headers = fake.getvalue()
    body = fake.buffer.getvalue().decode("utf-8")

    assert headers.startswith("Content-Type: text/html; charset=utf-8\r\n")
    assert f"Content-Length: {len(body.encode('utf-8'))}\r\n" in headers
    assert "<b>Operating System:</b> MockOS 1.0" in body
    assert "<b>Version:</b> mock-version" in body
