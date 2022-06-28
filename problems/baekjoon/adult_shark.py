move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
move_str = ["up", "down", "left", " right"]

import logging
from collections import deque

simple_formatter = logging.Formatter("[%(name)s] %(message)s")
console_handler = logging.StreamHandler()
console_handler.setFormatter(simple_formatter)
console_handler.setLevel(logging.INFO)

root_logger = logging.getLogger()
root_logger.addHandler(console_handler)
root_logger.setLevel(logging.INFO)

shark_moves = {}
shark_direct = []
result = 0
K = 0


def get_input():
    global shark_moves
    global shark_direct
    global K

    n, m, K = map(int, input().split(" "))

    graph = [[] for _ in range(n)]
    shark_dict = {i + 1: deque([]) for i in range(m)}
    for i in range(n):
        row = list(map(int, input().split(" ")))
        for j, r in enumerate(row):
            graph[i].append(r)
            if r != 0:
                shark_dict[r].append([i, j, K])

    shark_direct = [0] + list(map(int, input().split(" ")))

    shark_moves = {i: [] for i in range(1, m + 1)}

    for i in range(1, m + 1):
        shark_moves[i] = [tuple(map(int, input().split(" "))) for _ in range(4)]

    return graph, shark_dict


def remove_idx(shark, graph):
    global K

    for i in range(len(shark)):
        shark[i][-1] -= 1
        
    if shark:
        while shark[0][-1] <= 0:
            y, x, _ = shark.popleft()
            graph[y][x] = 0
            
            if not shark:
                break
    
    return graph

def remove_from_graph(shark, graph):
    for y, x, _ in shark:
        graph[y][x] = 0
    return graph


def move_shark(graph, shark_dict, is_shark):
    global shark_moves
    global shark_direct
    global result
    global K

    n = len(graph)
    m = len(shark_dict)
    
    for i in range(1, m + 1):
        if not is_shark[i]:
            remove_idx(shark_dict[i], graph)
            continue

        y, x, _ = shark_dict[i][-1]
        direct = shark_direct[i]
        is_move = False

        for di in shark_moves[i][direct - 1]:
            y_tmp, x_tmp = y + move[di - 1][0], x + move[di - 1][1]

            if not ((0 <= y_tmp < n) and (0 <= x_tmp < n)):
                continue
            
            if graph[y_tmp][x_tmp] == 0:
                shark_direct[i] = di
                remove_idx(shark_dict[i], graph)
                shark_dict[i].append([y_tmp, x_tmp, K])
                is_move=True
                break
        
        if is_move:
            continue
        
        for di in shark_moves[i][direct - 1]:
            y_tmp, x_tmp = y + move[di - 1][0], x + move[di - 1][1]

            if not ((0 <= y_tmp < n) and (0 <= x_tmp < n)):
                continue

            if graph[y_tmp][x_tmp] == i:
                shark_direct[i] = di
                remove_idx(shark_dict[i], graph)
                shark_dict[i].append([y_tmp, x_tmp, K])
                break

    # if sum(is_shark) == 1:
    #     return result
    
    only_one = True
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] > 1:
                only_one = False
                
    if only_one:
        return result
            
    in_shark = []
    for i in range(1, len(shark_dict) + 1):
        
        if not shark_dict[i]:
            continue
        
        y, x, _ = shark_dict[i][-1]
        if graph[y][x] == 0:
            graph[y][x] = i
        else:
            is_shark[i] = False
            
    result += 1
    
    root_logger.info(f"result: {result}")
    root_logger.info("graph")
    for g in graph:
        root_logger.info(g)
    root_logger.info(f"n_shark = {sum(is_shark)}")
    root_logger.info("shark")
    root_logger.info(f"{shark_dict}")
    root_logger.info("")
    root_logger.info("")
    root_logger.info("-" * 60)
    input(" ")
    
    move_shark(graph, shark_dict, is_shark)


def main():
    global K
    global result
    graph, shark_dict = get_input()
    is_shark = [False] + [True] * K
    root_logger.info("")
    root_logger.info("graph")
    for g in graph:
        root_logger.info(g)

    root_logger.info(shark_dict)
    move_shark(graph, shark_dict, is_shark)
    
    print(result)


if __name__ == "__main__":
    main()