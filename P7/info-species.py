def info_species():
    import requests, sys

    server = "https://rest.ensembl.org"
    ext = "/info/species?"

    r = requests.get(server + ext, headers={"Content-Type": "application/json"})

    if not r.ok:
        r.raise_for_status()
        sys.exit()

    decoded = r.json()
    # print(repr(decoded["species"][-1]["common_name"]))
    a = list(decoded["species"])
    counter = 0
    for n in a:
        print(a[counter]["common_name"])
        counter += 1


info_species()