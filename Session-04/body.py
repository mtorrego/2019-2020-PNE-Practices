from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "U5.txt"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

x = file_contents.split("\n")
e = x[1:]
for i in e:
    print(i, end="")