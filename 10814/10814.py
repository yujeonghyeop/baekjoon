n=int(input())
answer=[]
for i in range(n):
    a,b=input().split()
    a=int(a)
    answer.append([a,b])
answer=sorted(answer, key=lambda x:x[0])
for j in range(n):   
    print(*answer[j])