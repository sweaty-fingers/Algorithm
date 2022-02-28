from bisect import bisect_left, bisect_right

def solution(words, queries):
    answer = []
    
    words = list(set(words))
    
    words_f = [[] for _ in range(10001)]
    words_b = [[] for _ in range(10001)]
    
    for w in words:
        words_f[len(w)].append(w)
        words_b[len(w)].append(w[::-1])
        
    for i in range(len(words_f)):
        words_f[i].sort()
        words_b[i].sort()

    for q in queries:
        
         if q[0] == "?":
             idx_right = bisect_right(words_b[len(q)], q[::-1].replace("?", "z"))
             idx_left = bisect_left(words_b[len(q)], q[::-1].replace("?", "a"))
            
         else:
             idx_right = bisect_right(words_f[len(q)], q.replace("?", "z"))
             idx_left = bisect_left(words_f[len(q)], q.replace("?", "a"))
           
         answer.append(idx_right - idx_left)

    return answer