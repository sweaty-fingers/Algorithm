# 백준 치킨배달
# https://www.acmicpc.net/problem/15686

from itertools import combinations

def get_input():
    n, m = map(int, input().split(" "))
    
    ind_chicken = []
    ind_home = []
    
    for i in range(n):
        temp = list(map(int, input().split(" ")))
        for j, t in enumerate(temp):
            if t == 2:
                ind_chicken.append((i, j))  
            elif t == 1:
                ind_home.append((i, j))
    
    return ind_chicken, ind_home, m

def get_min_distance(ind_chicken, ind_home, m):
    remain_comb = combinations(ind_chicken, m)
    
    cumm_dists = []
    for remain_chicken in remain_comb:
        home_dist = [1e9] * len(ind_home)
        for i_c, j_c in remain_chicken:
            for i, (i_h, j_h) in enumerate(ind_home):
                home_dist[i] = min(home_dist[i], abs(i_c - i_h) + abs(j_c - j_h))
        
        cumm_dists.append(sum(home_dist))
    
    return min(cumm_dists)

def main():
    ind_chicken, ind_home, m = get_input()

    min_dist = get_min_distance(ind_chicken, ind_home, m)
    
    print(min_dist)    
    
if __name__ == "__main__":
    main()