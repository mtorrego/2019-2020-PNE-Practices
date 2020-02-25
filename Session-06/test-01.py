from Seq0 import *

seq1 = "ATTCCCGGGG"

#seq_check(seq1) #habria que crear una funcion nueva para chequear si solo tiene esas bases

print(f"Seq:    {seq1}")
print(f"  Rev : {seq_reverse(seq1)}")
print(f"  Comp: {seq_complement(seq1)}")
print(f"  Length: {seq_len(seq1)}")
print(f"    A: {seq_count_base(seq1, 'A')}")
print(f"    T: {seq_count_base(seq1, 'T')}")
print(f"    C: {seq_count_base(seq1, 'C')}")
print(f"    G: {seq_count_base(seq1, 'G')}")
