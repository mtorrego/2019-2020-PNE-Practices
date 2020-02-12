def seq_ping():
    print("OK")

def seq_read_fasta(FILENAME):
    from pathlib import Path
    file_contents = Path(FILENAME).read_text()
    file_contents.split("\n")
    return file_contents
