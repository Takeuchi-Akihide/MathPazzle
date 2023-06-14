# solver19.py
#   Created on: 2023/06/12
#       Author: a_takeuchi
#  Chapter2-19
#  フック

import math
RUNNER = 50
HOOK = 35

memo = [[-1] * (HOOK+2) for i in range(RUNNER+2)]
memo[2][2] = 1
memo[3][2] = 1

def main():
    runner = RUNNER
    hook = HOOK
    result = 0
    isNecessary = True
    result = (calcHookPattern(runner, hook))

    print(result)

def calcHookPattern(runner, hook):
    if (memo[runner][hook] != -1):
        return memo[runner][hook]
    elif (hook <= 1 or runner < hook):
        return 0
    count = 0
    count += (calcHookPattern(runner-1, hook-1))
    count += (calcHookPattern(runner-2, hook-1))
    memo[runner][hook] = count
    return count
    
if __name__ == "__main__":
    main()  

