# solver21.py
#   Created on: 2023/06/13
#       Author: a_takeuchi
#  Chapter2-21
#  本を読むパターン

import math
PAGE = 180
MAX = 14

memo = [[[-1] * (MAX+2) for j in range (PAGE+2)] for i in range(PAGE+2)]

def main():
    result = calc(PAGE, PAGE+1, MAX)

    print(result)

def calc(page, prev, date):
    count = 0
    if (page == 0):
        memo[page][prev][date] = 1
        return 1
    if (page < 0 or date < 0 or page > prev * date):
        return count

    if (memo[page][prev][date] != -1):
        return memo[page][prev][date]
    
    for i in range (prev):
        count += calc(page-i, i, date-1)
    
    memo[page][prev][date] = count
    return count
    
if __name__ == "__main__":
    main()  

