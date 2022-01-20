
def combination(n, m):
    return int(Factorial(n) / (Factorial(n - m) * Factorial(m)))

def Factorial(num):
    if num <= 0:
        return 1
    else:
        return Factorial(num - 1) * num
