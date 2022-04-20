# 프로그래머스 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057
def solution(s):
    
    max_len = len(s) // 2
    
    result = len(s)
    for w in range(1, max_len + 1):
        c_num = 1
        result_string = ""
        for i in range(0, len(s), w):
            if s[i: i + w] == s[i + w: i + 2 * w]:
                c_num += 1
            else:
                result_string += (str(c_num) + str(s[i: i + w])) if c_num > 1 else str(s[i: i + w])
                c_num = 1
        
        result_string += f"{c_num}{s[i: i + w]}" if c_num > 1 else str(s[i + w: i + 2 * w])
        result = min(result, len(result_string))

    return result