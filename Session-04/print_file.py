from pathlib import Path

# -- Constant with the new of the info to open
FILENAME = "RNU6_269P.txt"

# -- Open and read the info
file_contents = Path(FILENAME).read_text()

# -- Print the contents on the console
print(file_contents)