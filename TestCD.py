def gcd(x, y):
    (y, x) = (x, y) if x > y else (x, y)
    for i in range(x, 0, -1):
        if (x % i == 0 and y % i == 0):
           return i

result = gcd(12, 4)
print(result)