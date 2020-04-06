from Seq0 import *
filename = "U5.txt"
FOLDER = "../Session-04/"
print("DNA info: ", filename)
print("The first 20 bases are: ", seq_read_fasta(FOLDER + filename)[:20])
