def fibosum(n):
    counter = 0
    summ = 0
    x = 0
    y = 1
    while counter < n:
        new = x + y
        x = y
        y = new
        summ += x
        counter += 1
    return summ


print("The 5th Fibonacci terms is:", fibosum(5))
print("The 10th Fibonacci terms is:", fibosum(10))
