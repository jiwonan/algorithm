price = int(input())
change = 1000 - price

count = 0
coins = [500,100,50,10,5,1]

for idx in range(0, len(coins)):
    count += change // coins[idx]
    change = change % coins[idx]

print(count)