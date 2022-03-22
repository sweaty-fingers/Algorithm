from itertools import combinations

MAX_DIST = 1e10

def get_house_and_chicken(mapping):

    house = []
    chickens= []

    for i, r in enumerate(mapping):
        for c in range(len(r)):
            if r[c] == 1:
                house.append((i, c))
            if r[c] == 2:
                chickens.append((i, c))

    return house, chickens

def get_distance(house, comb):
    distance = 0 
    for h in house:
        dist_temp = []
        for c in comb:
            d = abs(h[0] - c[0]) + abs(h[1] - c[1])
            dist_temp.append(d)
        distance += min(dist_temp)

    return distance


def get_min_distance(house, chickens, m):
    chickens_comb = combinations(chickens, m)
    min_dist = MAX_DIST

    for comb in chickens_comb:
        min_dist = min(min_dist, get_distance(house, comb))
    
    return min_dist

def main():
    
    N, M = map(int, input().split(" "))

    mapping = []
    for _ in range(N):
        row = list(map(int, input().split(" ")))
        mapping.append(row)

    house, chickens = get_house_and_chicken(mapping)

    distance = get_min_distance(house, chickens, M)

    print(distance)

    return distance
    
if __name__ == "__main__":
    main()