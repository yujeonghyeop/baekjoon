a = int(input())
answer = []
b = a//5+1
for i in range(1, b):
    if (a-5*i) % 3 == 0:
        answer.append(i+(a-5*i)//3)
        print(answer, i)
if a % 3 == 0:
    answer.append(a//3)
if a % 5 == 0:
    answer.append(a//5)
if len(answer) == 0:
    print(-1)
else:
    print(answer)
    print(min(answer))
