import socket
import termcolor

IP = "192.168.8.108"
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
number_con = 0

while True:
    print("Waiting for Clients to connect")
    try:
        # --- Step 4: Wait for clients tro connect
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server is done!")
        ls.close()
        exit()
    else:
        number_con += 1
        print("CONNECTION: {}. From the IP: {}".format(number_con, client_ip_port))

        # --- Step 5: Receiving information from the client
        msg_raw = cs.recv(2000)
        msg = msg_raw.decode()

        print(f" Received message: ", end="")
        termcolor.cprint(msg, "green")

        # --- Step 6: Send a response message to the client
        response = "ECHO: " + msg
        cs.send(response.encode())

        cs.close()
