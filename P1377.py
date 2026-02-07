import sys
input = sys.stdin.readline 
# 빨리 계산해야 돼서... 

n = int(input())
A = []

# A 리스트를 저장한다.
for i in range(n):
    A.append((int(input()), i)) # 괄호 주의! 튜플 형태로 저장해야 된다.
    # 인덱스 값을 포함하여 같이 저장한다.

# A 리스트를 정렬한다.
B = sorted(A) # 새로운 리스트를 만들어서 정렬된 걸 복사해준다. 
max = 0 # 최댓값 계산해야 되니까 하나 선언해줌

# 정렬 전 인덱스에서 정렬 후 인덱스를 뺀 최댓값을 구한다.
for i in range(n):
    if B[i][1] - i > max:
        max = B[i][1] - i

print(max + 1)