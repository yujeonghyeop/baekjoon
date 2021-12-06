import sys
a = int(input())
answer = []
for i in range(a):
    b = ''
    read = sys.stdin.readline().split()
    for j in range(len(read[1])):
        b += read[1][j]*int(read[0])
    answer.append(b)
    print(answer[i])
