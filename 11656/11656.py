import sys
a = sys.stdin.readline().rstrip('\n')
answer = []
for i in range(len(a)):
    answer.append(a[i:])
answer = sorted(answer)
for j in range(len(answer)):
    print(answer[j])
