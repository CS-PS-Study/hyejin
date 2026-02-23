import sys
# 재귀함수에 리밋을 걸어둔다. 과부하 문제
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())

A = [[] for _ in range(n+1)]
# 인접 리스트로 그래프를 표현하기 위해 이렇게 둔다.
# n+1로 두는 이유는 0부터 시작하는 걸 쉽게 이해하기 위해서 그냥 한 칸 늘려줌.
visited = [False] * (n+1)
# 이미 방문한 곳 리스트도 만들어준다. 초기엔 모두 방문한 적 없으니 False로 두기 

def DFS(v):
    visited[v] = True # 호출하면 방문하는 것
    for i in A[v]:
        if not visited[i]: # 방문하지 않은 상태(False)라면 재귀함수 추가 (스택에 추가하는 느낌)
            DFS(i) # 재귀함수

for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s) # 양방향이므로 서로 추가해주기

count = 0

for i in range(1, n+1):
    if not visited[i]: # 방문리스트에 False라면 DFS 함수 부르기 (스택에 들어간단 생각)
        count += 1
        DFS(i)

print(count) 