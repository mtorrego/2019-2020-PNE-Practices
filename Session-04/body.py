from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "U5.txt"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

q = file_contents.split("\n")
file_contentss = q[1:]
e = "".join(file_contentss)
print(e)
#for i in e:
 #   print(i, end="")