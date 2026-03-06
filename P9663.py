import sys 
input = sys.stdin.read 
sys.setrecursionlimit(10**6)

n = int(input())
cnt = 0 

cols = [False] * n # 열 충돌 체크
diag1 = [False] * (2 * n - 1) # 오른쪽 위 대각선 체크 (row + col)
diag2 = [False] * (2 * n - 1) # 오른쪽 아래 대각선 체크 (row - col + n - 1)

def backtrack(row):
    global cnt 
    if row == n: # 이미 n개 다 차있으면 return 
        cnt += 1 # 경우의 수 1개 증가
        return 
    for col in range(n):
        if not cols[col] and not diag1[row + col] and not diag2[row - col + n - 1]:
            cols[col] = diag1[row + col] = diag2[row - col + n - 1] = True
            backtrack(row + 1) # 다음에도 반복
            cols[col] = diag1[row + col] = diag2[row - col + n - 1] = False # 다시 false로 맞춰주고 이어서 하기 

backtrack(0)
print(cnt) 