#import requests, sys

#server = "https://rest.ensembl.org"
#ext = "/info/ping?"

#r = requests.get(server + ext, headers={"Content-Type": "application/json"})

#if not r.ok:
  #  r.raise_for_status()
   # sys.exit()

#decoded = r.json()
#print(repr(decoded))

import requests, sys

server = "https://rest.ensembl.org"
ext = "/sequence/id/ENSG00000157764?"

r = requests.get(server + ext, headers={"Content-Type": "text/plain"})

if not r.ok:
    r.raise_for_status()
    sys.exit()

print(r.text)