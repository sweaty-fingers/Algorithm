import logging
from collections import defaultdict
import sys
sys.setrecursionlimit(5000)
#print(sys.getrecursionlimit())

simple_formatter = logging.Formatter("[%(name)s] %(message)s")
console_handler = logging.StreamHandler()
console_handler.setFormatter(simple_formatter)
console_handler.setLevel(logging.INFO)

root_logger = logging.getLogger()
root_logger.addHandler(console_handler)
root_logger.setLevel(logging.WARNING)

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def get_input():
    n, m, k = map(int, input().split(" "))
    
    graph = []
    for _ in range(n):
        
        li_tmp = [[i, k] if i > 0 else [i, 0] for i in list(map(int, input().split(" ")))]
        graph.append(li_tmp)
    
    
    shark_dict = {}
    shark_direct = list(map(int, input().split(" ")))
    for i in range(n):
        for j in range(n):
            if graph[i][j][0] > 0:
                shark = graph[i][j][0]
                shark_dict[shark] = [i, j, shark_direct[shark - 1]]
    
    moves_dict = {}
    for i in range(1, m + 1):
        moves_tmp = []
        for _ in range(4):
            moves_tmp.append(list(map(int, input().split(" "))))
        
        moves_dict[i] = moves_tmp
    
    return graph, moves_dict, shark_dict, k


def step(graph, move_dict, shark_dict, k, result, remain_sharks):
    
    
    if sum(remain_sharks) == 1:
        return result
    
    if result >= 1000:
        return -1
    
    root_logger.info(f"step: {result}")
    root_logger.info("shark_dict")
    for s in range(1, len(shark_dict) + 1):
        root_logger.info(f"{s}: {shark_dict[s]}")
        
        
    root_logger.info("graph")
    for g in graph:
        root_logger.info(g)
    
    # input()
    n = len(graph)
    moves_tmp = []
    
    for s in range(1, len(remain_sharks)):
        if not remain_sharks[s]:
            continue
        is_move = False
        y, x, direct = shark_dict[s]
        
        for d in move_dict[s][direct - 1]:
            dy, dx = move[d - 1]
            y_tmp, x_tmp = y + dy, x + dx
            
            if not ((0 <= y_tmp < n) and (0 <= x_tmp < n)):
                continue
            
            if graph[y_tmp][x_tmp][0] == 0:
                is_move = True
                moves_tmp.append((y_tmp, x_tmp, s, d))
                break
            
        if is_move:
            continue
        
        for d in move_dict[s][direct - 1]:
            dy, dx = move[d - 1]
            y_tmp, x_tmp = y + dy, x + dx
            
            if not ((0 <= y_tmp < n) and (0 <= x_tmp < n)):
                continue
            
            if graph[y_tmp][x_tmp][0] == s:
                is_move = True
                shark_dict[s] = [y_tmp, x_tmp, d]
                graph[y_tmp][x_tmp][0], graph[y_tmp][x_tmp][1] = s, k + 1
                break
    
    moves_tmp = sorted(moves_tmp, key=lambda x: x[-2], reverse=False)
    for y_tmp, x_tmp, s, d in moves_tmp:
        if graph[y_tmp][x_tmp][0] != 0:
            shark_dict[s] = []
            remain_sharks[s] = False
            continue
        graph[y_tmp][x_tmp][0], graph[y_tmp][x_tmp][1] = s, k + 1
        shark_dict[s] = [y_tmp, x_tmp, d]
    
    graph = remove_smell(graph)
    result += 1
    return step(graph, move_dict, shark_dict, k, result, remain_sharks)
    

def remove_smell(graph):
   
    n = len(graph)
   
    for i in range(n):
        for j in range(n):
            if graph[i][j][0] > 0:
                graph[i][j][1] -= 1
                if graph[i][j][1] <= 0:
                    graph[i][j][0], graph[i][j][1] = 0, 0

    return graph
    
# def sum_shark(graph):
#     result = 0
#     n = len(graph)
#     for i in range(n):
#         for j in range(n):
#             result += graph[i][j][0]

def main():
    graph, move_dict, shark_dict, k = get_input()
    root_logger.info(f"k: {k}")
        
    root_logger.info("move_dict")
    for m in range(1, len(move_dict) + 1):
        root_logger.info(f"{m}: {move_dict[m]}")
        
    for s in range(len(shark_dict)):
        root_logger.info(shark_dict[s + 1])
    
    remain_sharks = [False] + [True] * len(shark_dict)
    print(step(graph, move_dict, shark_dict, k, 0, remain_sharks))
        

if __name__ == "__main__":
    main()