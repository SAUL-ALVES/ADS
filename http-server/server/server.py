from server.router import Router

class Server:
    def __init__(self):
        self.router = Router()

    def route(self, path, methods=["GET"]):
        def decorator(handler):
            self.router.add_route(path, handler, methods)
            return handler
        return decorator

    def start(self, host="localhost", port=8000):
        from http.server import HTTPServer, BaseHTTPRequestHandler

        router = self.router

        class RequestHandler(BaseHTTPRequestHandler):
            def do_GET(self):
                self.handle_request("GET")

            def do_POST(self):
                self.handle_request("POST")

            def handle_request(self, method):
                path = self.path.split("?")[0]
                handler = router.match(path, method)
                if not handler:
                    self.send_response(404)
                    self.end_headers()
                    self.wfile.write(b"Not Found")
                    return

                content_length = int(self.headers.get('Content-Length', 0))
                body = self.rfile.read(content_length).decode("utf-8") if content_length > 0 else ""
                request = {
                    "path": path,
                    "method": method,
                    "body": body,
                }
                response = {
                    "status": 200,
                    "headers": {},
                    "body": "",
                }
                handler(request, response)

                self.send_response(response.get("status", 200))
                for key, value in response.get("headers", {}).items():
                    self.send_header(key, value)
                self.end_headers()
                self.wfile.write(response.get("body", "").encode("utf-8"))

        print(f"Servidor rodando em http://{host}:{port}")
        HTTPServer((host, port), RequestHandler).serve_forever()
