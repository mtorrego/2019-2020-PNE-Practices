from Seq1 import Seq
# -- Create a Null sequence
s = Seq()

# -- Initialize the null seq with the given file in fasta format
FOLDER = "../Session-04/"
list_names = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
ext = ".txt"
s.read_fasta(FOLDER + "U5" + ext)
print_seqs()