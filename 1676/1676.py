import math
a = int(input())
cnt = str(math.factorial(a))
answer = 0
for i in reversed(range(len(cnt))):
    if cnt[i] == '0':
        answer += 1
    else:
        print(answer)
        break
