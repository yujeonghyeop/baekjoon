A = int(input())
answer = []
for i in range(A):
    count=0
    ans=0
    cnt = str(input())
    for j in range(len(cnt)):
        if cnt[j]=='O':
            count+=1
            ans+=count
        else:
            count=0
    answer.append(ans)
for i in range(len(answer)):
        print(answer[i])