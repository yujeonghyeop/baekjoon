import sys
from itertools import combinations
## ENTJ INTP ESFJ
T = int(input())
for i in range(T):
    mbti = {}
    status = False
    N = int(input())
    a = sys.stdin.readline().split()
    for p in a:
        if p in mbti:
            mbti[p] += 1
            if mbti[p] >= 3:
                status = True
        else:
            mbti[p] = 1
    if status == False:
        answer = []
        all = list(combinations(a,3))
        for j in all:
            tmp = 0
            p1 = j[0]
            p2 = j[1]
            p3 = j[2]
            for i in range(4):
                if p1[i] != p2[i]:
                    tmp += 1
                if p1[i] != p3[i]:
                    tmp += 1
                if p2[i] != p3[i]:
                    tmp += 1
            answer.append(tmp)
        print(min(answer))
    else:
        print(0)
