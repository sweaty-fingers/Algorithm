# 프로그래머스 외벽 점검
# https://programmers.co.kr/learn/courses/30/lessons/60062
from itertools import permutations
def solution(n, weak, dist):
    
    w_len = len(weak)
    for i in range(w_len):
        weak.append(weak[i] + n)
        
    f_permut = permutations(dist, len(dist))
    result = len(dist) + 1
    
    for f_subset in f_permut:
        for s_idx in range(w_len):
            # print(f_subset)
            count = 1
            end = weak[s_idx] + f_subset[count - 1]
    
            for i in range(s_idx, s_idx + w_len):
                if end < weak[i]:
#                     print(f"weak: {weak[i]}")
#                     print(f"end: {end}")
                    
                    count += 1
                    if count > len(dist):
                        break
                    end = weak[i] + f_subset[count - 1]
                    # print(f"end_new: {end}")
                    # print(f"f: {f_subset[count - 1]}")
                    # print("-"* 10)
            
            result = min(result, count)
#             print(f"result: {result}")
                
    if result > len(dist):
        return -1
        
    return result