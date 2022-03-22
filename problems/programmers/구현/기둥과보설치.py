def check_construct(temp, result):
    x, y, a = temp
    
    beam_left = [x - 1, y, 1]
    beam_right = [x + 1, y, 1]
    beam_beneath = [x, y, 1]
    pillar_under = [x, y - 1, 0]
    pillar_below_right = [x + 1, y - 1, 0]
    
    if a == 0: #기둥
        if y == 0:
            if temp not in result:
                result.append(temp)
            return True   
            
        test_cases = [beam_left, beam_beneath, pillar_under]
        
    else: # 보
        if beam_left in result and beam_right in result:
            if temp not in result:
                result.append(temp)
            return True
        
        test_cases = [pillar_under, pillar_below_right]
        
    for test_case in test_cases:
        if test_case in result:
            if temp not in result:
                result.append(temp)
            return True
        
    return False

def check_distruct(temp, result):
    
    x, y, a = temp
    beam_on = [x, y + 1, 1]
    beam_above_left = [x - 1, y + 1, 1]
    pillar_above = [x, y + 1, 0]

    pillar_on = [x, y, 0]
    pillar_right = [x + 1, y, 0]
    beam_left = [x - 1, y, 1]
    beam_right = [x + 1, y, 1]

    if a == 0:
        test_cases = [beam_on, beam_above_left, pillar_above]   
    else:
        test_cases = [pillar_on, pillar_right, beam_left, beam_right]

    for test_case in test_cases:

        if test_case in result:
            test_case = result.pop(result.index(test_case))

            if not check_construct(test_case, result):
                result.append(test_case)
                result.append(temp)
                break


def solution(n, build_frame):
    
    result = []
    
    for frame in build_frame:
        x, y, a, b = frame
        temp = [x, y, a]
        
        if b == 1:
            if temp in result:
                continue
            check_construct(temp, result)
        
        else:
            if temp in result:
                result.pop(result.index(temp))
            else:
                continue
                
            check_distruct(temp, result)

    result.sort()
    print(result)
    return result