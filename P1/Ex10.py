from Seq1 import *
FOLDER = "../Session-04/"
list_names = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
bases = ["A", "C", "G", "T"]
ext = ".txt"

for name in list_names:
    s = Seq()
    a = s.read_fasta(FOLDER + name + ext)
    sequence = Seq(a)
    print("The most common base in ", name, "is :", ex10(sequence))

