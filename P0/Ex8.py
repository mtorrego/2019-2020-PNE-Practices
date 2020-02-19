from Seq0 import *
FOLDER = "../Session-04/"
list_names = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
bases = ["A", "C", "G", "T"]
ext = ".txt"
lista = []
for name in list_names:
    print("The most common base in ", name, "is :")
    x = seq_read_fasta(FOLDER + name + ext)
    y = seq_count(x)
    #print(y)
    #for keys, values in y.items():
    t = y.values()
    w = max(t)
    print(w)
        #maxx = ""
        #while keys > maxx:
         #   maxx = keys
          #  print(maxx)
        #print(y)
        #for keys, values in y: