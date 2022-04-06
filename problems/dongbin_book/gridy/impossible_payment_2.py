def get_input():
    n = int(input())
    coins = list(map(int, input().split(" ")))

    return n, coins


def main():
    n, coins = get_input()

    coins.sort()
    target = 1
    for c in coins:
        
        if c > target:
            break
        else:
            target += c

    print(target)

if __name__ == "__main__":
    main()