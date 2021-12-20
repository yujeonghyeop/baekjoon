n=int(input())
answer=[]
for i in range(n):
    a,b=map(int,input().split())
    answer.append([a, b])
answer=sorted(answer,key= lambda x:(x[0],x[1]))
for j in range(n):
    print(*answer[j])