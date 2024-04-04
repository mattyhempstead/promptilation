from math import isqrt

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

N = int(input("Enter a number: "))

for num in range(2, N + 1):
    if is_prime(num):
        print(num)
