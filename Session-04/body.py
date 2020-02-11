from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "U5.txt"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

file_contents.split("\n")[1:]
for i in file_contents:
    print(i)