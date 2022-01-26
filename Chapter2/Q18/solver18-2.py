# solver18-2.py
#   Created on: 2021/01/26
#       Author: a_takeuchi
#  Chapter2-18
#  非常階段での脱出。メモ化

import math

memo = {0:0, 1:1}

def main():
    n = 16
    result = 0

    for i in range(2 ** n):
    # pattern = 0xFF00
        result += calcMoveNum(n, i)

    print(result)

def calcMoveNum(n, pattern):
    # count = 0
    if pattern in memo.keys():
        return memo[pattern]

    newPattern = 0
    for i in range(n):
        if i == 0:
            pass
        elif pattern & (1 << i):
            if pattern & (1 << (i-1)):
                newPattern += (1 << i)
            else:
                newPattern += (1 << (i-1))
    memo[pattern] = calcMoveNum(n, newPattern) + 1
    return memo[pattern]
    
if __name__ == "__main__":
    main()  

