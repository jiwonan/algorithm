n = int(input())

dp = []
dp.append(0)
dp.append(1)
dp.append(1)

for i in range(3, n+1):
    dp.append(dp[i-2] + dp[i-1])

print(dp[n])