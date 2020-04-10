import termcolor

dict_genes = {"FRAT1": "ENSG00000165879",
            "ADA": "ENSG00000196839",
            "FXN": "ENSG00000165060",
            "RNU6_269P": "ENSG00000212379",
            "MIR633": "ENSG00000207552",
            "TTTY4C": "ENSG00000228296",
            "RBMY2YP": "ENSG00000227633",
            "FGFR3": "ENSG00000068078",
            "KDR": "ENSG00000128052",
            "ANK2": "ENSG00000145362"}
a = list(dict_genes.keys())
b = list(dict_genes.values())
print("Dictionary of genes!!")
print("There are ", len(a), "GENES in the dictionary")
sol = ""
for n in a:
    p = a.index(n)
    termcolor.cprint(n, "green", end="")
    print(" -->", str(b[p]))
