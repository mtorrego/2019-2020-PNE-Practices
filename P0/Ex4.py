from Seq0 import *
FOLDER = "../Session-04/"
list_names = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
bases = ["A", "C", "G", "T"]
ext = ".txt"
seq1 = "AAACTG"

#for b in ["A", "C", "G", "T"]:
 #   print(seq_count_base(seq1, b))

#for seq1 in ["ATCC", "AT"]:
 #   print(seq1, ":")
  #  for b in ["A", "C", "G", "T"]:
   #     print(seq_count_base(seq1, b))
for name in list_names:
    print(name, ":")
    for base in bases:
        x = seq_read_fasta(FOLDER + name + ext)
        print(seq_count_base(x, base))

