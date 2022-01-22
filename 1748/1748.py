import sys
n = sys.stdin.readline().rstrip()
cnt = len(n)
answer = 0
if cnt == 1:
    print(int(n))
else:
    a = 10**(cnt-1)
    b = int(n) - a
    answer += (b+1) * cnt
    cnt -= 1
    while(cnt != 0):
        answer += 9 * cnt * (10**(cnt-1))
        cnt -= 1
    print(answer)
