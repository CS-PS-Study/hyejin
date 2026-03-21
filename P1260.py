from collections import deque
# 큐를 사용할 거니까 deque를 import해준다.
n, m, start = map(int, input().split())
A = [ [] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

for i in range(n+1):
    A[i].sort()
    # 번호가 ㅈ가은 순서부터 방문하기 위해 정렬해준다.

def DFS(v):
    print(v, end = ' ')
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)

visited = [False] * (n+1) # 방문한 노드 리스트
DFS(start)

def BFS(v):
    queue = deque() # 큐 불러오기
    queue.append(v)
    visited[v] = True
    while queue: # 큐가 채워져있으면
        now_node = queue.popleft()
        print(now_node, end = ' ')
        for i in A[now_node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

print() # 줄 띄워주기
visited = [False] * (n+1) # BFS 시작
BFS(start)