tc = int(input())

answer = []

for _ in range(0, tc):
    n = int(input())
    dp = []
    dp.append(0)
    dp.append(1)
    dp.append(2)
    dp.append(4)

    for i in range(4, n+1):
        dp.append(dp[i-1]+dp[i-2]+dp[i-3])
    
    answer.append(dp[n])

for a in answer:
    print(a)
