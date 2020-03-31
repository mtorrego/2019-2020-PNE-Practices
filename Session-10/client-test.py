from Client0 import Client

IP = "192.168.8.108"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
print(c)

counter = 0
while counter < 5:
    c.debug_talk(f"Message {counter}")
    counter += 1
