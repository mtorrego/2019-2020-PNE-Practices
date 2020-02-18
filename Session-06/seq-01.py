class Seq:
    """A class for representing sequence objects"""
    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)

    pass


class Gene(Seq):
    pass


#----Main program
s1 = Seq("AACGTC")
g = Gene("ACCTGA")
print(f"Sequence 1 : {s1}")
print(f"Sequence 2 : {g}")
l1 = s1.len()
print(f"The length of the sequence 1 is {l1}")
print(f"The length of sequence 2 is {g.len()}")

print("Testing objects...")
