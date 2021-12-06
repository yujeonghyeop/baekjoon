A = int(input())
B = int(input())
C = int(input())
cnt = str(A*B*C)
answer = [0]*10
for i in range(len(cnt)):
    answer[int(cnt[i])] += +1
for i in range(len(answer)):
    print(answer[i])
