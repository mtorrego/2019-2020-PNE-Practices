from Client0 import Client
from Seq1 import *

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "192.168.8.108"
PORT = 8081

# -- Create a client object
c = Client(IP, PORT)
print(c)

# -- Create a Null sequence
s = Seq()

# -- Initialize the null seq with the given info in fasta format
FOLDER = "../Session-04/"
list_names = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
ext = ".txt"
a = s.read_fasta(FOLDER + "U5" + ext)
sequence = Seq(a)

c.debug_talk("Sending U5 gene to the server...")
c.debug_talk(str(sequence))
