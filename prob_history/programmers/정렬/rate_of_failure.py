# https://programmers.co.kr/learn/courses/30/lessons/42889
from collections import Counter, defaultdict
def solution(N, stages):
    remain_players = len(stages)

    stage_dict = defaultdict(int)
    for key, value in Counter(stages).items():
        stage_dict[key] = value
        
    fail_rate = {}    
    for key in range(1, N + 1):
        
        fail = stage_dict[key]
        fail_rate[key] = fail / remain_players
        
        remain_players -= stage_dict[key]
        if remain_players == 0:
            for key in range(key + 1, N + 1):
                fail_rate[key] = 0
            break
            
    return sorted(fail_rate, key=lambda x : -fail_rate[x])