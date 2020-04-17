import http.server
import socketserver
import termcolor
from Seq1 import *
import http.client
import requests, sys

# Define the Server's port
PORT = 8080
server = "https://rest.ensembl.org"


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


def html_folder(title):
    main_message = f"""
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>{title}</title>
  </head>
  <body style="background-color: lightblue;">
    <h1>List of species</h1>
    <p><textarea rows = "20" cols= "100">"""

    return main_message


final_message = f"""
    </textarea>
    </p>
    <a href="http://127.0.0.1:8080/">Main Page </a>
  </body>
</html> """


def info_species(serv):
    ext = "/info/species?"

    r = requests.get(serv + ext, headers={"Content-Type": "application/json"})

    if not r.ok:
        r.raise_for_status()
        sys.exit()

    decoded = r.json()
    # print(repr(decoded["species"][-1]["common_name"]))
    a = list(decoded["species"])
    return a
    #counter = 0
    list_animals = []
    #while counter < number:
        #animal = a[counter]["common_name"]
        #print(animal)
        #list_animals.append(animal)
        #counter += 1
    #return list_animals

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
        list_resource = self.path.split('?')
        resource = list_resource[0]
        if resource == "/":
            contents = Path("main_page.html").read_text()
            content_type = 'text/html'
            error_code = 200
        elif resource == "/listSpecies":
            tittle = "LIST OF SPECIES IN THE BROWSER"
            index_eq = self.path.find("=")
            number = int(self.path[index_eq + 1:])
            #a = info_species(server, number)
            contents_in = html_folder(tittle)
            print(contents_in)
            counter = 0
            a = info_species(server)
            contents_in += "There are a total of " + str(len(a)) + " species in the database" + "\n"
            contents_in += "You have selectioned a number of: " + str(number) + "species" \
                           + "\n" + "The name of the species are: " + "\n" + "\n"
            while counter < number:
                animal = a[counter]["common_name"]
                contents_in = contents_in + " ·" + animal + "\n"
                counter += 1
            contents = contents_in + final_message
            print(contents)
            content_type = 'text/html'
            error_code = 200
        elif resource == "/karyotype":
            tittle = "KARYOTIPE OF A SPECIFIC SPECIE"
            body = "ee"
            contents = html_folder(tittle, body)
            content_type = 'text/html'
            error_code = 200
        elif resource == "/chromosomeLength":
            tittle = "LENGTH OF THE SELECTED CHROMOSOME"
            body="eeeee"
            contents = html_folder(tittle, body)
            content_type = 'text/html'
            error_code = 200
        else:
            contents = Path("Error.html").read_text()
            content_type = 'text/html'
            error_code = 404

        self.send_response(error_code)
        # Define the content-type header:
        self.send_header('Content-Type', content_type)
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
