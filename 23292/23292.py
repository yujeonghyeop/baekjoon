birth = input()
num = int(input())
time = []
bio = []
vs = []
answer = []
for i in range(num):
    cnt = input()
    time.append(cnt)
for i in range(num):
    count1 = 0
    count2 = 0
    count3 = 0
    for j in range(4):
        count1 += (int(birth[j])-int(time[i][j]))**2
    for k in range(4, 6):
        count2 += (int(birth[k])-int(time[i][k]))**2
    for q in range(6, 8):
        count3 += (int(birth[q])-int(time[i][q]))**2
    bio.append(count1*count2*count3)
print(bio)
for i in range(len(bio)):
    if bio[i] == max(bio):
        vs.append(i)
if len(vs) >= 2:
    for p in range(len(vs)):
        answer.append(time[vs[p]])
    answer.sort()
    print(answer[0])
else:
    print(time[vs[0]])
