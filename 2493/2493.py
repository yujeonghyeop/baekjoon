import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))
stack = []
pos = {}
for i in range(len(a)):
    pos[a[i]] = i
answer =[0]*n
for i in range(n-1, -1, -1):
    if len(stack) == 0:
        stack.append(a[i])
    else:
        if stack[-1] < a[i]:
            cnt = stack.pop()
            answer[pos[cnt]] = i+1
            while(True):
                if len(stack) == 0:
                    stack.append(a[i])
                    break
                else:
                    if stack[-1] < a[i]:
                        cnt = stack.pop()
                        answer[pos[cnt]] = i+1
                    else:
                        stack.append(a[i])
                        break
        elif stack[-1] >= a[i]:
            stack.append(a[i])
print(*answer)