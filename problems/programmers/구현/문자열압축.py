# 문자열은 맨 앞부터 압축가능 한 것을 놓침.
def solution(s):
    answer = len(s)
    comp_len = len(s) // 2

    while comp_len >= 1:
        comp_s = ""
        comp_temp = ""
        iter_s = ""
        iter_num = 0
        i = 0
        while i < (len(s)-comp_len):
            if s[i] == s[i+comp_len]:
                comp_temp += s[i]
                
                if len(comp_temp) == comp_len:
                    iter_num +=1
                    iter_s = comp_temp
                    comp_temp = ""
                i += 1
            elif iter_num != 0:
                comp_s += str(iter_num + 1) + iter_s
                iter_num = 0
                iter_s = ""
                comp_temp = ""
                i += comp_len
            else:
                comp_s += comp_temp + s[i]
                comp_temp = ""
                i += 1
            
        if iter_num != 0:
            comp_s += str(iter_num + 1) + iter_s
        else:
            comp_s += comp_temp + s[len(s)-comp_len:]
        
        
        answer = min(answer, len(comp_s))
        comp_len -= 1
        
    
    return answer



def solution(s):
    answer = len(s)
    comp_len = len(s) // 2

    while comp_len >= 1:
        comp_s = ""
        iter_num = 1
        prev = s[0:comp_len]
        for i in range(comp_len, len(s), comp_len):
            if prev == s[i:i+comp_len]:
                iter_num +=1
            else:
                comp_s += str(iter_num) + prev if iter_num >= 2 else prev
                iter_num = 1
                prev = s[i:i+comp_len]
        
        comp_s += str(iter_num) + prev if iter_num >= 2 else prev
        answer = min(answer, len(comp_s))
        comp_len -= 1
    
    return answer