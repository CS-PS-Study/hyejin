import sys 
sys.setrecursionlimit(10000)
input = sys.stdin.readline 
n, m = map(int, input().split())
arrive = False # 순환이 되면 True로 바뀌며 종료 위함
A = [[] for _ in range(n + 1)] # 인접 리스트로 그래프를 표현한다.
visited = [False] * (n + 1) # 방문 리스트

def DFS(now, depth):
    global arrive
    if depth == 5: # 깊이가 5가 되면 종료
        arrive = True
        return
    visited[now] = True
    for i in A[now]:
        if not visited[i]:
            DFS(i, depth + 1) # 재귀호출마다 깊이가 증가한다 
    visited[now] = False # 끝까지 다 돌았는데도 모든 점을 방문하지 못했으면 다시 구해야 하므로 방문 리스트를 리셋해준다.

for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

for i in range(n):
    DFS(i, 1)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)