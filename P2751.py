import sys
input = sys.stdin.readline
print = sys.stdout.write

def mergeSort(start, end):
    # 구간의 길이가 1이면 종료. 이미 정렬된 상태라서. 
    if end - start < 1 :
        return
    # 가운데값 구하기. 
    middle = int(start + (end - start) / 2)
    # (start + end) / 2 라고 안 하고 이렇게 굳이 나눠서 한 이유는 오버플로우 방지

    # 재귀 함수로 구현
    mergeSort(start, middle)
    mergeSort(middle + 1, end)

    # 정렬 전 상태를 tmp 배열에 복사
    for i in range(start, end + 1):
        tmp[i] = A[i]
    
    # 병합을 위한 변수 초기화 
    k = start # 정렬된 값을 넣을 위치 
    index1 = start # 왼쪽 배열 시작 
    index2 = middle + 1 # 오른쪽 배열 시작

    # 왼쪽과 오른쪽 비교하며 작은 값부터 넣기 
    while index1 <= middle and index2 <= end:
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            k += 1
            index2 += 1
        else:
            A[k] = tmp[index1]
            k += 1
            index1 += 1
    # 왼쪽 배열이 남은 경우
    while index1 <= middle:
        A[k] = tmp[index1]
        k += 1
        index1 += 1
    # 오른쪽 배열이 남은 경우
    while index2 <= end:
        A[k] = tmp[index2]
        k += 1
        index2 += 1

n = int(input())
# 1번 인덱스부터 사용하기 위해 n+1 크기 
A = [0] * int(n + 1)
tmp = [0] * int(n + 1)

for i in range(1, n+1):
    A[i] = int(input())

# 병합 정렬 실행 
mergeSort(1, n)

# 결과 출력
for i in range(1, n+1):
    print(str(A[i]) + '\n')