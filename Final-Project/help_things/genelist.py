import requests, sys

server = "http://rest.ensembl.org"
ext = "/overlap/region/human/2:12313-123445?feature=gene;feature=transcript;feature=cds;feature=exon"

r = requests.get(server + ext, headers={"Content-Type": "application/json"})

if not r.ok:
    r.raise_for_status()
    sys.exit()

decoded = r.json()
print(decoded)
for n in decoded:
    a = decoded.index(n)
    print(decoded[a]["id"], end="")
    if "external_name" in decoded[a]:
        print("-->" + decoded[a]["external_name"])
    else:
        print("")

