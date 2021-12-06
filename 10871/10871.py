import sys
r, num = input().split()
r = int(r)
num = int(num)
cnt = sys.stdin.readline().split()
answer = []
for i in range(r):
    if int(cnt[i]) < num:
        answer.append(cnt[i])
print(*answer)
