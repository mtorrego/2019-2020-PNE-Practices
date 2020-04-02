from Seq1 import *
from Client0 import *
import socket
import termcolor
from Seq0 import *

IP = "127.0.0.1"
PORT = 8080

# --- Step 1: creating the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# --- Step 2: Bind the socket to the server's IP and PORT
ls.bind((IP, PORT))

# --- Step 3: Convert into a listening socket
ls.listen()

print("Server is configured!!")

FOLDER = "../Session-04/"
list_names = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
ext = ".txt"

aa = True
while aa:
    print("Waiting for Clients to connect")
    try:
        # --- Step 4: Wait for clients tro connect
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server is done!")
        ls.close()
        exit()
    else:
        msg_raw = cs.recv(2000)
        msg = msg_raw.decode()
        termcolor.cprint(msg, "green")
        if msg == "PING":
            response = "OK!"
        elif "GET" in msg:
            number = msg.find(" ")
            chain = int(msg[number + 1:])
            seq = list_names[chain]
            response = seq_read_fasta(FOLDER + seq + ext)
        elif "INFO" in msg:
            n = msg.find(" ")
            sequence = msg[n + 1:]
            s = Seq(sequence)
            a = s.count()
            b = s.len()
            listvalues = list(a.values())
            listt = []
            for value in listvalues:
                listt.append(f"{value} {round(value/b * 100), 2}%")
            listkeys = list(a.keys())
            d = dict(zip(listkeys, listt))

            response = f"Sequence: {s} \nThe length is: {b} \n{d}"


        cs.send(response.encode())
        print(response)

        cs.close()
