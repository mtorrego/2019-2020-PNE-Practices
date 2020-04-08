dictt = {"A": "HOLA", "B": "JAJA"}
keyslist = list(dictt.keys())
valueslist = list(dictt.values())
print(keyslist)
sol = ""
for n in keyslist:
    a = keyslist.index(n)
    sol = sol + "\n"+ keyslist[a] + " " + valueslist[a]
print(sol)

