from pathlib import Path

# -- Constant with the new of the info to open
FILENAME = "U5.txt"

# -- Open and read the info
file_contents = Path(FILENAME).read_text()

content = file_contents.split("\n")[1:]
e = "".join(content)
print(e)
