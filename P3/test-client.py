from Client0 import Client

IP = "127.0.0.1"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
print(c)

# TEST PING
print("* Testing PING...")
print(c.talk("PING"))

# TEST GET
print("* Testing GET...")
for n in range(0,5):
    print("Gene", n, c.talk(f"GET {n}"))

sequence = c.talk("GET 0")
# TEST INFO
print("* Testing INFO...")
print(c.talk("INFO " + sequence))

# TEST COMP
print("* Testing COMP...")
print("COMP " + sequence)
print(c.talk("COMP " + sequence))

# TEST REV
print("* Testing REV...")
print("REV " + sequence)
print(c.talk("REV " + sequence))

# TEST GENE
print("* Testing GENE...")
list_names = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
for file in list_names:
    print("GENE", file)
    print(c.talk("GENE " + file))
