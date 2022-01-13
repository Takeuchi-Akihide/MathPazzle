# solver4-1.py
#   Created on: 2021/01/14
#       Author: a_takeuchi
#  Chapter1-4
#  点灯している量で考えるデジタル時計

def main():
    digitalNum = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    maxNum = 24 * 60 * 60
    Charalist = []      # 点灯量を入れる配列
    # tmpNum = digitalNum[0] * 6
    resultNum = 30

    for i in range(maxNum):
        time = calcTime(i)
        count = 0
        for j in range(len(time)):
            count += digitalNum[time[j]]
        
        while (len(Charalist) < count):
            Charalist.append(0)
        Charalist[count-1] += 1

    print(Charalist)
    print(Charalist[resultNum-1])

def calcTime(sec):
    second = sec % 60
    minute = ((sec - second) / 60) % 60
    hour = ((sec - second) / 60) / 60
    hour0 = int(hour / 10)
    hour1 = int(hour % 10)
    minute0 = int(minute / 10)
    minute1 = int(minute % 10)
    second0 = int(second / 10)
    second1 = int(second % 10)
    return [hour0, hour1, minute0, minute1, second0, second1]

    
if __name__ == "__main__":
    main()  

