from Seq1 import *
# -- Create a Null sequence
s = Seq()

# -- Initialize the null seq with the given info in fasta format
FOLDER = "../Session-04/"
list_names = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
ext = ".txt"
a = s.read_fasta(FOLDER + "U5" + ext)
sequence = Seq(a)
print_seqs2(sequence)
