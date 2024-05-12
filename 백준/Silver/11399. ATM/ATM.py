import sys

num = int(input())
time = list(map(int, sys.stdin.readline().split()))
time.sort()

wait = [0,]

sum = 0
idx = 0

for t in time:
    sum += (t + wait[idx])
    wait.append(t + wait[idx])
    idx += 1

print(sum)