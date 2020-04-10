import http.server
import socketserver
import termcolor
from Seq0 import *
from Seq1 import *

# Define the Server's port
PORT = 8080


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


def html_folder(title, h1, body):
    main_message = f"""
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>{title}</title>
  </head>
  <body style="background-color: white;">
    <h1>{h1}</h1>
    <p><textarea rows = "20" cols= "100">{body}</textarea>
    
    </p>
    <a href="http://127.0.0.1:8080/">Main Page </a>
  </body>
</html>
"""

    return main_message


def ex4(sequence, info, result):
    main_message = f"""
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>OPERATION</title>
  </head>
  <body style="background-color: white;">
    <h1>Sequence</h1>
    <p><textarea rows = "5" cols= "100">{sequence}</textarea></p>
    <hr>
    <h2>Operation</h2>
    <p>{info}</p>
    <hr>
    <h3>Result</h3>
    <p><textarea rows = "6" cols= "100">{result}</textarea></p>
    <hr>
    <a href="http://127.0.0.1:8080/">Main Page </a>
  </body>
</html>
"""

    return main_message


listsequences = ["AATTCCTACTGAACACTGGATGGGTGTACA", "GTGATACTAGATCACAACTTAGTCAGTCGT", "AAACCCTATGAGCTCGAGCTGATCGACATG",
                 "TTTACTTCGGATCACGATGCATAGTTACCA", "ACTTACGATCGTATCGACAAATCGTTTGCA"]

FOLDER = "../Session-04/"
list_names = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
ext = ".txt"


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Open the form1.html file
        # Read the index from the file
        if self.path == "/":
            contents = Path("form-4.html").read_text()
            self.send_response(200)
        elif "/ping" in self.path:
            h1 = "PING OK"
            body = "The sequence is running"
            contents = html_folder("PING", h1, body)
            self.send_response(200)
        elif "/get" in self.path:
            a = self.path.find("=")
            number = int(self.path[a + 1:])
            seq = listsequences[number]
            h1 = "Sequence number " + str(number)
            contents = html_folder("GET", h1, seq)
            self.send_response(200)
        elif "/gene" in self.path:
            a = self.path.find("=")
            name = self.path[a + 1:]
            seq = seq_read_fasta(FOLDER + name + ext)
            h1 = "Gene " + name
            contents = html_folder("GENE", h1, seq)
            self.send_response(200)
        elif "/operation" in self.path:
            a = self.path.find("=")
            b = self.path.find("&")
            seq = self.path[a + 1: b]
            s = Seq(seq)
            if "INFO" in self.path:
                a = s.count()
                b = s.len()
                listvalues = list(a.values())
                listt = []
                for value in listvalues:
                    listt.append(f"{value} {round(value / b * 100), 2}%")
                listkeys = list(a.keys())
                d = dict(zip(listkeys, listt))
                sol = ""
                for n in listkeys:
                    a = listkeys.index(n)
                    sol = sol + "\n" + str(listkeys[a]) + " = " + str(listt[a])
                response = f"The length is: {b} \n{sol}"
                contents = ex4(seq, "INFO", response)
            elif "COMP" in self.path:
                res = s.seq_complement()
                contents = ex4(seq, "COMP", res)
            elif "REV" in self.path:
                res = s.seq_reverse()
                contents = ex4(seq, "REV", res)
            self.send_response(200)
        else:
            contents = Path("Error.html").read_text()
            self.send_response(404)

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

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
