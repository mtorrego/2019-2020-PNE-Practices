from Seq0 import *
FOLDER = "../Session-04/"
list_names = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
for name in list_names:
    print("The gene", name, "---> Length: ", seq_len(FOLDER + name + ".txt"))
