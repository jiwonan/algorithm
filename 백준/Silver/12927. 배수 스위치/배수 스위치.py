def toggle(state):
    if state == 'N':
        return 'Y'
    else: return 'N'

switch = list(input())
count = 0

for i in range(0, len(switch)):
    if switch[i] == 'N':
        continue
    for j in range(i, len(switch), i + 1):
        switch[j] = toggle(switch[j])
    count += 1

print(count)