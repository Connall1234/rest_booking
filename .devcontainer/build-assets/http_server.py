"""
Simple wrapper for http.server
to switch off caching for users

"""

import http.server

class NoCacheHTTPHandler(http.server.SimpleHTTPRequestHandler):
    """
    Subclass of http.server.SimpleHTTPRequestHandler that adds headers
    to disable caching for users.
    """

    def end_headers(self):
        """
        Overrides the default end_headers method to add cache control headers.
        """
        self.send_cache_headers()
        http.server.SimpleHTTPRequestHandler.end_headers(self)

    def send_cache_headers(self):
        """
        Sends cache control headers to disable caching.
        """
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")

if __name__ == '__main__':
    http.server.test(HandlerClass=NoCacheHTTPHandler)
