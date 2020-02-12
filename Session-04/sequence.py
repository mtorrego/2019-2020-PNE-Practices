from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "ADA.txt"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

# -- Print the contents on the console
counter = 0
x = file_contents.split("\n")
e = x[1:]
for i in e:
    counter += 1
print(counter)