# solver20.py
#   Created on: 2023/06/12
#       Author: a_takeuchi
#  Chapter2-20
#  帰り道

import math
STATION = 15
START = 3
GOAL = 10

def main():
    if (START > GOAL):
        goal = STATION - START
        start = STATION - GOAL
    else:
        goal = GOAL
        start = START
    afterGoal = STATION - goal
    beforeGoal = goal - 2

    product = 1
    result = product + calc(afterGoal, beforeGoal, 1, product)

    print(result)

def calc(after, before, now, product):
    count = 0
    if (after < 0 or before < 0):
        return count

    if (now == 1):
        count = product * after
        return count + calc(after-1, before, -1, count)
    else:
        count = product * before
        return count + calc(after, before-1, 1, count)
    
if __name__ == "__main__":
    main()  

