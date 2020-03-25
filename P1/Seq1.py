class Seq:
    """A class for representing sequence objects"""
    def __init__(self, strbases="NULL"):
        if strbases == "NULL":
            print("Null sequence created")
            self.strbases = strbases
            self.length = 0
            return
        else:
            bases = ["A", "C", "G", "T"]
            for base in strbases:
                if base not in bases:
                    print("INVALID seq created")
                    self.strbases = "ERROR"
                    self.length = 0
                    return
                else:
                    print("New sequence created!")
                    self.strbases = strbases
                    self.length = len(self.strbases)
                    return

    def __str__(self):
        return self.strbases

    def len(self):
        return self.length

    def count_base(self, base):
        return self.strbases.count(base)

    pass


def print_seqs(ls):
    index = 0
    listbases = ["A", "C", "G", "T"]
    for e in ls:
        index += 1
        print(f"Sequence : {index}, Length: ({e.len()}), {e}")
        for base in listbases:
            print(f"Base : {base} : {e.count_base(base)} ")


def generate_seqs(pattern, number):
    lista = []
    for e in range(1, number + 1):
        sequence = pattern*e
        lista.append(Seq(sequence))
    return lista
