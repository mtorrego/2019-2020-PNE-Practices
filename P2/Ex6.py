from Client0 import Client
from Seq1 import *

PRACTICE = 2
EXERCISE = 6

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
a = s.read_fasta(FOLDER + "FRAT1" + ext)


def function(times):
    counter = 0
    word = ""
    number = int((times/10) + 1)
    while counter <= 5:
        for base in str(a[times:times + 10]):
            word += base
            counter += 1
    return "Fragment " + str(number) + ": " + word


c.debug_talk("Sending FRAT1 gene to the server in fragments of 10 bases")

listtimes = [0, 10, 20, 30, 40]
for time in listtimes:
    c.debug_talk(function(time))
