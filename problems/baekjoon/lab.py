import logging
from collections import deque
from copy import deepcopy

simple_formatter = logging.Formatter("[%(name)s] %(message)s")
console_handler = logging.StreamHandler()
console_handler.setFormatter(simple_formatter)
console_handler.setLevel(logging.INFO)

root_logger = logging.getLogger()
root_logger.addHandler(console_handler)
root_logger.setLevel(logging.WARNING)

parent_logger = logging.getLogger("parent")
parent_logger.setLevel(logging.WARNING)


move = [(1, 0), (0, 1), (-1, 0), (0, -1)] # 상하좌우

N, M = map(int, input().split(" "))

def get_input():
    map_size = N * M
    map_array = []
    for _ in range(N):
        map_array.append(list(map(int, input().split(" "))))
    
    return map_array, map_size
        

def bfs(map_array):
    q = deque([])
    n = len(map_array)
    m = len(map_array[0])
    for i in range(len(map_array)):
        for j in range(len(map_array[0])):
            if map_array[i][j] == 2:
                q.append((i, j))
                
                while q:
                    y, x = q.popleft()
                    
                    
                    for dy, dx in move:
                        y_temp, x_temp = y + dy, x + dx
                        
                        if not ((0 <= y_temp < N) and (0 <= x_temp < M)):
                            continue
                        
                        if map_array[y_temp][x_temp] == 1 or map_array[y_temp][x_temp] == 2:
                            continue
                        
                        if map_array[y_temp][x_temp] == 0:
                            map_array[y_temp][x_temp] = 2
                            q.append((y_temp, x_temp))
    
    return map_array


def get_num(map_array):
    result = 0
    for i in range(N):
        for j in range(M):
            if map_array[i][j] == 0:
                result += 1
                
    return result


def main():
    map_array, map_size = get_input()
    
    parent_logger.info(f"map_size: {map_size}")
    parent_logger.info(f"n: {N}, m: {M}")
    
    for m in map_array:
        parent_logger.info(f"{m[:]}")
    parent_logger.info(f"-" * 10)
        
    result = 0
    
    for i_1 in range(N):
        for j_1 in range(M):
            if map_array[i_1][j_1] != 0:
                continue
            
            map_array[i_1][j_1] = 1
            for i_2 in range(N):
                for j_2 in range(M):
                    if map_array[i_2][j_2] != 0:
                        continue
                    
                    map_array[i_2][j_2] = 1
                    
                    for i_3 in range(N):
                        for j_3 in range(M):
                            if map_array[i_3][j_3] != 0:
                                continue
                            
                            map_array[i_3][j_3] = 1
                            
                            # for m in map_array:
                            #     parent_logger.debug(f"{m[:]}")
        
                            # parent_logger.debug("-" * 10)
                            
                            map_temp = bfs(deepcopy(map_array))
                            
                            # for m in map_temp:
                            #     parent_logger.info(f"{m[:]}")
                            #input()
                            
                            
                            result = max(result, get_num(map_temp))

                            map_array[i_3][j_3] = 0
                            
                            # for m in map_array:
                            #     parent_logger.debug(f"{m[:]}")
                            
                            # parent_logger.debug(f"{result}")
                            # parent_logger.debug("-" * 10)
                            # parent_logger.debug("-" * 10)
                    
                    map_array[i_2][j_2] = 0
            
            map_array[i_1][j_1] = 0
    
    print(result)
                
            
if __name__ == "__main__":
    main()