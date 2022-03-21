from collections import defaultdict
def solution(food_times, k):
    
    len_food = len(food_times)
    
    food_dict = defaultdict(list)
    for i, time in enumerate(food_times):
        food_dict[time].append(i)
    sorted_food_times = sorted(food_dict.items(), key=lambda x: x[0])
    
    food_left = []
    time_past = 0
    for time, food in sorted_food_times:
        time -= time_past
        
        if time <= k // len_food:
            k -= (time) * len_food
            len_food -= len(food)
            
            if len_food <= 0:
                return -1
            
            time_past += time
        else:
            food_left.extend(food)
    
    food_left.sort()
    k = k % len_food
    return  food_left[k] + 1