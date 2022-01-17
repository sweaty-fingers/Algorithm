def make_group(N, fearness):
    N = N
    fear_list = list(map(int, fearness.split(" ")))
    print(fear_list)

    fear_list.sort()
    group_num = 0
    count = 0
    for i in fear_list:
        count += 1

        if i <= count:
            group_num += 1
            count = 0

    return group_num

if __name__ == "__main__":

    N = 5
    fearness = "2 3 1 2 2"
    result = make_group(N, fearness)

    print(result)
