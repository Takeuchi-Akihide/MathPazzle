# solver6-1.py
#   Created on: 2021/01/19
#       Author: a_takeuchi
#  Chapter1-6
#  長方形から作る正方形

def main():
    maxL = 1000
    square = 20
    count = 0
    for l in range(maxL):
        for s in range(l):
            result = calcSquare(l+1, s+1)
            if result == square:
                count += 1

    print(count)

def calcSquare(a, b):
    if a >= b:
        long = a
        short = b
    else:
        long = b
        short = a
    count = int(long / short)
    rem = long % short
    if rem != 0:
        count += calcSquare(short, rem)
    return count
    
if __name__ == "__main__":
    main()  

