from Seq0 import *
FOLDER = "../Session-04/"
list_names = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
bases = ["A", "C", "G", "T"]
ext = ".txt"
seq1 = "AAACTG"

for name in list_names:
    print(name, ":")
    for base in bases:
        x = seq_read_fasta(FOLDER + name + ext)
        print(seq_count_base(x, base))
