# solver2.py
#   Created on: 2021/01/12
#       Author: a_takeuchi
#  Chapter1-2
#  山手線でスタンプラリー

import sys
sys.path.append("../")
from common import combination

def main():
    N = 29      # 駅の数
    S = 1       # 乗る駅の番号
    E = 17      # 降りる駅の番号
    count = 0

    # 降りる駅の数(2通り)
    S1 = abs(S-E) - 1
    S2 = N - S1 - 2
    
    # 右回りの場合
    for i in range(S1 + 1):
        # 降りる回数(0からK-2)ごとにカウントアップ
        count += combination(S1, i)
    # 左回りの場合
    for i in range(S2 + 1):
        count += combination(S2, i)
    # 1回も下りない場合が重複しているため1引く
    count -= 1
    print(int(count))


# def combination(n, m):
#     return Factorial(n) / (Factorial(n - m) * Factorial(m))

# def Factorial(num):
#     if num <= 0:
#         return 1
#     else:
#         return Factorial(num - 1) * num



if __name__ == "__main__":
    main()  