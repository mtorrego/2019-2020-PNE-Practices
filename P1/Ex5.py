from Seq1 import *
# -- Create a Null sequence
s1 = Seq()

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

#print("Sequence 1", s1)
#print("Sequence 2", s2)
#print("Sequence 3", s3)
seq_list = [s1, s2, s3]
print_seqs(seq_list)

