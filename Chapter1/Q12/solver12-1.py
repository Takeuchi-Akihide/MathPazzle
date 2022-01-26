# solver12-1.py
#   Created on: 2021/01/22
#       Author: a_takeuchi
#  Chapter1-12
#  円周率の近似

import math

def main():
    n = 11
    pi_n = math.floor(math.pi * (10 ** n)) / (10 ** n)
    flag = True
    bunbo = 0

    while flag:
        bunbo += 1
        # print(int(bunbo * pi_n))
        # print(int(bunbo * (pi_n + 1 / (10 ** n))))
        if int(bunbo * pi_n) < int(bunbo * (pi_n + 1 / (10 ** n))):
            bunshi = int(bunbo * (pi_n + 1 / (10 ** n)))
            flag = False
    
    print(bunbo)
    print(bunshi)
    print(bunshi / bunbo)
    
if __name__ == "__main__":
    main()  

