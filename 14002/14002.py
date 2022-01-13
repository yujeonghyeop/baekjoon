n = int(input())
a = list(map(int, input().split()))
dp = [0 for i in range(n)]
array = [[x] for x in a]
cnt = []
for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:
            array[i] = array[j] + [a[i]]
            dp[i] = dp[j]
    dp[i] += 1

for j in range(len(array)):
    if len(array[j]) == max(dp):
        flag = j
print(max(dp))
print(*array[flag])
