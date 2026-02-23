import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline 
n = int(input())

def isPrime(num): # 소수 판별하는 함수 
    if num < 2: return False 
    for i in range(2, int(num ** 0.5) + 1): # 2부터 시작해서 제곱근까지만 확인
        if num % i == 0: # 나눠떨어지면 소수가 아니므로 False 반환
            return False
    return True

def DFS(number):
    if len(str(number)) == n:
        print(number)
        return 
    else:
        for i in [1, 3, 7, 9]:
            if isPrime(number * 10 + i): # 소수이면 다음수로 늘려서 다시 시작 (재귀함수로 계속 반복)
                DFS(number * 10 + i)

# 일의 자리 소수는 2, 3, 5, 7이므로 4가지 수에서만 시작한다.
DFS(2)
DFS(3)
DFS(5)
DFS(7)
