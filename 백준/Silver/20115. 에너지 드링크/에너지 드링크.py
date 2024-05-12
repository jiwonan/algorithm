count = int(input())
size = list(map(int, input().split()))
size.sort(reverse=True)

sum = size[0]

for i in range(1, len(size)):
    sum += size[i] / 2

print(sum)