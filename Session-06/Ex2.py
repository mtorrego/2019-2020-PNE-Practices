class Seq:
    """A class for representing sequence objects"""
    def __init__(self, strbases):
        self.strbases = strbases

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)


class Gene(Seq):
    pass


def print_seqs(ls):
    index = -1
    for e in ls:
        index += 1
        print(f"Sequence : {index}, Length: ({e.len()}), {e}")


seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs(seq_list)
