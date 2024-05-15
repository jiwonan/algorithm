st = input()

temp = ""
initQueue = []

for n in st:
    if n == "+" or n == "-":
        initQueue.append(temp)
        initQueue.append(n)
        temp = ""
    else:
        temp += n
initQueue.append(temp)

answer=int(initQueue.pop(0))
inBracket = False

curOp = ""
while len(initQueue) != 0:
    value = initQueue.pop(0)

    if value == "-" and not inBracket:
        inBracket = True
        curOp = "-"

    if value == "-":
        curOp = "-"
    elif value == "+":
        curOp = "+"
    elif value.isnumeric():
        op = 1
        if inBracket or curOp == "-":
            op = -1
        answer += (abs(int(value)) * op)

print(answer)