def impossible(input):
    coins = list(map(int, input.split(" ")))
    coins.sort()

    target = 1
    for c in coins:

        if c > target:
            break
        else:
            target += c

    return target
     

if __name__ == "__main__":
    N = 5
    input = "3 2 1 1 9"

    target = impossible(input)

    print(target)