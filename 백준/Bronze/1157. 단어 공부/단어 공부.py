input = input().upper()

map = dict()

for x in input:
    if x in map:
        map[x] = map[x] + 1
    else:
        map[x] = 1

max = 0
alpha = "?"
for x in map:
    if max == map[x]:
        alpha = "?"
    elif max < map[x]:
        max = map[x]
        alpha = x

print(alpha)