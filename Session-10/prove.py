from Client0 import Client
# -- Parameters of the server to talk to
IP = "192.168.8.108"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
print(c)

while True:
    a = input("Type what do you want to write: ")
    response = c.talk(a)
    print(f"Response: \n{response}")
