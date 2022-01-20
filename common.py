
from unittest import result


def combination(n, m):
    return int(Factorial(n) / (Factorial(n - m) * Factorial(m)))

def Permutation(n, m):
    result = 1
    for i in range(m):
        result *= (n - i)
    return result

def Factorial(num):
    if num <= 0:
        return 1
    else:
        return Factorial(num - 1) * num
