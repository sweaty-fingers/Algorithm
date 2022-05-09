# 프로그래머스 블록 움직이기
# https://programmers.co.kr/learn/courses/30/lessons/60063
from collections import deque

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def check_out_of_bound(y, x):
    global n
    
    if not ((0 <= y < n) and (0 <= x < n)):
        return True
    
    return False

            
def rotate_1(py, px, ry, rx):
    global b
    
    if py == ry:
        if check_out_of_bound(py - 1, px) or check_out_of_bound(ry - 1, rx):
            return False
            
        if b[py - 1][px] != 1 and b[ry - 1][rx] != 1:
            return py, px, py - 1, px
        
    if px == rx:
        if check_out_of_bound(py, px + 1) or check_out_of_bound(ry + 1, rx):
            return False

        if b[py][px + 1] != 1 and b[ry][rx + 1] != 1:
            return py, px, py, px + 1
            
    return False
        

def rotate_2(py, px, ry, rx):
    global b
    
    if py == ry:
            
        if check_out_of_bound(py - 1, px) or check_out_of_bound(ry - 1, rx):
            return False
            
        if b[py - 1][px] != 1 and b[ry - 1][rx] != 1:
            return ry - 1, rx, ry, rx
    
    if px == rx:
            
        if check_out_of_bound(py, px + 1) or check_out_of_bound(ry, rx + 1):
            return False
            
        if b[py][px + 1] != 1 and b[ry][rx + 1] != 1:
            return ry, rx + 1, ry, rx
        
    return False

            
def rotate_3(py, px, ry, rx):
    global b
    if py == ry:
        if check_out_of_bound(py + 1, px) or check_out_of_bound(ry + 1, rx):
            return False
            
        if b[py + 1][px] != 1 and b[ry + 1][rx] != 1:
            return py, px, py + 1, px
            
        
    if px == rx:
        if check_out_of_bound(py, px - 1) or check_out_of_bound(ry, rx - 1):
            return False
            
        if b[py][px - 1] != 1 and b[ry][rx - 1] != 1:
            return py, px, py, px - 1
    
    return False
    
    
def rotate_4(py, px, ry, rx):
    global b
    if py == ry:
            
        if check_out_of_bound(py + 1, px) or check_out_of_bound(ry + 1, rx):
            return False
            
        if b[py + 1][px] != 1 and b[ry + 1][rx] != 1:
            return ry + 1, rx, ry, rx
        
    if px == rx:
            
        if check_out_of_bound(py, px - 1) or check_out_of_bound(ry, rx - 1):
            return False
            
        if b[py][px - 1] != 1 and b[ry][rx - 1] != 1:
            return ry, rx - 1, ry, rx
    
    return False


rotate = [rotate_1, rotate_2, rotate_3, rotate_4]
    
def solution(board):
            
    answer = 0
    q = deque([(0, 0, 0, 0, 1)]) # t y1, x1, y2, x2
    seen = [(0, 0, 0, 1), (0, 1, 0, 0)]
    
    global n
    global b
    b = board
    n = len(board)
    
    while q:
        # t, y1, x1, y2, x2 = q.popleft()
        t, y1, x1, y2, x2 = q.popleft()
        if (y1 == n - 1 and x1 == n - 1) or (y2 == n - 1 and x2 == n - 1):
            return t
        
        for dy, dx in move:
            
            y1_tmp, x1_tmp, y2_tmp, x2_tmp = y1 + dy, x1 + dx, y2 + dy, x2 + dx
            
            if check_out_of_bound(y1_tmp, x1_tmp) or check_out_of_bound(y2_tmp, x2_tmp):
                continue
                
            if b[y1_tmp][x1_tmp] == 1 or b[y2_tmp][x2_tmp] == 1:
                continue
                
            if (y1_tmp, x1_tmp, y2_tmp, x2_tmp) in seen or ((y1_tmp, x1_tmp, y2_tmp, x2_tmp) in seen):
                continue
            
            q.append((t + 1, y1_tmp, x1_tmp, y2_tmp, x2_tmp))
            seen.extend([(y1_tmp, x1_tmp, y2_tmp, x2_tmp), (y2_tmp, x2_tmp, y1_tmp, x1_tmp)])
        
        for r in rotate:
            if not r(y1, x1, y2, x2):
                continue
            else:
                y1_tmp, x1_tmp, y2_tmp, x2_tmp = r(y1, x1, y2, x2)
            
            if (y1_tmp, x1_tmp, y2_tmp, x2_tmp) in seen or (y1_tmp, x1_tmp, y2_tmp, x2_tmp) in seen:
                continue
                
            q.append((t + 1, y1_tmp, x1_tmp, y2_tmp, x2_tmp))
            seen.extend([(y1_tmp, x1_tmp, y2_tmp, x2_tmp), (y2_tmp, x2_tmp, y1_tmp, x1_tmp)])
        
            
    return t