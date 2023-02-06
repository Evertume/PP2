import math
def filter_prime(a):
    return list(filter(lambda x : is_prime(x), a))
def is_prime(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True
print(filter_prime(input()))