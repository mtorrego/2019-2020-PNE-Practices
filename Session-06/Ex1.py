class Seq:
    """A class for representing sequence objects"""
    def __init__(self, strbases):
        self.strbases = strbases
        if "A" and "C" and "G" and "T" in strbases:
            return "New sequence created!"
        else:
            return "ERROR"

    def __str__(self):
        if "A" and "C" and "G" and "T" in self.strbases:
            print("New sequence created!")
        else:
            print("ERROR")
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
