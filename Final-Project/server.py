import http.server
import socketserver
import termcolor
from Seq1 import *
import http.client
import requests
import sys
import json

# Define the Server's port
PORT = 8080
server = "https://rest.ensembl.org"


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


def html_folder(title, sub_tittle):
    main_message = f"""
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>{title}</title>
  </head>
  <body style="background-color: lightblue;">
    <h1>{sub_tittle}</h1>
    <p><textarea rows = "20" cols= "100" style="background-color: lightpink;">"""

    return main_message


final_message = f"""
    </textarea>
    </p>
    <a href="http://127.0.0.1:8080/">Main Page </a>
  </body>
</html> """


def info_species(server1):
    ext = "/info/species?"

    r = requests.get(server1 + ext, headers={"Content-Type": "application/json"})

    if not r.ok:
        r.raise_for_status()
        sys.exit()

    decoded = r.json()
    # print(repr(decoded["species"][-1]["common_name"]))
    a = list(decoded["species"])
    return a


def info_assembly(server1, specie):
    ext = "/info/assembly/" + specie + "?"

    r = requests.get(server1 + ext, headers={"Content-Type": "application/json"})

    if not r.ok:
        r.raise_for_status()
        sys.exit()

    decoded = r.json()
    # print(repr(decoded))
    a = list(decoded["karyotype"])
    return a


def chromosome_length(server1, specie, number):
    ext = "/info/assembly/" + specie + "/" + str(number) + "?"

    r = requests.get(server1 + ext, headers={"Content-Type": "application/json"})

    if not r.ok:
        r.raise_for_status()
        sys.exit()

    decoded = r.json()
    length = decoded["length"]
    return length


def gene_seq(gene):
    ext = "/xrefs/symbol/homo_sapiens/" + gene + "?"

    r = requests.get(server + ext, headers={"Content-Type": "application/json"})

    if not r.ok:
        r.raise_for_status()
        sys.exit()

    decoded = r.json()
    id_gene = decoded[0]["id"]
    return id_gene


def get_sequence(id_gene):
    server4 = "rest.ensembl.org"
    endpoint = "/sequence/id"
    params = "/" + id_gene + "?content-type=application/json"
    conn = http.client.HTTPConnection(server4)

    try:
        conn.request("GET", endpoint + params)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()
    response = conn.getresponse()
    data1 = response.read().decode("utf-8")
    data = json.loads(data1)
    seq = data["seq"]
    return seq


