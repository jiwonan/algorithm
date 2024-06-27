import sys
input = sys.stdin.readline

def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    dp = [-1 for _ in numbers]

    dp[0] = numbers[0]

    for idx in range (1, n):
        dp[idx] = max((dp[idx-1] + numbers[idx]), numbers[idx])

    print(max(dp))

    return 1

if __name__ == '__main__':
    main()