# renbunsu.py
#   Created on: 2021/01/22
#       Author: a_takeuchi
#  Chapter1-12の類題
#  連分数を求めるプログラム

import math

def main():
    n = 1000000
    x_a = calc_pi_a(n+1)
    x_b = calc_pi_b(n+1)

    for i in range(n):
        x_a[n-i-1] += x_b[n-i] / x_a[n-i]

    print(x_a[0])

def calc_pi_a(n):
    x_a = []
    x_a.append(3)
    for i in range(n-1):
        x_a.append(6)
    return x_a
    
def calc_pi_b(n):
    x_b = []
    x_b.append(0)
    for i in range(n-1):
        x_b.append((i*2+1) ** 2)
    return x_b

if __name__ == "__main__":
    main()  

