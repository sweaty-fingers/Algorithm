from itertools import permutations

def return_num_of_f(weak, dist_list, n):
    # print("-" * 20)
    # print(f"dist_list : {dist_list}")
    for start in range(len(weak)):
        i = start
        checked = []
        node_pre = weak[start]
        for l, d in enumerate(dist_list):
            # print(f"d: {d}")
            dist_temp = 0
            while True:
                temp_ = weak[i] - node_pre
                node_pre = weak[i]
                
                if temp_ < 0:
                    temp_ += n
                    
                dist_temp += temp_
                
                if dist_temp > d:
                    # print("break")
                    # print("-" * 20)
                    break
                
                checked.append(weak[i])
                i = (i + 1) % len(weak)
                # print(checked)
                
                if len(checked) == len(weak):
                    return l + 1
    return -1

def solution(n, weak, dist):
    if n < max(dist):
        return 1
    
    answer = -1
    min_dist = len(dist) + 1
    for i in range(1, len(dist) + 1):
        for d in permutations(dist, i):
            answer = return_num_of_f(weak, d, n)
            if answer != -1:
                min_dist = min(answer, min_dist)
    if min_dist <= len(dist):
        return min_dist 

    return -1