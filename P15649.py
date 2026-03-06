n, m = map(int, input().split())
s = [0] * m # 수열을 저장할 리스트
visited = [False] * n # 숫자 사용 여부 저장 리스트

def backtrack(length):
    if length == m: # 이미 길이가 m이 만들어진 경우
        print(' '.join(str(x+1) for x in s)) 
        # 공백을 구분자로 해서 리스트에 있는 값 출력하기 
        return 
    
    for i in range(n):
        if not visited[i]: # 아직 방문하지 않았으면 
            visited[i] = True 
            s[length] = i 
            backtrack(length + 1) 
            visited[i] = False # 다시 수를 반납하기 위해 

backtrack(0) 