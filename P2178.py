from collections import deque

# 상하좌우를 탐색하기 위한 리스트 선언
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
n, m = map(int, input().split())
A = [[0] * m for _ in range(n)] # 미로 2차원 리스트 만들기
visited = [[False] * m for _ in range(n)]

for i in range(n):
    numbers = list(input())
    for j in range(m):
        A[i][j] = int(numbers[j])

def BFS(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    while queue:
        now = queue.popleft()
        for k in range(4): #상하좌우
            x = now[0] + dx[k] 
            y = now[1] + dy[k]
            if x >= 0 and y >= 0 and x < n and y < m:
                if A[x][y] != 0 and not visited[x][y]:
                    visited[x][y] = True
                    A[x][y] = A[now[0]][now[1]] + 1
                    queue.append((x, y))

BFS(0,0)
print(A[n-1][m-1])
