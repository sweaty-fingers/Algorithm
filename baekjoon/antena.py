# https://www.acmicpc.net/problem/18310


def get_input():

    N = input()
    li = list(map(int, input().split(" ")))

    return li


def main():

    li = get_input()

    li.sort()
    index = len(li) // 2

    if len(li) == 1:
        print(li[0])

    indices = [index - 1, index]

    min_dist = 0
    for i in indices:
        dist_temp = 0
        for j in range(len(li)):
            dist_temp += abs(li[i] - li[j])

        if min_dist == 0:
            min_dist = dist_temp

        elif min_dist <= dist_temp:
            print(li[indices[0]])

        else:
            print(li[indices[1]])


if __name__ == "__main__":
    main()