def gene_info(server5, gene):
    ext = "/lookup/symbol/homo_sapiens/" + gene + "?"

    r = requests.get(server5 + ext, headers={"Content-Type": "application/json"})

    if not r.ok:
        r.raise_for_status()
        sys.exit()

    decoded = r.json()
    start = decoded["start"]
    end = decoded["end"]
    chromosome = decoded["seq_region_name"]
    return "The gene " + gene + " starts at " + str(start) + "\n" + "The gene " + gene + " ends at " + str(end) + "\n" + \
           "The gene " + gene + " is located at " + str(chromosome) + " chromosome \n"


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        global contents
        global number
        termcolor.cprint(self.requestline, 'green')

        # Open the form1.html file
        # Read the index from the file
        list_resource = self.path.split('?')
        resource = list_resource[0]

        a = info_species(server)
        counter = 0
        list_species = []
        while counter < int(len(a)):
            animal = a[counter]["common_name"]
            list_species.append(animal)
            counter += 1

        if resource == "/":
            contents = Path("main_page.html").read_text()
            content_type = 'text/html'
            error_code = 200
        elif resource == "/listSpecies":
            tittle = "LIST OF SPECIES IN THE BROWSER"
            sub_tittle = "List of species"
            index_eq = self.path.find("=")
            msg = self.path[index_eq + 1:]
            contents_in = html_folder(tittle, sub_tittle)
            a = info_species(server)
            total_number = len(a)
            contents_in += "There are a total of " + str(total_number) + " species in the database" + "\n"
            counter = 0
            if msg == "":
                number = total_number
            else:
                number = msg
            contents_in += "You have selectioned a number of: " + str(number) + " species" \
                            + "\n" + "The name of the species are: " + "\n" + "\n"
            if 0 < int(number) <= int(total_number):
                while counter < int(number):
                    animal = a[counter]["common_name"]
                    contents_in = contents_in + " ·" + animal + "\n"
                    counter += 1
                contents = contents_in + final_message
            else:
                contents = Path("Error.html").read_text()
            content_type = 'text/html'
            error_code = 200
        elif resource == "/karyotype":
            tittle = "KARYOTYPE OF A SPECIFIC SPECIE"
            sub_tittle = "Karyotype of a specie"
            index_eq = self.path.find("=")
            msg = self.path[index_eq + 1:]
            a = info_species(server)
            counter = 0
            list_species = []
            while counter < int(len(a)):
                animal = a[counter]["common_name"]
                list_species.append(animal)
                counter += 1
            if msg in list_species:
                contents_in = html_folder(tittle, sub_tittle)
                a = info_assembly(server, msg)
                contents_in += "The names of the chromosomes of the specie: " + str(msg) + " are: " + "\n\n"
                for chrom in a:
                    contents_in += " ·" + chrom + "\n"
                contents = contents_in + final_message
            else:
                contents = Path("Error.html").read_text()
            content_type = 'text/html'
            error_code = 200
        elif resource == "/chromosomeLength":
            tittle = "LENGTH OF THE SELECTED CHROMOSOME"
            sub_tittle = "Chromosome Length"
            index_1 = self.path.find("=")
            index_2 = self.path.find("&")
            specie = self.path[index_1 + 1: index_2]

            if specie in list_species:
                number_1 = self.path[index_2:]
                list_number = number_1.split("=")[1:]
                for n in list_number:
                    number = n
                list_chromosome = []
                b = info_assembly(server, specie)
                for spec in b:
                    list_chromosome.append(spec)
                if number in list_chromosome:
                    length_final = chromosome_length(server, specie, number)
                    contents_in = html_folder(tittle, sub_tittle)
                    contents = contents_in + "The length of the chromosome " + number + " is " \
                                + str(length_final) + final_message
                else:
                    contents = Path("Error.html").read_text()
            else:
                contents = Path("Error.html").read_text()
            content_type = 'text/html'
            error_code = 200
        elif resource == "/geneSeq":
            try:
                tittle = "SEQUENCE OF A GENE"
                sub_tittle = "The sequence of a human gene"
                initial_index = self.path.find("=")
                gene = self.path[initial_index + 1:]
                id_gene = gene_seq(gene)
                sequence = get_sequence(id_gene)
                contents_in = html_folder(tittle, sub_tittle)
                contents = contents_in + "The sequence of the gene " + gene + " is: " + "\n\n" + \
                        + sequence + final_message
                content_type = 'text/html'
                error_code = 200
            except IndexError:
                contents = Path("Error.html").read_text()
                content_type = 'text/html'
                error_code = 404
        elif resource == "/geneInfo":
            try:
                tittle = "INFO OF A GENE"
                sub_tittle = "The information of a human gene"
                contents_in = html_folder(tittle, sub_tittle)
                initial_index = self.path.find("=")
                gene = self.path[initial_index + 1:]
                id_gene = gene_seq(gene)
                contents_in += gene_info(server, gene)
                sequence = get_sequence(id_gene)
                len_seq = len(sequence)
                contents_in += "The length of the gene " + gene + " is: " + str(len_seq)
                contents = contents_in + final_message
                content_type = 'text/html'
                error_code = 200
            except IndexError:
                contents = Path("Error.html").read_text()
                content_type = 'text/html'
                error_code = 404
        else:
            contents = Path("Error.html").read_text()
            content_type = 'text/html'
            error_code = 404

        print(resource)
        print(contents)
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
