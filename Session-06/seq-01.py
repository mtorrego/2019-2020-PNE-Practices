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
    def __init__(self, strbases, name=""):
        # -- Call first the Seq initilizer and then the
        # -- Gene init method
        super().__init__(strbases)
        self.name = name
        print("New gene created")

    def __str__(self):
        """Print the Gene name along with the sequence"""
        return self.name + "-" + self.strbases
    pass


s1 = Seq("AGTACACTGGT")
g = Gene("CGTAAC", "FRAT1")
print(f"Sequence 1 : {s1}")
l1 = s1.len()
print(f"    The length of the sequence 1 is {l1}")
print(f"Gene: {g}")
