import sys
n = int(sys.stdin.readline())
candy = []
temp = ''
answer = 0
answercnt = 1
for i in range(n):
    candy.append(sys.stdin.readline().split())
    candy[i] = ''.join(candy[i])
    candy[i] = list(candy[i])
for i in range(n):
    for j in range(n-1):
        if candy[i][j] != candy[i][j+1]:
            temp = candy[i][j]
            candy[i][j] = candy[i][j+1]
            candy[i][j+1] = temp
            for k in range(n):
                for p in range(n-1):
                    if candy[p][k] == candy[p+1][k]:
                        answercnt += 1
                    else:
                        if answercnt > answer:
                            answer = answercnt
                        answercnt = 1
                if answercnt > answer:
                    answer = answercnt
                answercnt = 1
            for k in range(n):
                for p in range(n-1):
                    if candy[k][p] == candy[k][p+1]:
                        answercnt += 1
                    else:
                        if answercnt > answer:
                            answer = answercnt
                        answercnt = 1
                if answercnt > answer:
                    answer = answercnt
                answercnt = 1
            candy[i][j+1] = candy[i][j]
            candy[i][j] = temp
for i in range(n):
    for j in range(n-1):
        if candy[j][i] != candy[j+1][i]:
            temp = candy[j][i]
            candy[j][i] = candy[j+1][i]
            candy[j+1][i] = temp
            for k in range(n):
                for p in range(n-1):
                    if candy[k][p] == candy[k][p+1]:
                        answercnt += 1
                    else:
                        if answercnt > answer:
                            answer = answercnt
                        answercnt = 1
                if answercnt > answer:
                    answer = answercnt
                answercnt = 1
            for k in range(n):
                for p in range(n-1):
                    if candy[p][k] == candy[p+1][k]:
                        answercnt += 1
                    else:
                        if answercnt > answer:
                            answer = answercnt
                        answercnt = 1
                if answercnt > answer:
                    answer = answercnt
                answercnt = 1
            candy[j+1][i] = candy[j][i]
            candy[j][i] = temp
print(answer)
