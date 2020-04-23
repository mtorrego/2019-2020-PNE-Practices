from Seq0 import *
FOLDER = "../Session-04/"
filename = "U5"
ext = ".txt"
x = seq_read_fasta(FOLDER + filename + ext)
x20 = x[:20]
print(x20)
print(seq_complement(x20))
