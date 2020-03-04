class Seq:
    """A class for representing sequence objects"""
    def __init__(self, strbases):
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


def print_seqs(ls):
    index = 0
    for e in ls:
        index += 1
        print(f"Sequence : {index}, Length: ({len(e)}), {e}")


def generate_seqs(pattern, number):
    lista = []
    for e in range(1, number + 1):
        sequence = pattern*e
        lista.append(Seq(sequence))
    return lista
