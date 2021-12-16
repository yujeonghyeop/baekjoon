n = int(input())
answer = []
score = [1]*n
for i in range(n):
    a, b = map(int, input().split())
    answer.append([a, b])
    if len(answer) >= 2:
        for j in range(len(answer)):
            if answer[j][0] > answer[-1][0] and answer[j][1] > answer[-1][1]:
                score[len(answer)-1] += 1
            elif answer[j][0] < answer[-1][0] and answer[j][1] < answer[-1][1]:
                score[j] += 1
print(*score)
