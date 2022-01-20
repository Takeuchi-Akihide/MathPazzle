# solver5-1.py
#   Created on: 2021/01/19
#       Author: a_takeuchi
#  Chapter1-5
#  お札の枚数で考えるパスカルの三角形

# from multiprocessing.context import SpawnContext

import sys
sys.path.append("../")
from common import combination

def main():
    print(calcBill(10101))
    n = 45
    count = 0
    result = calcPascal(n)
    for i in result:
        count += calcBill(i)

    print(result)
    print(count)

# num番目のパスカルの三角形の配列を返す
# def calcPascal(num):
#     row = [0] * (num + 1)
#     row[0] = 1
#     for i in range(num+1):
#         for j in range(i)[::-1]:
#             row[j+1] += row[j]
#         # result.append(combination(num, i))
#     return row

def calcPascal(num):
    result = []
    for i in range(num+1):
        result.append(combination(num, i))
    return result

def calcBill(num):
    Bills = [10000, 5000, 2000, 1000, 500, 100, 50, 10, 5, 1]
    place = 0
    count = 0
    while (num > 0):
        if num >= Bills[place]:
            num -= Bills[place]
            count += 1
        else:
            place += 1
    return count
    
if __name__ == "__main__":
    main()  

