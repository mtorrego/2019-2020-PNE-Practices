from Client0 import Client

IP = "127.0.0.1"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
print(c)
while True:
    a = input("Type what you want to analise: ")
    c.debug_talk(a)