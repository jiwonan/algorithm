n = int(input())
nCards = set(map(int, input().split()))
m = int(input())
mCards = list(map(int, input().split()))

answer = []

for card in mCards:
    if card in nCards:
        answer.append("1")
    else:
        answer.append("0")

print(' '.join(answer))
