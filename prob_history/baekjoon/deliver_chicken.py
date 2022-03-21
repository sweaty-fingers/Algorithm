def get_house_and_chicken(mapping):

    house = []
    chicken = []
    for i, r in enumerate(mapping):
        for c in range(len(r)):
            if r[c] == 1:
                house.append((i, c))
                
            if r[c] == 2:
                chicken.append((i, c))
    return house, chicken


def get_distance(house, chicken):
    """
    distance list 반환
    row : 집 번호
    column : 치킨집 번호
    """
    distance = []
    for h in house:
        dist = []
        for c in chicken:
            d = abs(h[0] - c[0]) + abs(h[1] - c[1])
            dist.append(d)
        distance.append(dist)

    return distance


def select_chicken(distance, min_list, num_chicken, selected):

    min_list_new = min_list[:]
    _min_total_dist = sum(min_list)

    if selected:
        _min_idx = selected[-1]
    else:
        _min_idx = None

    for n in range(num_chicken):
        if n in selected:
            continue

        min_list_temp = min_list_new[:]  # len : 집의 수

        for i, h in enumerate(distance):
            min_list_temp[i] = min(h[n], min_list[i])

        if sum(min_list_temp) < _min_total_dist:
            _min_total_dist = min(sum(min_list_temp), _min_total_dist)
            _min_idx = n
            min_list_new = min_list_temp[:]
            # print("update")
            # print(min_list_new)
            # print(_min_idx)

    if _min_idx is not None:
        selected.append(_min_idx)
        return min_list_new
    else:
        return min_list


def main():
    MAX_DIST = 1e10
    N, M = map(int, input().split(" "))

    mapping = []
    for _ in range(N):
        row = list(map(int, input().split(" ")))
        mapping.append(row)

    house, chicken = get_house_and_chicken(mapping)
    num_house = len(house)
    num_chicken = len(chicken)

    # print(f"house : {house!r}")
    # print(f"chicken : {chicken!r}")
    # print(f"num_house : {num_house}")
    # print(f"num_chicken : {num_chicken}")

    distance = get_distance(house, chicken)
    # print("distance list : ")
    # print(f"{distance!r}")

    selected = []
    min_list = [MAX_DIST for _ in range(num_house)]
    min_dist = sum(min_list)

    while True:
        if len(selected) >= M:
            return min_dist

        min_list = select_chicken(distance, min_list, num_chicken, selected)

        if sum(min_list) < min_dist:
            min_dist = sum(min_list)
        else:
            return min_dist

        # print("end")
        # print(selected)
        # print(min_list)
        # print(min_dist)

    return min_dist


if __name__ == "__main__":

    answer = main()
    print(answer)
