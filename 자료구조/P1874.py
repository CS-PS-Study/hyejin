n = int(input())
A = [0]*n

for i in range(n):
    A[i] = int(input())
# 일단 n개만큼 입력 받아서 A 수열 리스트에 저장한다.

stack = [] #stack 추가
num = 1 # 오름차순 자연수 
result = True # 계속 참이면 돌고, 아니면 NO가 나오게끔 
answer = [] # 출력할 결과물 

for i in range(n):
    x = A[i] #현재 수열값을 x라고 두자.
    if x >= num: # 현재 수열값보다 오름차순 자연수가 크거나 같음
        while x >= num:
            stack.append(num)
            num += 1
            answer.append('+')
        stack.pop() # 그러고 제일 위에 있는 것 꺼내기 
        answer.append('-')
    else: # 현재 수열값 < 오름차순 자연수: pop()를 통해 원소를 꺼냄
        y = stack.pop() # 비교를 위해 잠시 y로 꺼냄
        if y > x: # 꺼낸 숫자가 현재 수열값보다 크면 오류
            print("NO")
            result = False
            break
        else:
            answer.append('-')

if result:
    for i in answer:
        print(i)
