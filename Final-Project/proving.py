a = "/geneList?chromo=9&start=23&end=45"
index_1 = a.find("=")
index_2 = a.find("&")
chromosome = a[index_1 + 1: index_2]
print(chromosome)
line = a[index_2:]
print(line)
index_3 = line.find("=")
index_4 = line.find("end")
start = line[index_3 + 1: index_4 - 1]
print(start)

listt = a.split("=")
print(listt)
x = ""
for n in listt:
    a = listt.index(n)
    for word in n:
        word = int(word)
        if word == int:
            x += str(word)
            print(x)
