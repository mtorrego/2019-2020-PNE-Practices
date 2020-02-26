from Seq0 import *
FOLDER = "../Session-04/"
list_names = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
bases = ["A", "C", "G", "T"]
ext = ".txt"
lista = []
lista2 = []
for name in list_names:
    x = seq_read_fasta(FOLDER + name + ext)
    y = seq_count(x)
    t = y.values()
    lista = list(t)
    a = max(lista)
    s = lista.index(a)
    r = y.keys()
    lista2 = list(r)
    solucion = lista2[s]
    print("The most common base in ", name, "is :", solucion)
