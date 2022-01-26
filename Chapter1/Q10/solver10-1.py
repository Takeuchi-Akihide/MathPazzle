# solver10-1.py
#   Created on: 2021/01/22
#       Author: a_takeuchi
#  Chapter1-10
#  アダムズ方式

import math

def main():
    PopulationList = [5381733, 
                      1308265,
                      1279594,
                      2333899,
                      1023119,
                      1123891,
                      1914039,
                      2916976,
                      1974255,
                      1973115,
                      7266534,
                      6222666,
                      13515271,
                      9126214,
                      2304264,
                      1066328,
                      1154008,
                      786740,
                      834930,
                      2098804,
                      2031903,
                      3700305,
                      7483128,
                      1815865,
                      1412916,
                      2610353,
                      8839469,
                      5534800,
                      1364316,
                      963579,
                      573441,
                      694352,
                      1921525,
                      2843990,
                      1404729,
                      755733,
                      976263,
                      1385262,
                      728276,
                      5101556,
                      832832,
                      1377187,
                      1786170,
                      1166338,
                      1104069,
                      1648177,
                      1433566,  ]
    flag = True
    prefecture = len(PopulationList)
    result = [0] * prefecture
    giseki = 289
    Min = 1
    Max = max(PopulationList)
    Integer = int((Min + Max) / 2)
    print(prefecture)

    while flag:
        count = 0
        for i in range(prefecture):
            result[i] = math.ceil(PopulationList[i] / Integer)
            count += result[i]
        print(count)
        # flag = False
        if count > giseki:
            Min = Integer
            # Integer = int((Integer + Max) / 2)
        elif count < giseki:
            Max = Integer
            # Integer = int((Integer + Min) / 2)
        else:
            flag = False
        Integer = int((Min + Max) / 2)
    
    print(Integer)
    print(result)

    
if __name__ == "__main__":
    main()  

