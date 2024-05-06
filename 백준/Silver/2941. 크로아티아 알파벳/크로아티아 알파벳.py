str = input()

map = dict()
map["c"] = ["=", "-"]
map["d"] = ["z=", "-"]
map["l"] = ["j"]
map["n"] = ["j"]
map["s"] = ["="]
map["z"] = ["="]

count = 0
idx = 0
while idx < len(str):
    if str[idx] in map:
        if idx < len(str) - 1 and str[idx+1] in map[str[idx]]:
            idx+=2
        elif idx < len(str) - 2 and str[idx+1] +str[idx+2] in map[str[idx]]:
            idx+=3
        else:
            idx+=1
    else:
        idx+=1
    
    count += 1

print(count)