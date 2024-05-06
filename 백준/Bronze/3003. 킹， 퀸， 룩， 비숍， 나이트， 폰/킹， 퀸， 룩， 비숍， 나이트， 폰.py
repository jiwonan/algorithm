import sys
found = list(map(int, sys.stdin.readline().split()))
base = [1,1,2,2,2,8]

for idx in range(len(found)):
    print(base[idx] - found[idx], end=" ")