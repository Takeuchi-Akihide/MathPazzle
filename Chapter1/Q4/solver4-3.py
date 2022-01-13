# solver4-3.py
#   Created on: 2021/01/14
#       Author: a_takeuchi
#  Chapter1-4
#  点灯している量で考えるデジタル時計

digitalNum = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
HOUR_MAX = 24
MINUTE_MAX = 60
SECOND_MAX = 60

def main():
    Charalist = []      # 点灯量を入れる配列
    Digitallist = []
    resultNum = 30

    for s in range(SECOND_MAX):
        Digitallist.append(calc_digitalNum(s))

    for h in range(HOUR_MAX):
        for m in range(MINUTE_MAX):
            for s in range(SECOND_MAX):
                count = Digitallist[h] + Digitallist[m] + Digitallist[s]
                while (len(Charalist) < count):
                    Charalist.append(0)
                Charalist[count-1] += 1

    print(Charalist)
    print(Charalist[resultNum-1])

def calc_digitalNum(num):
    num0 = int(num / 10)
    num1 = int(num % 10)
    return digitalNum[num0] + digitalNum[num1]
    
if __name__ == "__main__":
    main()  

