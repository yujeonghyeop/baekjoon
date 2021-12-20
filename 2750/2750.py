n = int(input())
answer=[]
for i in range(n):
    answer.append(int(input()))
answer=sorted(answer)
for j in range(n):
    print(answer[j])