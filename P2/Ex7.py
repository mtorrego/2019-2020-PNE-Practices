from Client0 import Client
from Seq1 import *

PRACTICE = 2
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "192.168.8.108"
PORT1 = 8080
PORT2 = 8081
# -- Create a client object
c = Client(IP, PORT1)
c1 = Client(IP, PORT2)
print(c)
print(c1)

# -- Create a Null sequence
s = Seq()

# -- Initialize the null seq with the given file in fasta format
FOLDER = "../Session-04/"
list_names = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
ext = ".txt"
a = s.read_fasta(FOLDER + "FRAT1" + ext)
#sequence = Seq(a)


def function(times):
    counter = 0
    word = ""
    number = int((times/10) + 1)
    while counter <= 10:
        for base in str(a[times:times + 10]):
            word += base
            counter += 1
    return "Fragment " + str(number) + ": " + word


listtimes = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print("Gene FRAT1: ", a)
for time in listtimes:
    print(function(time))


listtimes1 = [10, 30, 50, 70, 90]
for time in listtimes1:
    c.talk(function(time))
listtimes2 = [0, 20, 40, 60, 80]
for time in listtimes2:
    c1.talk(function(time))




