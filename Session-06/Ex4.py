import termcolor


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


def print_seqs(ls, color):
    index = -1
    for e in ls:
        index += 1
        termcolor.cprint(f"Sequence : {index}, Length: ({e.len()}), {e}", color)


def generate_seqs(pattern, number):
    lista = []
    for e in range(1, number + 1):
        sequence = pattern*e
        lista.append(Seq(sequence))
    return lista


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

termcolor.cprint("List 1:", "green")
print_seqs(seq_list1, "green")


print()
termcolor.cprint("List 2:", "blue")
print_seqs(seq_list2, "blue")
