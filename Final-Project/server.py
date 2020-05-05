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
IP = "localhost"
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


def info_species():
    ext = "/info/species?"

    r = requests.get(server + ext, headers={"Content-Type": "application/json"})

    if not r.ok:
        r.raise_for_status()
        sys.exit()

    decoded = r.json()
    list_species = list(decoded["species"])
    return list_species


def info_assembly(specie):
    ext = "/info/assembly/" + specie + "?"

    r = requests.get(server + ext, headers={"Content-Type": "application/json"})

    if not r.ok:
        r.raise_for_status()
        sys.exit()

    decoded = r.json()
    list_karyotype = list(decoded["karyotype"])
    return list_karyotype


def chromosome_length(specie, number1):
    ext = "/info/assembly/" + specie + "/" + str(number1) + "?"

    r = requests.get(server + ext, headers={"Content-Type": "application/json"})

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


def gene_info(gene):
    ext = "/lookup/symbol/homo_sapiens/" + gene + "?"

    r = requests.get(server + ext, headers={"Content-Type": "application/json"})

    if not r.ok:
        r.raise_for_status()
        sys.exit()

    decoded = r.json()
    start = decoded["start"]
    end = decoded["end"]
    chromosome = decoded["seq_region_name"]
    id_gene = decoded["id"]
    length_gene = end - start
    return start, end, chromosome, id_gene, length_gene


def percentages(seq):
    count_bases = seq.count()
    length = seq.len()
    listvalues = list(count_bases.values())
    listt = []
    for value in listvalues:
        listt.append(f"{value} {round(value / length * 100), 2}%")
    listkeys = list(count_bases.keys())
    full_dictionary = dict(zip(listkeys, listt))
    return full_dictionary


def gene_list(chromosome, start, end):
    ext = "/overlap/region/human/" + chromosome + ":" + start + "-" + end + \
          "?feature=gene;feature=transcript;feature=cds;feature=exon"

    r = requests.get(server + ext, headers={"Content-Type": "application/json"})

    if not r.ok:
        r.raise_for_status()
        sys.exit()

    decoded = r.json()
    return decoded


