import sys
input = sys.stdin.readline
# 구간 합 구하는 거고 시간 단축해야 되니까 빠른 입력

# n: 숫자 개수, m: 합을 구해야 하는 횟수
n, m = map(int, input().split())
numbers = list(map(int, input().split())) # 숫자 데이터 저장
prefix_sum = [0] # 합 배열 변수 선언
temp = 0

for i in numbers:
    temp += i
    prefix_sum.append(temp)

for i in range(m):
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s-1])
