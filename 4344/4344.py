import sys
number = int(input())
answer = []
for i in range(number):
    av = 0
    count = 0
    cnt = sys.stdin.readline().split()
    for j in range(1, len(cnt)):
        av += int(cnt[j])
    av = av/int(cnt[0])
    for k in range(1, len(cnt)):
        if int(cnt[k]) > int(av):
            count += 1
    answer.append(round(count/int(cnt[0]), 5))
for p in range(len(answer)):
    print('%.3f' % (answer[p]*100)+'%')
