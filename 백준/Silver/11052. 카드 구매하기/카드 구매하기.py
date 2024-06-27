import sys
input = sys.stdin.readline

def main():
    n = int(input())
    cards = list(map(int, input().split()))
    cards.insert(0,0)

    for i in range(1, n+1):
        for j in range(1, i+1):
            cards[i] = max(cards[i], cards[j]+cards[i-j])

    print(cards[n])

    return

if __name__ == '__main__':
    main()