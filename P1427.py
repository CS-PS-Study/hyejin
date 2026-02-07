import sys
print = sys.stdout.write

A = list(input())

for i in range(len(A)):
    max = i # 제일 앞부터 비교 
    for j in range((i + 1), len(A)):
        # 현재 범위에서 max값 찾기
        if A[j] > A[max]:
            max = j
    # 제일 앞 index 값과 min 값 바꾸기 
    if A[i] < A[max]:
        tmp = A[i]
        A[i] = A[max]
        A[max] = tmp

for i in range(len(A)):
    print(A[i])