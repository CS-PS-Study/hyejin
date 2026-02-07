n = int(input())
count = 1 # 숫자 자신 포함하기 때문에 1로 초기화
start_index = 1
end_index = 1
sum = 1 

while end_index != n:
    if sum == n: 
        count += 1
        end_index += 1
        sum = sum + end_index
    elif sum > n:
        sum = sum - start_index
        start_index += 1
    else:
        end_index += 1
        sum += end_index 

print(count)