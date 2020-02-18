from pathlib import Path
def seq_ping():
    print("OK")

def seq_read_fasta(FILENAME):
    file_contents = Path(FILENAME).read_text()
    content = file_contents.split("\n")[1:]
    e = "".join(content)
    return e

def seq_len(seq):
    sequence = seq_read_fasta(seq)
    return len(sequence)

def seq_count_base(b):
    counter = 0
    for base in b:
        counter += 1
    return counter

