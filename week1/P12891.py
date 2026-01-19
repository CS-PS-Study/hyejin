# 전역 변수 선언
checkList = [0] * 4 # 비밀번호 체크 리스트 (ACGT)
myList = [0] * 4 # 현재 상태 리스트
checkSecret = 0 # 몇 개의 문자가 개수 조건을 충족했는지

# 함수 선언
def myadd(c): # 문자 더하기 함수
    # 새로 들어온 문자에 대해 myList 업데이트 및 checkSecret 값 변경
    global checkList, myList, checkSecret
    if c == 'A':
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret += 1
            # 왜 >= 말고 ==를 쓰냐면 >=를 쓰면 항상 늘어날 수 있으므로.
    elif c == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif c == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif c == 'T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1

def myremove(c): # 문자 빼기 함수
    global checkList, myList, checkSecret
    if c == 'A':
        if myList[0] == checkList[0]:
            checkSecret -= 1
        myList[0] -= 1
    elif c == 'C':
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    elif c == 'G':
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -= 1
    elif c == 'T':
        if myList[3] == checkList[3]:
            checkSecret -= 1
        myList[3] -= 1

# 메인 코드
s, p = map(int, input().split()) # s: 문자열 크기, p: 부분 문자열 크기
a = list(input()) # 문자열 데이터
checkList = list(map(int, input().split())) # 비밀번호 체크 리스트 받기
result = 0 # 결과값 출력용 

# 체크 리스트에 0이 있으면 언제든 참이므로
for i in range(4):
    if checkList[i] == 0:
        checkSecret += 1

# 초기 슬라이드 만들기 
for i in range(p):
    myadd(a[i])
# 이미 첫 슬라이드부터 만족하는 경우 1 증가시키기
if checkSecret == 4:
    result += 1

# 이제 그 뒷부분부터 슬라이드 추가하면서 진행
for i in range(p, s):
    j = i - p # 슬라이드 가장 첫 부분 인덱스
    myadd(a[i])
    myremove(a[j])
    if checkSecret == 4:
        result += 1

print(result)
