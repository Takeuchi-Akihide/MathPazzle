# solver7-1.py
#   Created on: 2021/01/19
#       Author: a_takeuchi
#  Chapter1-7
#  ファイルの順番

import sys
sys.path.append("../")
from common import Permutation


def main():
    fileNum = 15
    count = 0

    # i:動かす必要のある回数
    for i in range(fileNum):
        count += i * (fileNum - i) * Permutation(fileNum, i - 1)
    
    print(count)

    
if __name__ == "__main__":
    main()  

