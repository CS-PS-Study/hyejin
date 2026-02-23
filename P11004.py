import sys 
input = sys.stdin.readline 

n, k = map(int, input().split())
A = list(map(int, input().split()))

# swap 함수 만들어줌 
def swap(i, j):
    global A 
    temp = A[i]
    A[i] = A[j]
    A[j] = temp 

def partition(start, end):
    global A 
    if start + 1 == end: # 비교 대상이 2개뿐일 때
        if A[start] > A[end]:
            swap(start, end)
        return end 
    
    middle = (start + end) // 2
    swap(start, middle)
    pivot = A[start]
    i = start + 1
    j = end

    while i <= j:
        while pivot < A[j] and j > 0:
            j -= 1 
        while pivot > A[i] and i < len(A) - 1:
            i += 1
        if i <= j:
            swap(i, j)
            i += 1
            j -= 1
    # i==j pivot의 값을 양쪽으로 분리한 가운데에 오도록 설정하기
    A[start] = A[j]
    A[j] = pivot
    return j 

# 별도의 함수 구현
def quickSort(start, end, k):
    global A 

    if start < end:
        pivot = partition(start, end)
        if pivot == k:
            return 
        elif k < pivot:
            quickSort(start, pivot-1, k)
        else:
            quickSort(pivot+1, end, k)

quickSort(0, n-1, k-1)
print(A[k-1])
