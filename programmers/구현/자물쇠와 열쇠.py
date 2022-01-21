def rotate_90(key):
    m = len(key)
    
    li = []
    for r in range(m):
        row_ = []
        for c in range(m):
            row_.append(0)
        li.append(row_)
            
    for i in range(m):
        for j in range(m):
            li[m - 1 - j][i] = key[i][j]
    
    return li

# def check(lock):
#     for row in lock:
#         if sum(row) != len(lock):
#             return False
#     return True

def check(lock):
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] != 1:
                return False
    return True
            
        
def solution(key, lock):
    m = len(key)
    n = len(lock)
    
    if check(lock):
        return True
    
    for _ in range(4):
        key = rotate_90(key)
        for i in range(n + m - 1):
            for j in range(n + m - 1):
                for y in range(m):
                    for x in range(m):
                        if i - y < 0 or j - x < 0 or i - y > n - 1 or j - x > n - 1:
                            continue
                        lock[i - y][j - x] += key[m-1-y][m-1-x]
            
                if check(lock):
                    return True
                
                for y in range(m):
                    for x in range(m):
                        if i - y < 0 or j - x < 0 or i - y > n - 1 or j - x > n - 1:
                            continue
                        lock[i - y][j - x] -= key[m - 1 - y][m - 1 - x]
        
    return False