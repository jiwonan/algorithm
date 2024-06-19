import sys
input = sys.stdin.readline

k, n = map(int, input().split())
ropes = []
for _ in range(0, k):
    ropes.append(int(input()))

def getLonger(length):
    cnt = 0
    for rope in ropes:
        cnt += rope // length
    
    return cnt >= n

def main():
    left = 1
    right = max(ropes)
    temp = []

    while left <= right:
        mid = (left + right) // 2
        if getLonger(mid):
            left = mid + 1
            temp.append(mid)
        else:
            right = mid - 1
    
    print(max(temp))

if __name__ == '__main__':
    main()