a = int(input())
answer = []
for i in range(a):
    h, w, c = map(int, input().split())
    if c % h == 0:
        floor = h
        room = c//h
    else:
        floor = c % h
        room = c//h+1
    if room < 10:
        answer.append(str(floor)+str(0)+str(room))
    else:
        answer.append(str(floor)+str(room))
for j in range(len(answer)):
    print(answer[j])
