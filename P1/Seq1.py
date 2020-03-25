from pathlib import Path
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

    def count(self):
        result = {"A": self.count_base("A"), "C": self.count_base("C"),
                  "G": self.count_base("G"), "T": self.count_base("T")}
        return result

    def seq_reverse(self):
        if not self.len():
            return self.strbases
        else:
            inverse = self.strbases[::-1]
            return inverse

    def seq_complement(self):
        if not self.len():
            return self.strbases
        else:
            complement_dictionary = {"A": "T", "C": "G", "G": "C", "T": "A"}
            new_list = ""
            for n in self.strbases:
                a = complement_dictionary[n]
                new_list = new_list + a
            return new_list

    def seq_read_fasta(self):
        file_contents = Path(self.strbases).read_text()
        content = file_contents.split("\n")[1:]
        e = "".join(content)
        return e

    pass


def print_seqs(ls):
    index = 0
    listbases = ["A", "C", "G", "T"]
    for e in ls:
        index += 1
        print(f"Sequence : {index}, Length: ({e.len()}), {e}")
        for base in listbases:
            print(f"Base : {base} : {e.count_base(base)} ")


def print_seqs1(ls):
    index = 0
    for e in ls:
        index += 1
        print(f"Sequence : {index}, Length: ({e.len()}), {e}")
        print(f" Bases : {e.count()}")
        print(f" Reverse : {e.seq_reverse()}")
        print(f" Complement: {e.seq_complement()}")


def generate_seqs(pattern, number):
    lista = []
    for e in range(1, number + 1):
        sequence = pattern*e
        lista.append(Seq(sequence))
    return lista
