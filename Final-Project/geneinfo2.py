import requests, sys

server = "http://rest.ensembl.org"
ext = "/lookup/symbol/homo_sapiens/BRCA2?"

r = requests.get(server + ext, headers={"Content-Type": "application/json"})

if not r.ok:
    r.raise_for_status()
    sys.exit()

decoded = r.json()
print(repr(decoded))