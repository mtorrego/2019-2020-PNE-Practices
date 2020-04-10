import http.client
import json

SERVER = "rest.ensembl.org"
ENDPOINT = "/info/ping"
PARAMS = "?content-type=application/json"
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
print(data1)
# -- Create a variable with the data,
# -- form the JSON received
ex1 = json.loads(data1)
print(ex1)
ping = ex1['ping']
print(ping)

if ping == 1:
    print("PING OK! The database is running!")
else:
    print("KA")