import sys

n = int(input())
far = list(map(int, sys.stdin.readline().split()))
city = list(map(int, sys.stdin.readline().split()))
answer = 0
now = city[0]
i = 0
while(True):
    if now > city[i]:
        now = city[i]
    answer += far[i] * now
    i+=1
    if i == len(far):
        break
print(answer)