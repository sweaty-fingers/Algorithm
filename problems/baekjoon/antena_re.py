def get_input():
    n = int(input())
    house = list(map(int, input().split(" ")))

    return house


def main():
    house = get_input()
    house.sort()

    if len(house) == 1:
        print(house[0])
        return

    indices = [len(house) // 2 - 1, len(house) // 2]
    results = []

    for i in indices:
        result = 0
        for j in range(len(house)):

            result += abs(house[i] - house[j])

        results.append(result)


    print(house[indices[results[0] > results[1]]])


if __name__ == "__main__":
    main()

