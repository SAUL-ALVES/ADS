
import re

class Router:
    def __init__(self):
        self.routes = []

    def add_route(self, path, handler, methods=["GET"]):
        self.routes.append((path, handler, methods))

    def match(self, path, method):
        for route_path, handler, methods in self.routes:
            if method not in methods:
                continue
            if "<id>" in route_path:
                pattern = re.sub(r"<id>", r"(\\d+)", route_path)
                if re.fullmatch(pattern, path):
                    return handler
            elif route_path == path:
                return handler
        return None
