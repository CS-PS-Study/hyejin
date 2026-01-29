from queue import PriorityQueue
import sys
print = sys.stdout.write
input = sys.stdin.readline

n = int(input())
myQueue = PriorityQueue()

for i in range(n):
    request = int(input())
    if request == 0:
        if myQueue.empty(): # 큐에 아무것도 없으면 0을 출력
            print('0\n')
        else: # 큐에 뭔가가 있으면 
            temp = myQueue.get() # 가장 우선순위가 높은 것을 출력한다.
            print(str((temp[1]))+'\n') # sys.stdout.write가 str만 허용하므로 이렇게 바꿔줌
    else: # 숫자를 입력하는 상황
        myQueue.put((abs(request), request))
        # 절댓값을 기준으로 정렬하고 같으면 음수 우선 정렬하도록 구성 