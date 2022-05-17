def bisect_left(array: list, target: str, start=0, end=None):
    if not end:
        end = len(array)
    
    while start < end:
        mid = start + (end - start) // 2
        
        if array[mid] < target:
            start = mid + 1
        else:
            end = mid
            
    return start

    
def bisect_right(array: list, target: str, start=0, end=None):
    
    if not end:
        end = len(array)
        
    while start < end:
        mid = start + (end - start) // 2
        
        if array[mid] > target:
            end = mid
        else:
            start = mid + 1

    return start

    
def solution(words, queries):
    answer = []
    
    words = list(set(words))
    
    words_by_len = [[] for _ in range(100001)]
    reversed_words_by_len = [[] for _ in range(100001)]
    
    
    for w in words:
        words_by_len[len(w)].append(w)
        reversed_words_by_len[len(w)].append(w[::-1])
    
    for _ in range(len(words_by_len)):
        words_by_len[_].sort()
        reversed_words_by_len[_].sort()
    
    for q in queries:
        is_post = q.index("?")
        
        if is_post:
            array = words_by_len[len(q)]
        else:
            array = reversed_words_by_len[len(q)]
            q = q[::-1]
        
        if array is None:
            answer.append(0)
            continue
            
        first = q.replace("?","a")
        end = q.replace("?","z")
        
        count = bisect_right(array, end) - bisect_left(array, first)
        answer.append(count)
        
    return answer