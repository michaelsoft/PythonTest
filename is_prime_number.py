def is_prime_number(x):
    for i in range(x-1, 1, -1):
        if (x % i == 0):
            return False
    return True

result = is_prime_number(1)
print(result)