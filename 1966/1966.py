import sys
from collections import deque
n = int(input())
for i in range(n):
    answer = []
    j = 0
    a, b = list(map(int, input().split()))
    read = list(map(int, sys.stdin.readline().split()))
    arr = []
    for i in range(len(read)):
        arr.append([i, read[i]])
    arr = deque(arr)
    arr1 = sorted(arr, key=lambda x: x[1], reverse=True)
    m = arr1[0][1]
    while(arr):
        cnt = arr.popleft()
        if cnt[1] == m:
            answer.append(cnt[0])
            if len(arr) != 0:
                arr1 = sorted(arr, key=lambda x: x[1], reverse=True)
                m = arr1[0][1]
        else:
            arr.append(cnt)
    print(answer.index(b)+1)
