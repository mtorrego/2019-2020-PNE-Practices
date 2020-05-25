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
    conn.request("GET", "/geneList?chromo=4&start=42222&end=422233&json=1")
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
key_word = function["List"]

# This is the example for the last endpoint
termcolor.cprint("List of the genes in the range 42222-422233 of the chromosome 4: ", 'blue')
list_keys = list(key_word.keys())
list_values = list(key_word.values())
for key in list_keys:
    index = list_keys.index(key)
    print(list_keys[index] + " --> " + list_values[index])
