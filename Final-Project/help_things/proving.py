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
a = listt[1].find("&")
print(listt[1][:a])
b = listt[2].find("&")
print(listt[2][:b])
print(listt[3])