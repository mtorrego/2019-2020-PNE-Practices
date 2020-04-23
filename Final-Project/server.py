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
    """

    return main_message


final_message = f"""
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


def chromosome_length(server1, specie, number1):
    ext = "/info/assembly/" + specie + "/" + str(number1) + "?"

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
    id_gene = decoded["id"]
    length_gene = end - start
    return f"The gene gene  starts at  {str(start)}<br>The gene gene ends at {str(end)}<br>The gene gene is located " \
           f"at {str(chromosome)} chromosome<br>The id of the gene is:  {id_gene}<br>" \
           f"The length of the gene is: {str(length_gene)}<br><br>"


def percentages(s):
    a = s.count()
    b = s.len()
    listvalues = list(a.values())
    listt = []
    for value in listvalues:
        listt.append(f"{value} {round(value / b * 100), 2}%")
    listkeys = list(a.keys())
    d = dict(zip(listkeys, listt))
    return d


def gene_list(server6, chromosome, start, end):
    ext = "/overlap/region/human/" + chromosome + ":" + start + "-" + end + \
          "?feature=gene;feature=transcript;feature=cds;feature=exon"

    r = requests.get(server6 + ext, headers={"Content-Type": "application/json"})

    if not r.ok:
        r.raise_for_status()
        sys.exit()

    decoded = r.json()
    return decoded


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
            line = list_resource[1]
            tittle = "LIST OF SPECIES IN THE BROWSER"
            sub_tittle = "List of species"
            index_eq = line.find("=")
            msg = line[index_eq + 1:]
            contents_in = html_folder(tittle, sub_tittle)
            a = info_species(server)
            total_number = len(a)
            contents_in += f"<p>There are a total of  {str(total_number)} species in the database<br>"
            counter = 0
            if msg == "":
                number = total_number
            else:
                number = msg
            contents_in += f"""You have selected a number of:  {str(number)}  species \
<br>The name of the species are: <ul>"""
            if 0 < int(number) <= int(total_number):
                while counter < int(number):
                    animal = a[counter]["common_name"]
                    contents_in = contents_in + f"<li> {animal} </li>"
                    counter += 1
                contents = contents_in + f"</ul>" + final_message
            else:
                contents = Path("Error.html").read_text()
            content_type = 'text/html'
            error_code = 200
        elif resource == "/karyotype":
            line = list_resource[1]
            tittle = "KARYOTYPE OF A SPECIFIC SPECIE"
            sub_tittle = "Karyotype of a specie"
            index_eq = line.find("=")
            msg = line[index_eq + 1:]
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
                contents_in += f"The names of the chromosomes of the specie: {str(msg)}  are: <br><ul>"
                for chrom in a:
                    contents_in += f" <li> {chrom} </li>"
                contents = contents_in + f"</ul>" + final_message
            else:
                contents = Path("Error.html").read_text()
            content_type = 'text/html'
            error_code = 200
        elif resource == "/chromosomeLength":
            line = list_resource[1]
            tittle = "LENGTH OF THE SELECTED CHROMOSOME"
            sub_tittle = "Chromosome Length"
            index_1 = line.find("=")
            index_2 = line.find("&")
            specie = line[index_1 + 1: index_2]

            if specie in list_species:
                number_1 = line[index_2:]
                list_number = number_1.split("=")[1:]
                number = 0
                for n in list_number:
                    number = n
                list_chromosome = []
                b = info_assembly(server, specie)
                for spec in b:
                    list_chromosome.append(spec)
                if number in list_chromosome:
                    length_final = chromosome_length(server, specie, number)
                    contents_in = html_folder(tittle, sub_tittle)
                    contents = contents_in + f"The length of the chromosome {number} is {str(length_final)} <br><br>" \
                        + final_message
                else:
                    contents = Path("Error.html").read_text()
            else:
                contents = Path("Error.html").read_text()
            content_type = 'text/html'
            error_code = 200
        elif resource == "/geneSeq":
            try:
                line = list_resource[1]
                tittle = "SEQUENCE OF A GENE"
                sub_tittle = "The sequence of a human gene"
                initial_index = line.find("=")
                gene = line[initial_index + 1:]
                id_gene = gene_seq(gene)
                sequence = get_sequence(id_gene)
                contents_in = html_folder(tittle, sub_tittle)
                contents_in += f"""The sequence of the gene {gene} is:<p><textarea rows = "20" cols= "100" 
style="background-color: lightpink;">{sequence}"""
                contents = contents_in + f"</textarea></p>" + final_message
                content_type = 'text/html'
                error_code = 200
            except IndexError:
                contents = Path("Error.html").read_text()
                content_type = 'text/html'
                error_code = 404
        elif resource == "/geneInfo":
            try:
                line = list_resource[1]
                tittle = "INFO OF A GENE"
                sub_tittle = "The information of a human gene"
                contents_in = html_folder(tittle, sub_tittle)
                initial_index = line.find("=")
                gene = line[initial_index + 1:]
                contents_in += gene_info(server, gene)
                contents = contents_in + final_message
                content_type = 'text/html'
                error_code = 200
            except IndexError:
                contents = Path("Error.html").read_text()
                content_type = 'text/html'
                error_code = 404
        elif resource == "/geneCalc":
            try:
                line = list_resource[1]
                tittle = "INFO OF A GENE"
                sub_tittle = "The information of a human gene"
                contents_in = html_folder(tittle, sub_tittle)
                initial_index = line.find("=")
                gene = line[initial_index + 1:]
                id_gene = gene_seq(gene)
                s = get_sequence(id_gene)
                seq = Seq(s)
                dict_sol = percentages(seq)
                a = list(dict_sol.keys())
                b = list(dict_sol.values())
                contents_in += f"The length of the gene is: {str(seq.len())} <br>Information about the bases<ul>"
                for n in dict_sol.keys():
                    p = a.index(n)
                    contents_in += f"<li> Base:  {str(a[p])}"
                    contents_in += f" --> {str(b[p])} </li>"
                contents = contents_in + f"</ul>" + final_message
                content_type = 'text/html'
                error_code = 200
            except IndexError:
                contents = Path("Error.html").read_text()
                content_type = 'text/html'
                error_code = 404
        elif resource == "/geneList":
            try:
                line = list_resource[1]
                tittle = "LIST OF GENES IN A RANGE"
                sub_tittle = "All the genes in a specific range"
                contents_in = html_folder(tittle, sub_tittle)
                list_ = line.split("=")
                a = list_[1].find("&")
                chromosome = list_[1][:a]
                b = list_[2].find("&")
                start = list_[2][:b]
                end = list_[3]
                function = gene_list(server, chromosome, start, end)
                contents_in += f"The genes in the range: {start} - {end} are: <br><br>"
                for n in function:
                    index = function.index(n)
                    contents_in += f"""Gene: {function[index]["id"]}"""
                    if "external_name" in function[index]:
                        contents_in += f""" -->  {function[index]["external_name"]}<br>"""
                    else:
                        contents_in += f"<br>"
                contents = contents_in + final_message
                content_type = 'text/html'
                error_code = 200
            except requests.exceptions.HTTPError:
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
