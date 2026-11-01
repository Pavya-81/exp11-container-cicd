from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        message = b"Hello from a Docker container built by GitHub Actions!\n"

        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(message)))
        self.end_headers()

        self.wfile.write(message)


HTTPServer(
    ("0.0.0.0", int(os.environ.get("PORT", "8080"))),
    Handler
).serve_forever()