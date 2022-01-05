import sys
import math
a = int(sys.stdin.readline())
answer = ''
while(True):
    if a % -2 == -1:
        a = (a//-2)+1
        answer += '1'
    elif a % -2 == 0:
        a = a//-2
        answer += '0'
    if a == 1:
        answer += '1'
        break
print(answer[::-1])
