from Seq1 import *
import socket
import termcolor

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

listsequences = ["AATTCCTACTGAACACTGGATGGGTGTACA", "GTGATACTAGATCACAACTTAGTCAGTCGT", "AAACCCTATGAGCTCGAGCTGATCGACATG",
                 "TTTACTTCGGATCACGATGCATAGTTACCA", "ACTTACGATCGTATCGACAAATCGTTTGCA"]
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
        n = msg.find(" ")
        command = msg[:n]
        termcolor.cprint(command, "green")
        sequence = msg[n + 1:]
        if msg == "PING":
            response = "OK!"
        elif "GET" in msg:
            chain = int(sequence)
            seq = listsequences[chain]
            response = seq
        elif "INFO" in msg:
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
        elif "COMP" in msg:
            s = Seq(sequence)
            response = s.seq_complement()
        elif "REV" in msg:
            s = Seq(sequence)
            response = s. seq_reverse()
        elif "GENE" in msg:
            s = Seq()
            response = s.read_fasta(FOLDER + sequence + ext)
        else:
            response = "ERROR"

        cs.send(response.encode())
        print(response, "\n")

        cs.close()
