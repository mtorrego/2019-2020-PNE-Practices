
def sumn(n):
    res = 0
    for i in range(1, n + 1):
        res += i
    return res


print("Total sum of 1-20 is: ", sumn(20))
print("Total sum of 1-100 is: ", sumn(100))
