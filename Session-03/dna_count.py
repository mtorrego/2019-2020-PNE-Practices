chain = input("Type a correct chain of DNA")
#if "A" or "C" or "T" or "G" not in chain:
    #print("Wrong chain")
#else:
counter = 0
for letter in chain:
    counter += 1
print("Total length", counter)
counter_A = 0
counter_C = 0
counter_G = 0
counter_T = 0
for letter in chain:
    if letter == "A":
        counter_A += 1
    if letter == "G":
        counter_G += 1
    if letter == "C":
        counter_C += 1
    if letter == "T":
        counter_T += 1
print("Counter A: ", counter_A, "\nCounter G: ", counter_G, "\nCounter C: ", counter_C, "\nCounter T: ", counter_T)
