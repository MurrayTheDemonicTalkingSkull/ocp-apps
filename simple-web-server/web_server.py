from http.server import SimpleHTTPRequestHandler, HTTPServer


class HelloWorldHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Respond with "200 OK" and specify HTML content type
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # Write the response body
        self.wfile.write(b"Hello, World! version1")


# Define the server address and port
server_address = ('', 8000)
httpd = HTTPServer(server_address, HelloWorldHandler)

print("Server running on port 8000...")
httpd.serve_forever()