import sys

n = int(sys.stdin.readline())
array = sys.stdin.readline().split()
dp = [10001]*(n*2)  # dp 테이블 초기화
for i in range(1, n+1):  # 더해주는 기준값이기 때문에 1부터 시작
    # 더해지기 이전에 순전히 Pn으로 dp[n]을 만족할 수 있기 때문에 값 비교
    dp[i] = min(dp[i], int(array[i-1]))
    for j in range(n):
        # 이전의 값과 더해진 값중 최댓값을 dp 테이블에 저장
        dp[j+i] = min(dp[j+i], dp[j]+int(array[i-1]))
print(dp[n])
