class Seq:
    """A class for representing sequence objects"""
    def __init__(self, strbases):
        #self.strbases = strbases
        #print(self.strbases)
        bases = ["A", "C", "G", "T"]
        for base in strbases:
            if base not in bases:
                self.strbases = "ERROR"
                print(self.strbases)
                return
            else:
                print("New sequence created!")
                self.strbases = strbases
                return

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)

    pass


class Gene(Seq):
    pass

s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
