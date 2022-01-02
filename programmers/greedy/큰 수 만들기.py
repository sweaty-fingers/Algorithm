# time out error로 풀리지 않음.
def solution(number, k):
    
    num_origin = number
    total_len = len_need = len(number) - k
    
    value = ""
    
    idx = number.index(max(number))
    
    while len_need:
        if len(number[idx:]) >= len_need:
            value += number[idx]
            len_need -= 1
            number = number[idx+1:]
            if not number:
                break
            idx = number.index(max(number))
        else:
            idx = number.index(max(number[:idx]))
    
    return value