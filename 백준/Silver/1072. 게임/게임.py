x, y = map(int, input().split())
z = y * 100 // x

def calc(n):
    nZ = (y + n) * 100 // (x + n)
    if nZ > z:
        return True
    return False

def solutaion():
    if z >= 99:
        print(-1)
        return
    
    left = 1
    right = x

    while left <= right:
        mid = (left + right) // 2
        if calc(mid):
            right = mid - 1
        else:
            left = mid + 1
    
    print(left)
        


if __name__ == '__main__':
    solutaion()