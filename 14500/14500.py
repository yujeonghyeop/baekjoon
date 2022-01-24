import sys
n,m = list(map(int,sys.stdin.readline().split()))
a = []
answer=[]
for i in range(n):
    read = list(map(int,sys.stdin.readline().split()))
    a.append(read)
new_list = list(map(list, zip(*a)))
#1번
for i in range(n):
    for j in range(m-3):
        answer.append(sum(a[i][j:j+4]))
for i in range(m):
    for j in range(n-3):
        answer.append(sum(new_list[i][j:j+4]))
#2번
for i in range(n-1):
    for j in range(m-1):
        answer.append(a[i][j]+a[i][j+1]+a[i+1][j]+a[i+1][j+1])
#3번 ㅜ
for i in range(n-1):
    for j in range(m-2):
        answer.append(a[i][j] + a[i][j+1]+a[i][j+2]+a[i+1][j+1])
#3번 ㅗ
for i in range(1,n):
    for j in range(m-2):
        answer.append(a[i][j]+a[i][j+1]+a[i][j+2]+a[i-1][j+1])
#3번 뒤집기 ㅜ
for i in range(m-1):
    for j in range(n-2):
        answer.append(new_list[i][j] + new_list[i][j+1]+new_list[i][j+2]+new_list[i+1][j+1])
#3번 뒤집기 ㅗ
for i in range(1,m):
    for j in range(n-2):
        answer.append(new_list[i][j]+new_list[i][j+1]+new_list[i][j+2]+new_list[i-1][j+1])
#4번 
for i in range(n-2):
    for j in range(m-1):
        answer.append(a[i][j]+a[i+1][j]+a[i+1][j+1]+a[i+2][j+1])
#4번 대칭
for i in range(n-2):
    for j in range(1,m):
        answer.append(a[i][j]+a[i+1][j]+a[i+1][j-1]+a[i+2][j-1])
for i in range(n-1):
    for j in range(1,m-2):
        answer.append(a[i][j]+a[i][j+1]+a[i+1][j]+a[i+1][j-1])
for i in range(n-1):
    for j in range(1,m-2):
        answer.append(a[i][j]+a[i][j-1]+a[i+1][j]+a[i+1][j+1])
#4번 뒤집기
for i in range(m-2):
    for j in range(n-1):
        answer.append(new_list[i][j]+new_list[i+1][j]+new_list[i+1][j+1]+new_list[i+2][j+1])
#4번 뒤집기 대칭
for i in range(m-2):
    for j in range(1,n):
        answer.append(new_list[i][j]+new_list[i+1][j]+new_list[i+1][j-1]+new_list[i+2][j-1])
for i in range(m-1):
    for j in range(1,n-2):
        answer.append(new_list[i][j]+new_list[i][j+1]+new_list[i+1][j]+new_list[i+1][j-1])
for i in range(m-1):
    for j in range(1,n-2):
        answer.append(new_list[i][j]+new_list[i][j-1]+new_list[i+1][j]+new_list[i+1][j+1])
#5번 
for i in range(n-2):
    for j in range(m-1):
        answer.append(a[i][j]+a[i+1][j]+a[i+2][j]+a[i+2][j+1])
#5번 대칭
for i in range(n-2):
    for j in range(1,m):
        answer.append(a[i][j]+a[i+1][j]+a[i+2][j]+a[i+2][j-1])
for i in range(n-1):
    for j in range(m-2):
        answer.append(a[i][j]+a[i][j+1]+a[i][j+2]+a[i+1][j+2])
for i in range(n-1):
    for j in range(m-2):
        answer.append(a[i][j]+a[i][j+1]+a[i][j+2]+a[i+1][j])
for i in range(m-1):
    for j in range(n-2):
        answer.append(new_list[i][j]+new_list[i][j+1]+new_list[i][j+2]+new_list[i+1][j+2])
for i in range(m-1):
    for j in range(n-2):
        answer.append(new_list[i][j]+new_list[i][j+1]+new_list[i][j+2]+new_list[i+1][j])    
for i in range(n-2):
    for j in range(m-1):
        answer.append(a[i][j]+a[i][j+1]+a[i+1][j]+a[i+2][j])
        answer.append(a[i][j]+a[i][j+1]+a[i+1][j+1]+a[i+2][j+1])    
for i in range(m-2):
    for j in range(n-1):
        answer.append(new_list[i][j]+new_list[i][j+1]+new_list[i+1][j]+new_list[i+2][j])
        answer.append(new_list[i][j]+new_list[i][j+1]+new_list[i+1][j+1]+new_list[i+2][j+1])
#5번 뒤집기
for i in range(m-2):
    for j in range(n-1):
        answer.append(new_list[i][j]+new_list[i+1][j]+new_list[i+2][j]+new_list[i+2][j+1])
#5번 뒤집기 대칭
for i in range(m-2):
    for j in range(1,n):
        answer.append(new_list[i][j]+new_list[i+1][j]+new_list[i+2][j]+new_list[i+2][j-1])
print(max(answer))