import requests, sys

server = "http://rest.ensembl.org"
ext = "/overlap/region/human/5:140424943-140624564?feature=gene;feature=transcript;feature=cds;feature=exon"

r = requests.get(server + ext, headers={"Content-Type": "application/json"})

if not r.ok:
    r.raise_for_status()
    sys.exit()

decoded = r.json()
print(repr(decoded))