def list_names(dict_species):
    counter = 0
    list_name = []
    while counter < int(len(dict_species)):
        animal = dict_species[counter]["common_name"]
        list_name.append(animal)
        counter += 1
    return list_name


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
        if "json=1" in self.path:
            content_type = "application/json"
            index_json = self.path.find("json=1")
            real_resource = self.path[:index_json - 1]
        else:
            content_type = "text/html"
            real_resource = self.path
        error_code = 200
        contents = ""
        list_resource = real_resource.split('?')
        resource = list_resource[0]

        if resource == "/":
            contents = Path("index-advanced.html").read_text()
            content_type = 'text/html'
            error_code = 200
        else:
            if resource == "/listSpecies":
                line = list_resource[1]
                tittle = "LIST OF SPECIES IN THE BROWSER"
                sub_tittle = "List of species"
                index_eq = line.find("=")
                msg = line[index_eq + 1:]
                contents_in = html_folder(tittle, sub_tittle)
                a = info_species()
                total_number = len(a)
                contents_in += f"<p>There are a total of  {str(total_number)} species in the database<br>"
                counter = 0
                if msg == "":
                    number = total_number
                else:
                    number = msg
                contents_in += f"""You have selected a number of:  {str(number)}  species \
            <br>The name of the species are: <ul>"""
                list_animals = []
                list_counter = []
                if 0 < int(number) <= int(total_number):
                    if "json=1" in self.path:
                        while counter < int(number):
                            list_animals.append(a[counter]["common_name"])
                            counter += 1
                            list_counter.append(str(counter)+": ")
                        contents = dict(zip(list_counter, list_animals))
                    else:
                        while counter < int(number):
                            animal = a[counter]["common_name"]
                            contents_in = contents_in + f"<li> {animal} </li>"
                            counter += 1
                        contents = contents_in + f"</ul>" + final_message
                    error_code = 200
                else:
                    contents = Path("Error.html").read_text()
                    error_code = 404
            elif resource == "/karyotype":
                line = list_resource[1]
                tittle = "KARYOTYPE OF A SPECIFIC SPECIE"
                sub_tittle = "Karyotype of a specie"
                index_eq = line.find("=")
                msg = line[index_eq + 1:]
                a = info_species()
                list_species = list_names(a)
                if msg in list_species:
                    contents_in = html_folder(tittle, sub_tittle)
                    list_karyotype = info_assembly(msg)
                    contents_in += f"The names of the chromosomes of the specie: {str(msg)}  are: <br><ul>"
                    if "json=1" in self.path:
                        counter_list = []
                        for karyotype in list_karyotype:
                            index = str(list_karyotype.index(karyotype))
                            counter_list.append(index)
                        contents = dict(zip(counter_list, list_karyotype))
                    else:
                        for karyotype in list_karyotype:
                            contents_in += f" <li> {karyotype} </li>"
                        contents = contents_in + f"</ul>" + final_message
                    error_code = 200
                else:
                    contents = Path("Error.html").read_text()
                    error_code = 404
            elif resource == "/chromosomeLength":
                line = list_resource[1]
                tittle = "LENGTH OF THE SELECTED CHROMOSOME"
                sub_tittle = "Chromosome Length"
                index_1 = line.find("=")
                index_2 = line.find("&")
                specie = line[index_1 + 1: index_2]
                a = info_species()
                list_species = list_names(a)

                if specie in list_species:
                    number_1 = line[index_2:]
                    list_number = number_1.split("=")[1:]
                    number = 0
                    for n in list_number:
                        number = n
                    list_chromosome = info_assembly(specie)
                    if number in list_chromosome:
                        length_final = chromosome_length(specie, number)
                        contents_in = html_folder(tittle, sub_tittle)
                        if "json=1" in self.path:
                            phrase = "The length of the chromosome " + number + " is: "
                            contents = {phrase: str(length_final)}
                        else:
                            contents = contents_in + f"The length of the chromosome {number} is {str(length_final)} " \
                                                 f"<br><br>" + final_message
                        error_code = 200
                    else:
                        contents = Path("Error.html").read_text()
                        error_code = 404
                else:
                    contents = Path("Error.html").read_text()
                    error_code = 404

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
                    if "json=1" in self.path:
                        phrase = "The seqnece of the gene " + gene + " is: "
                        contents = {phrase: sequence}
                    else:
                        contents = contents_in + f"</textarea></p>" + final_message
                    error_code = 200
                except IndexError:
                    contents = Path("Error.html").read_text()
                    error_code = 404

            elif resource == "/geneInfo":
                try:
                    line = list_resource[1]
                    tittle = "INFO OF A GENE"
                    sub_tittle = "The information of a human gene"
                    contents_in = html_folder(tittle, sub_tittle)
                    initial_index = line.find("=")
                    gene = line[initial_index + 1:]
                    start, end, chromosome, id_gene, length_gene = gene_info(gene)
                    if "json=1" in self.path:
                        contents = {"Starts at:": start, "Ends at": end, "Located at chromosome:": chromosome,
                                    "Id of the gene:": id_gene, "Length of the gene: ": length_gene}
                    else:
                        contents_in += f"The gene gene  starts at  {str(start)}<br>The gene gene ends at {str(end)}" \
                                       f"<br>The gene gene is located at {str(chromosome)} chromosome<br>" \
                                       f"The id of the gene is:  {id_gene}<br>The length of the gene is: " \
                                       f"{str(length_gene)}<br><br>"
                        contents = contents_in + final_message
                    error_code = 200
                except IndexError:
                    contents = Path("Error.html").read_text()
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
                    list_keys = list(dict_sol.keys())
                    list_values = list(dict_sol.values())
                    contents_in += f"The length of the gene is: {str(seq.len())} <br>Information about the bases<ul>"
                    if "json=1" in self.path:
                        for n in list_keys:
                            index_base = list_keys.index(n)
                            list_keys[index_base] = "Base: " + list_keys[index_base]
                        list_keys.append("The length of the gene is: ")
                        list_values.append(str(seq.len()))
                        contents = dict(zip(list_keys, list_values))
                    else:
                        for n in list_keys:
                            index_base = list_keys.index(n)
                            contents_in += f"<li> Base:  {str(list_keys[index_base])}"
                            contents_in += f" --> {str(list_values[index_base])} </li>"
                        contents = contents_in + f"</ul>" + final_message
                    error_code = 200
                except IndexError:
                    contents = Path("Error.html").read_text()
                    error_code = 404
            elif resource == "/geneList":
                try:
                    line = list_resource[1]
                    tittle = "LIST OF GENES IN A RANGE"
                    sub_tittle = "All the genes in a specific range"
                    contents_in = html_folder(tittle, sub_tittle)
                    list_ = line.split("=")
                    index_a = list_[1].find("&")
                    chromosome = list_[1][:index_a]
                    index_b = list_[2].find("&")
                    start = list_[2][:index_b]
                    end = list_[3]
                    function = gene_list(chromosome, start, end)
                    contents_in += f"The genes in the range: {start} - {end} are: <br><br>"
                    if "json=1" in self.path:
                        list_keys = []
                        list_values = []
                        for n in function:
                            index = function.index(n)
                            list_keys.append(function[index]["id"])
                            if "external_name" in function[index]:
                                list_values.append(function[index]["external_name"])
                            else:
                                list_values.append("No name found")
                        contents = dict(zip(list_keys, list_values))
                    else:
                        for n in function:
                            index = function.index(n)
                            contents_in += f"""Gene: {function[index]["id"]}"""
                            if "external_name" in function[index]:
                                contents_in += f""" -->  {function[index]["external_name"]}<br>"""
                            else:
                                contents_in += f"<br>"
                        contents = contents_in + final_message
                    error_code = 200
                except requests.exceptions.HTTPError:
                    contents = Path("Error.html").read_text()
                    error_code = 404
        print(contents)

        self.send_response(error_code)
        # Define the content-type header:
        self.send_header('Content-Type', content_type)
        if "json=1" in self.path:
            encoded_dict = str(contents).encode('utf-8')
            # -- base64_dict = base64.b64encode(encoded_dict)
            self.send_header('Content-Length', len(encoded_dict))
            self.end_headers()
            self.wfile.write(encoded_dict)
        else:
            self.send_header('Content-Length', len(str.encode(contents)))
            self.end_headers()
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
