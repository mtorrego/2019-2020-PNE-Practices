def fibon(n):
    counter = 0
    x = 0
    y = 1
    while counter < n:
        new = x + y
        x = y
        y = new
        counter += 1
    return x


print("The 5th Fibonacci term is:", fibon(5))
print("The 10th Fibonacci term is:", fibon(10))
print("The 15th Fibonacci term is:", fibon(15))
