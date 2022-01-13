# solver1.py
#   Created on: 2021/01/11
#       Author: a_takeuchi
#  Chapter1-1
#  一発で決まる多数決

def main():
    N = 100      # 多数決に参加する人数
    K = 3       # 選択肢の数
    count = 0

    for i in range(N+1):
        if i < N / 3:
            continue
        for j in range(N-i+1):
            k = N - i - j
            if k > j or j >= i:
                continue
            if k == j:
                count += 3
            else:
                count += 6
    print(count)


if __name__ == "__main__":
    main()  