# A simple python program that serves a directory via http on port 8080 (http://localhost:8080) and default to reading index.html
import http.server
import socketserver

# Define the directory you want to serve
DIRECTORY = "."

# Create a handler that serves files from the directory
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # Set the directory to serve
        # 
        # Parameters:
        #     *args (list): The arguments passed to the base class
        #     **kwargs (dict): The keyword arguments passed to the base class
        # 
        # Returns:
        #     None
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def do_GET(self):
        # Serve index.html by default
        
        # If the request path is '/', serve index.html in the current directory.
        # Otherwise, serve the requested file.
        
        # Returns:
        #     None

        if self.path == '/':
            self.path = 'index.html'
        return super().do_GET()

# Define the server address and port
PORT = 8080
Handler = MyHttpRequestHandler

# Create the server
with socketserver.TCPServer(("localhost", PORT), Handler) as httpd:
    print(f"Serving directory {DIRECTORY} at http://localhost:{PORT}")
    # Start the server
    httpd.serve_forever()
