import string
import sys

tmp = string.digits+string.ascii_uppercase

read = sys.stdin.readline().split()
a = int(read[1])
cnt = 1
b = read[0]
answer = 0
for i in reversed(range(len(b))):
    answer += tmp.index(b[i])*cnt
    cnt = cnt*a
print(answer)
