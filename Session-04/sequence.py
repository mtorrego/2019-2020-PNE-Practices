from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "ADA.txt"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()
content = file_contents.split("\n")[1:]
e = "".join(content)
print(len(e))