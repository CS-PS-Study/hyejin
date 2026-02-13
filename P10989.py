import sys
input = sys.stdin.readline

n = int(input())
count = [0] * 10001

# 계수 정렬. 인덱스와 같은 입력값에 1을 추가해주는 식.
for i in range(n):
    count[int(input())] += 1

for i in range(10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)