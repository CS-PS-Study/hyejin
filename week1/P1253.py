import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
A.sort()
count = 0

for k in range(n): # i와 j의 투 포인터 설정 범위 확인
    find = A[k]
    i = 0
    j = n-1 
    while i < j: # i와 j가 같으면 '좋은 수'가 아닌 것
        if A[i] + A[j] == find:
            if i != k and j != k:
                count += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif A[i] + A[j] < find:
            i += 1
        else:
            j -= 1

print(count)
