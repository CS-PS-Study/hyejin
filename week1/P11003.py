from collections import deque 
# deque 자료구조를 사용하기 위해 가져오기

n, l = map(int, input().split()) # n: 데이터 개수, l: 최솟값 범위
mydeque = deque() # deque를 가져옴 
now = list(map(int, input().split())) # 숫자 데이터 리스트

for i in range(n):
    # 덱의 마지막 위치에서부터 현재 값보다 큰 값은 덱에서 제거
    while mydeque and mydeque[-1][1] > now[i]:
        mydeque.pop()
    # 여기서 mydeque 는 안에 값이 있는지 확인하려는 용도.
    # mydeque[-1][1]은 가장 뒤에 있는 1번 인덱스라는 뜻. 값이 들어 있는 것.

    # 덱의 마지막 위치에 현재 값 저장
    mydeque.append((i, now[i])) # 튜플 상태로 저장 

    # 덱의 1번째 위치에서부터 l의 범위를 벗어난 값을 덱에서 제거
    if mydeque[0][0] <= i - l:
        mydeque.popleft()

    # 덱의 1번째 데이터 출력 
    print(mydeque[0][1], end=' ') # 줄바꿈 되지 않고 띄어쓰기만 되도록 