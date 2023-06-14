# solver22.py
#   Created on: 2023/06/14
#       Author: a_takeuchi
#  Chapter2-22
#  最短経路を探索

import math
row = [8, 6, 8, 9, 3, 4, 1, 7, 6, 1]
col = [5, 1, 1, 9, 1, 6, 9, 0, 9, 6]

dp = [[20] * 10 for i in range (10)]
map = [[0] * 10 for i in range (10)]

def main():
    print("map")
    for i in range (10):
        print(i, end='\t')
        for j in range (10):
            map[i][j] = row[i] + col[j]
            print(map[i][j], end=' ')
        print("")
    dp[0][0] = map[0][0]
    for i in range (1, 10):
        dp[0][i] = map[0][i] + dp[0][i-1]
        dp[i][0] = map[i][0] + dp[i-1][0]

    for i in range (1, 10):
        for j in range (1, 10):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + map[i][j]

    print("dp")
    for i in range (10):
        print(i, end='\t')
        for j in range (10):
            print(dp[i][j], end=' ')
        print("")


    print(dp[9][9])
    
if __name__ == "__main__":
    main()  

