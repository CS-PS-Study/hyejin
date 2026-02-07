import sys
n = int(input())
ans = [0] * n # 정답 리스트 

A = list(map(int, input().split()))
myStack = [] # 스택 선언 

for i in range(n):
    # 스택이 비어있지 않고 현재 수열이 스택 top 인덱스가 가리키는 수열보다 큰 경우
    while myStack and A[i] > A[myStack[-1]]:
        ans[myStack.pop()] = A[i] # 정답 리스트에 오큰수를 현재 수열로 저장한다
    myStack.append(i)

while myStack: # 반복문을 다 돌고 나왔는데 스택이 비어 있지 않다면
    ans[myStack.pop()] = -1 # -1 넣기

for i in range(n):
    sys.stdout.write(str(ans[i]) + " ")
    # 출력 속도 때문에 print 대신 이렇게 써줌 
