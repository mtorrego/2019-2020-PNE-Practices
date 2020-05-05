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


def get_info(ext):

    r = requests.get(server + ext, headers={"Content-Type": "application/json"})

    if not r.ok:
        r.raise_for_status()
        sys.exit()

    decoded = r.json()
    return decoded


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
        request_line = self.path
        if "json=1" in request_line:
            content_type = "application/json"
            index_json = request_line.find("json=1")
            real_resource = request_line[:index_json - 1]
        else:
            content_type = "text/html"
            real_resource = request_line
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
                # First things to do
                line = list_resource[1]
                tittle = "LIST OF SPECIES IN THE BROWSER"
                sub_tittle = "List of species"
                index_eq = line.find("=")
                msg = line[index_eq + 1:]
                contents_in = html_folder(tittle, sub_tittle)
                # Getting the list of species
                ext = "/info/species?"
                a = get_info(ext)
                list_species = list(a["species"])
                total_number = len(list_species)
                contents_in += f"<p>There are a total of  {str(total_number)} species in the database<br>"
                # Seeing what is the number
                if msg == "":
                    number = total_number
                else:
                    number = msg
                contents_in += f"""You have selected a number of:  {str(number)}  species \
            <br>The name of the species are: <ul>"""
                counter = 0
                list_animals = []
                list_counter = []
                if 0 < int(number) <= int(total_number):
                    # Viewing if it is json or not
                    if "json=1" in request_line:
                        while counter < int(number):
                            list_animals.append(list_species[counter]["common_name"])
                            counter += 1
                            list_counter.append(str(counter)+": ")
                        contents = dict(zip(list_counter, list_animals))
                    else:
                        while counter < int(number):
                            animal = list_species[counter]["common_name"]
                            contents_in = contents_in + f"<li> {animal} </li>"
                            counter += 1
                        contents = contents_in + f"</ul>" + final_message
                    error_code = 200
                else:
                    contents = Path("Error.html").read_text()
                    error_code = 404
            elif resource == "/karyotype":
                # First things to do
                line = list_resource[1]
                tittle = "KARYOTYPE OF A SPECIFIC SPECIE"
                sub_tittle = "Karyotype of a specie"
                index_eq = line.find("=")
                msg = line[index_eq + 1:]
                # Getting the list of species to prove if what you have writen exists
                ext1 = "/info/species?"
                ext2 = "/info/assembly/" + msg + "?"
                a = get_info(ext1)
                list_species = list(a["species"])
                list_species = list_names(list_species)
                if msg in list_species:
                    contents_in = html_folder(tittle, sub_tittle)
                    # Getting the info of the second endpoint
                    list_karyotype = get_info(ext2)
                    list_karyotype = list(list_karyotype["karyotype"])
                    contents_in += f"The names of the chromosomes of the specie: {str(msg)}  are: <br><ul>"
                    if "json=1" in request_line:
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
                # First things to do
                line = list_resource[1]
                tittle = "LENGTH OF THE SELECTED CHROMOSOME"
                sub_tittle = "Chromosome Length"
                index_1 = line.find("=")
                index_2 = line.find("&")
                specie = line[index_1 + 1: index_2]
                # Getting all the species to prove if the specie you have writen exists
                ext1 = "/info/species?"
                ext2 = "/info/assembly/" + specie + "?"
                a = get_info(ext1)
                list_species = list(a["species"])
                list_species = list_names(list_species)

                if specie in list_species:
                    number_1 = line[index_2:]
                    list_number = number_1.split("=")[1:]
                    number = 0
                    for n in list_number:
                        number = n
                    # Doing a list to prove if the chromosome exists
                    list_chromosome = get_info(ext2)
                    list_chromosome = list(list_chromosome["karyotype"])
                    if number in list_chromosome:
                        # Getting the info of the third endpoint
                        ext3 = "/info/assembly/" + specie + "/" + str(number) + "?"
                        length_final = get_info(ext3)
                        length = length_final["length"]
                        contents_in = html_folder(tittle, sub_tittle)
                        if "json=1" in request_line:
                            phrase = "The length of the chromosome " + number + " is: "
                            contents = {phrase: str(length)}
                        else:
                            contents = contents_in + f"The length of the chromosome {number} is {str(length)} " \
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
                    # First things to do
                    line = list_resource[1]
                    tittle = "SEQUENCE OF A GENE"
                    sub_tittle = "The sequence of a human gene"
                    initial_index = line.find("=")
                    gene = line[initial_index + 1:]
                    # Getting the sequence of the gene
                    ext = "/xrefs/symbol/homo_sapiens/" + gene + "?"
                    id_gene = get_info(ext)
                    id_gene = id_gene[0]["id"]
                    sequence = get_sequence(id_gene)
                    contents_in = html_folder(tittle, sub_tittle)
                    contents_in += f"""The sequence of the gene {gene} is:<p><textarea rows = "20" cols= "100" 
                                style="background-color: lightpink;">{sequence}"""
                    # Viewing if it is json or not
                    if "json=1" in request_line:
                        phrase = "The seqnece of the gene " + gene + " is: "
                        contents = {phrase: sequence}
                    else:
                        contents = contents_in + f"</textarea></p>" + final_message
                    error_code = 200
                except requests.exceptions.HTTPError:
                    contents = Path("Error.html").read_text()
                    error_code = 404

            elif resource == "/geneInfo":
                try:
                    # First things to do
                    line = list_resource[1]
                    tittle = "INFO OF A GENE"
                    sub_tittle = "The information of a human gene"
                    contents_in = html_folder(tittle, sub_tittle)
                    initial_index = line.find("=")
                    gene = line[initial_index + 1:]
                    # Getting all the information of the endpoint geneInfo
                    ext = "/lookup/symbol/homo_sapiens/" + gene + "?"
                    decoded = get_info(ext)
                    start = decoded["start"]
                    end = decoded["end"]
                    chromosome = decoded["seq_region_name"]
                    id_gene = decoded["id"]
                    length_gene = end - start
                    # Viewing if it is json or not
                    if "json=1" in request_line:
                        contents = {"Starts at:": start, "Ends at": end, "Located at chromosome:": chromosome,
                                    "Id of the gene:": id_gene, "Length of the gene: ": length_gene}
                    else:
                        contents_in += f"The gene gene  starts at  {str(start)}<br>The gene gene ends at {str(end)}" \
                                       f"<br>The gene gene is located at {str(chromosome)} chromosome<br>" \
                                       f"The id of the gene is:  {id_gene}<br>The length of the gene is: " \
                                       f"{str(length_gene)}<br><br>"
                        contents = contents_in + final_message
                    error_code = 200
                except requests.exceptions.HTTPError:
                    contents = Path("Error.html").read_text()
                    error_code = 404
            elif resource == "/geneCalc":
                try:
                    # First things to do
                    line = list_resource[1]
                    tittle = "INFO OF A GENE"
                    sub_tittle = "The information of a human gene"
                    contents_in = html_folder(tittle, sub_tittle)
                    initial_index = line.find("=")
                    gene = line[initial_index + 1:]
                    # Getting the sequence
                    ext = "/xrefs/symbol/homo_sapiens/" + gene + "?"
                    id_gene = get_info(ext)
                    id_gene = id_gene[0]["id"]
                    s = get_sequence(id_gene)
                    # Using the Class
                    seq = Seq(s)
                    dict_sol = percentages(seq)
                    list_keys = list(dict_sol.keys())
                    list_values = list(dict_sol.values())
                    contents_in += f"The length of the gene is: {str(seq.len())} <br>Information about the bases<ul>"
                    # Viewing if it is json or not
                    if "json=1" in request_line:
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
                except requests.exceptions.HTTPError:
                    contents = Path("Error.html").read_text()
                    error_code = 404
            elif resource == "/geneList":
                try:
                    # First things to do
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
                    ext = "/overlap/region/human/" + chromosome + ":" + start + "-" + end + \
                          "?feature=gene;feature=transcript;feature=cds;feature=exon"
                    gene_list_ = get_info(ext)
                    contents_in += f"The genes in the range: {start} - {end} are: <br><br>"
                    # Viewing if it is json or not
                    if "json=1" in request_line:
                        list_keys = []
                        list_values = []
                        for n in gene_list_:
                            index = gene_list_.index(n)
                            list_keys.append(gene_list_[index]["id"])
                            if "external_name" in gene_list_[index]:
                                list_values.append(gene_list_[index]["external_name"])
                            else:
                                list_values.append("No name found")
                        contents = dict(zip(list_keys, list_values))
                    else:
                        for n in gene_list_:
                            index = gene_list_.index(n)
                            contents_in += f"""Gene: {gene_list_[index]["id"]}"""
                            if "external_name" in gene_list_[index]:
                                contents_in += f""" -->  {gene_list_[index]["external_name"]}<br>"""
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
        if "json=1" in request_line:
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
