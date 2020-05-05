# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server
import http.client
import json
import termcolor

PORT = 8080
SERVER = 'localhost'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")


# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
# -- list_endpoints = ["/", "/listSpecies", "/karyotype", "/chromosomeLength",
# "/geneSeq", "/geneInfo", "/geneCalc", "/geneList"]
try:
    conn.request("GET", "/karyotype?specie=human&json=1")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")

# -- Print the received data
print(f"CONTENT: ")
print(data1)
function = json.loads(data1)
dict_itself = function["karyotype"]
print(dict_itself)
termcolor.cprint("  List of chromosomes {}:", 'blue')
for i, num in enumerate(dict_itself):
    termcolor.cprint("    Chromosome: ", 'red', end='')
    print(num)
