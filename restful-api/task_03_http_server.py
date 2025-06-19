#!/usr/bin/env python3
"""
Simple API server using python's http.server module
Shows Basic HTTP request handling and JSON responses
"""

import json
import http.server
import socketserver
from urllib.parse import urlparse


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    Since we are inheriting fron BaseHTTPRequestHandler -
    we will get all networking infrastructure and only need
    to define our specific response logic
    """

    def do_GET(self):
        """
        Method will be called whenever we GET a request to our server
        """

        parsed_path = urlparse(self.path).path

        if parsed_path == '/':
            self._handle_root()
        elif parsed_path == '/data':
            self._handle_data()
        elif parsed_path == '/status':
            self._handle_status()
        else:
            self._handle_not_found()

    def _handle_root(self):
        """
        Handles requests to the root endpoint '/'
        Welcome users to the API.
        """

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        response_text = "Hello, welcome to this simple API!"
        self.wfile.write(response_text.encode('utf-8'))

    def _handle_data(self):
        """
        Handles request to /data endpoint
        Returns JSON data about a person
        """

        data = {
            "name": "John",
            "age": 30,
            "city": "New York"
        }

        json_response = json.dumps(data)

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Content-Length', str(len(json_response)))
        self.end_headers()
        self.wfile.write(json_response.encode('utf-8'))

    def _handle_status(self):
        """
        Handles requests to /status endpoint
        Returns simple status information
        """

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write("OK".encode('utf-8'))

    def _handle_not_found(self):
        """
        Handles undefined request endpoints
        Returns 404 NOT FOUND error
        """
        self.send_response(404)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        error_response = {
            "error": "Endpoint not found",
            "message": f"The requested endpoint '{self.path}' does not exist"
        }

        json_response = json.dumps(error_response)
        self.wfile.write(json_response.encode('utf-8'))

    def log_message(self, format, *args):
        """
        Override default logging making it more informative
        Shows requests are being made
        """
        print(f"[{self.address_string()}]{format % args}")


def run_server(port=8000):
    """
    Create and run the HTTP Server
    Sets up and begins listening for connections inbound
    """

    with socketserver.TCPServer(("", port), SimpleAPIHandler) as httpd:
        print(f"Starting server on port {port}")
        print(f"Visiting http://localhost:{port} to test your API")
        print("Available endpoints:")
        print(" / - Welcome message")
        print(" /data - JSON data about a person")
        print(" /status - API status check")
        print("\nPess Ctrl+C to stop server")

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped by user")


if __name__ == "__main__":
    run_server()
