import http.client
import json
import termcolor

SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id"
PARAMS = "/ENSG00000207552?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMS

print()
print(f"Server: {SERVER}")
print(f"URL: {URL}")

#Connect with the server
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

# -- Create a variable with the data,
# -- form the JSON received
name = "MIR633"
ex3 = json.loads(data1)
#print(ex1)
termcolor.cprint("Gene: ", "green", end="")
print(name)
termcolor.cprint("Description: ", "green", end="")
print(ex3["desc"])
termcolor.cprint("Bases: ", "green", end="")
print(ex3["seq"])

