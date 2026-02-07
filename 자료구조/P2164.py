from collections import deque # 큐 꺼내기
n = int(input())
myQueue = deque()

for i in range(1, n+1):
    myQueue.append(i)
    # index가 즉 숫자가 되도록 

while len(myQueue) > 1: # 카드가 1장 남을 때까지
    # 맨 위 카드 버림
    myQueue.popleft()
    # 맨 위 카드를 가장 아래의 카드 밑으로 이동
    myQueue.append(myQueue.popleft())

print(myQueue[0]) # 마지막으로 남은 카드 출력 