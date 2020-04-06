import http.server
import socketserver
import termcolor
from Seq0 import *

# Define the Server's port
PORT = 8080
FOLDER = "../Session-14/"
html = ".html"


def seq_read_fasta(filename):
    file_contents = Path(filename).read_text()
    content = file_contents.split("\n")[1:]
    e = "".join(content)
    return e


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happy server: It always returns a message saying
        # that everything is ok

        # Message to send back to the client
        if self.path == "/" or self.path == "/index.html":
            msg = "Index.html"
        else:
            msg = self.path
        try:
            contents = seq_read_fasta(FOLDER + msg)
            self.send_response(200)
        except FileNotFoundError:
            contents = seq_read_fasta(FOLDER + "error" + html)
            self.send_response(404)

        # Generating the response message


        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()