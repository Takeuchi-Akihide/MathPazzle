# solver3-1.py
#   Created on: 2021/01/13
#       Author: a_takeuchi
#  Chapter1-3
#  ローマ数字の変換規則

def main():
    resultNum = 12        # 記号の種類
    NumMax   = 3999     # 数値の最大値
    Charalist = []      # 使う記号の数を入れる配列
    tmpNum = 0

    for i in range(1, NumMax+1):
        digit = calcDigit(i)
        for j in range(digit):
            value1 = (i / 10**j) % 10
            if value1 == 4 or value1 == 5:
                tmpNum -= 1
            elif value1 == 0 or value1 == 9:
                tmpNum -= 2
            else:
                tmpNum += 1
            if value1 != 0:
                break
        while (len(Charalist) < tmpNum):
            Charalist.append(0)
        Charalist[tmpNum-1] += 1
    print(Charalist)
    print(Charalist[resultNum-1])

def calcDigit(num):
    digit = 0
    while(num > 0):
        digit += 1
        num /= 10
    return digit


if __name__ == "__main__":
    main()  