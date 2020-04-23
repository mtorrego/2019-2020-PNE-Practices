import http.client
import json
import termcolor
from Seq1 import *


def percentages(seq):
    count = seq.count()
    length = seq.len()
    listvalues = list(count.values())
    listt = []
    for value in listvalues:
        listt.append(f"{value} {round(value / length * 100), 2}%")
    listkeys = list(count.keys())
    for n in listkeys:
        n_index = listkeys.index(n)
        termcolor.cprint(n, "blue", end="")
        print(" -->", str(listt[n_index]))


dict_genes = {"FRAT1": "ENSG00000165879",
              "ADA": "ENSG00000196839",
              "FXN": "ENSG00000165060",
              "RNU6_269P": "ENSG00000212379",
              "MIR633": "ENSG00000207552",
              "TTTY4C": "ENSG00000228296",
              "RBMY2YP": "ENSG00000227633",
              "FGFR3": "ENSG00000068078",
              "KDR": "ENSG00000128052",
              "ANK2": "ENSG00000145362"}

gene = input("What gene do you want to analyze?: ")
a = list(dict_genes.keys())
b = list(dict_genes.values())
phrase = dict_genes[gene]

SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id"
PARAMS = "/" + phrase + "?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMS

print()
print(f"Server: {SERVER}")
print(f"URL: {URL}")

conn = http.client.HTTPConnection(SERVER)

try:
    conn.request("GET", ENDPOINT + PARAMS)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
response = conn.getresponse()

# -- Print the status line
print(f"Response received!: {response.status} {response.reason}\n")

# -- Read the response's body
data1 = response.read().decode("utf-8")

ex4 = json.loads(data1)

termcolor.cprint("Gene: ", "green", end="")
print(gene)
termcolor.cprint("Description: ", "green", end="")
print(ex4["desc"])
sequence = ex4["seq"]
s = Seq(sequence)
termcolor.cprint("Total length: ", "green", end="")
print(s.len())
percentages(s)
termcolor.cprint("Most frequent base: ", "green", end="")
print(ex10(s))
