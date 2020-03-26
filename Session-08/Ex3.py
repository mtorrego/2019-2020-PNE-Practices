import socket

# SERVER IP, PORT
PORT = 8081
#IP = "192.168.124.179"
IP = "192.168.8.108"

while True:
  # -- Ask the user for the message
    message = input("Type the message you want to write: ")
  # -- Create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # -- Establish the connection to the Server
    s.connect((IP, PORT))
  # -- Send the user message
    s.send(str.encode(message))
  # -- Close the socket
    s.close()