import requests, sys

server = "http://rest.ensembl.org"
ext = "/lookup/symbol/homo_sapiens/FRAT1?"

r = requests.get(server + ext, headers={"Content-Type": "application/json"})

if not r.ok:
    r.raise_for_status()
    sys.exit()

decoded = r.json()
print(decoded)
A = decoded["start"]
B = decoded["end"]
print(A)
print(B)
print(B-A)
print(decoded["seq_region_name"])
print(decoded["id"])