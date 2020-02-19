from pathlib import Path


def seq_ping():
    print("OK")


def seq_read_fasta(filename):
    file_contents = Path(filename).read_text()
    content = file_contents.split("\n")[1:]
    e = "".join(content)
    return e


def seq_len(seq):
    sequence = seq_read_fasta(seq)
    return len(sequence)


def seq_count_base(sequence, base):
    return sequence.count(base)


def seq_count(sequence):
    result = {"A": seq_count_base(sequence, "A"), "C": seq_count_base(sequence, "C"), "G": seq_count_base(sequence, "G"), "T": seq_count_base(sequence, "T")}
    return result


def seq_reverse(sequence):
    cadenaInvertida = sequence[::-1]
    return cadenaInvertida


def seq_complement(seq):
    complement_dictionary = {"A": "T", "C": "G", "G": "C", "T": "A"}
    new_list = ""
    for n in seq:
        a = complement_dictionary[n]
        new_list = new_list + a
    return new_list

#def ex8(seq):


