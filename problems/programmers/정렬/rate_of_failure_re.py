# https://programmers.co.kr/learn/courses/30/lessons/42889
# 실패율

def solution(N, stages):
    
    n_each_stage = [0] * (N + 2)
    
    for s in stages:
        n_each_stage[s] += 1
    
    total_players = len(stages)
    failure_rates = []
    players_cumm = 0
    for i, s in enumerate(n_each_stage):
        if i == 0 or i == len(n_each_stage) - 1:
            continue
            
        n_on_stage = total_players - players_cumm
        players_cumm += s
        
        if n_on_stage == 0:
            fr = 0
        else:
            fr = s / n_on_stage
            
        failure_rates.append((fr, i))
    
    failure_rates = sorted(failure_rates, key=lambda x: x[1])
    failure_rates = sorted(failure_rates, key=lambda x: x[0], reverse=True)
 
    answer = []
    for f in failure_rates:
        answer.append(f[1])
        
    return answer