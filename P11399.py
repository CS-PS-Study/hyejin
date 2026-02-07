n = int(input())
A = list(map(int, input().split()))
S = [0] * n

for i in range(1, n): # i는 선택된 값 
    selected = A[i] # 선택된 값 따로 저장해두기 
    insert_point = i # 삽입 포인트 지정 
    for j in range(i-1, -1, -1):
        # 한 칸씩 왼쪽으로 가면서 현재 선택된 값이 비교 값보다 작으면 더 왼쪽으로 감
        # 그러다가 현재 값이 j값보다 크면 그곳이 삽입할 자리임.
        if A[j] < selected:
            insert_point = j + 1
            break
        if j == 0: # 맨 앞까지 간 경우
            insert_point = 0
    for j in range(i, insert_point, -1):
        # 뒤에서부터 한 칸씩 뒤로 밀어야 됨
        A[j] = A[j-1]
    # 삽입 위치에 현재 데이터 저장 
    A[insert_point] = selected

# 합 배열
S[0] = A[0] # 처음은 이렇게 하고 밑에선 반복문으로 1부터 시작.
for i in range(1, n):
    S[i] = S[i-1] + A[i]

# 합 배열 합치기
sum = 0
for i in range(n):
    sum += S[i]

print(sum)