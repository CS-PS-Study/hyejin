from collections import deque

n = int(input())
A = [ [] for _ in range(n+1)]

for _ in range(n):
    data = list(map(int, input().split()))
    index = 0
    S = data[index] # 노드 번호 
    index += 1 
    while True:
        E = data[index] # 연결된 노드 
        if E == -1: # -1이면 종료
            break 
        V = data[index + 1] # 가중치 (거리)
        A[S].append((E,V)) # S에 연결한다.
        index += 2 # 그 다음 인덱스로 

distance = [0] * (n+1) # 거리 리스트
visited = [False] * (n+1) # 방문 리스트 

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_Node = queue.popleft() # 현재 노드 (탐색 시작)
        for i in A[now_Node]: # 현재 노드랑 연결된 노드 리스트 
            # i = (다음노드, 거리)
            if not visited[i[0]]:
                visited[i[0]] = True
                queue.append(i[0]) # BFS니까 큐에 넣어서 나중에 탐색 
                distance[i[0]] = distance[now_Node] + i[1] # 현재까지 온 거리 + 다음 노드까지 거리

BFS(1)
Max = 1

for i in range(2, n+1):
    if distance[Max] < distance[i]:
        Max = i

distance = [0] * (n+1)
visited = [False] * (n+1) # 다시 초기화해주고 
BFS(Max) # 최댓값 부분에서 다시 검사 시작.
distance.sort() # 정렬해준다. 가장 최댓값을 출력해내기 위해.
print(distance[n])