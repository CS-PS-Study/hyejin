import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A=list(map(int, input().split()))
B = [0]*m # 이건 각 구간 합의 m으로 나눈 나머지 종류를 세는 것

D = [0]*n # 구간 합 배열 
for i in range(n):
    D[i]=(D[i-1] + A[i]) % m # 구간 합을 구하고 나머지로 나눠준다.
    B[D[i]] += 1 # 그 나머지의 값을 나머지 배열에 추가한다. (갯수 파악)

count = 0 # 이건 정답 세는 용도 

count += B[0]
# 나머지가 0인 것만으로 조건에 충분.

for i in range(0, m):
    count += int((B[i] * (B[i]-1))/2)
    # 구간 합끼리 뺀 것이 조건에 만족하는 경우

print(count)