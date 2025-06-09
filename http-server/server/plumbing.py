def html_response(body, status=200):
    return (
        f"HTTP/1.1 {status} OK\r\n"
        "Content-Type: text/html; charset=utf-8\r\n"
        "Content-Length: {}\r\n"
        "\r\n"
        "{}"
    ).format(len(body.encode('utf-8')), body).encode('utf-8')
