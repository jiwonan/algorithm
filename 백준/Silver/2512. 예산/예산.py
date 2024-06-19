import sys
input = sys.stdin.readline

n = int(input())
requests = list(map(int, input().split()))
budget = int(input())

def giveMore(eachBudget):
    sum = 0
    for request in requests:
        if request > eachBudget:
            sum += eachBudget
        else:
            sum += request
    
    return sum <= budget

def main():
    left = 1
    right = budget
    temp = []

    while left <= right:
        mid = (left + right) // 2
        if giveMore(mid):
            left = mid + 1
            temp.append(mid)
        else:
            right = mid - 1
    
    maxBudget = max(temp)
    maxRequest = max(requests)

    if maxBudget > maxRequest:
        print(maxRequest)
    else:
        print(maxBudget)

if __name__ == '__main__':
    main()