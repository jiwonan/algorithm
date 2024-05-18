import sys
input = sys.stdin.readline

def main():
    n = int(input())
    stairs = [0]

    for _ in range(0, n):
        stairs.append(int(input()))

    if n <= 2:
        print(sum(stairs))
        return


    dp = [0] * (n + 1)
    dp[1] = stairs[1]
    dp[2] = dp[1] + stairs[2]

    for i in range(3, n+1):
        stepBefore1 = dp[i-2] + stairs[i] # 전전 계단을 밟고 오는 경우
        stepBefore2 = dp[i-3] + stairs[i-1] + stairs[i] # 직전 계단을 밟고 오는 경우
        dp[i] = max(stepBefore1, stepBefore2)

    print(dp[n])

if __name__ == "__main__":
    main()