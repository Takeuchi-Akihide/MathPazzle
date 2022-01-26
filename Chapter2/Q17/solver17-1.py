# solver17-1.py
#   Created on: 2021/01/26
#       Author: a_takeuchi
#  Chapter2-17
#  グループで乗るリフト

import math

memo = {0:1, 1:1}

def main():
    n = 32
    m = 6

    result = calcPattern(n, m)
    print(result)

def calcPattern(n, m):
    result = 0
    if n in memo.keys():
        return memo[n]
    for i in range(min(n, m)):
        crew = i + 1
        result += calcPattern(n-crew, m)
    
    memo[n] = result
    print(memo)
    return result

    
if __name__ == "__main__":
    main()  

