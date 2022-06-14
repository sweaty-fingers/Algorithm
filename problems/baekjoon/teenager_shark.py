move = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

import logging
from collections import defaultdict
import copy

simple_formatter = logging.Formatter("[%(name)s] %(message)s")
console_handler = logging.StreamHandler()
console_handler.setFormatter(simple_formatter)
console_handler.setLevel(logging.INFO)

root_logger = logging.getLogger()
root_logger.addHandler(console_handler)
root_logger.setLevel(logging.INFO)

result = 0

def default_value():
    return (-1, -1)


def get_input():
    graph = [[] for _ in range(4)]

    for i in range(4):
        line = list(map(int, input().split(" ")))
        for j in range(0, len(line), 2):
            root_logger.debug(f"{i}")
            graph[i].append([line[j], line[j + 1] - 1])

    return graph


def move_fish(graph):  
    fish_dic = defaultdict(default_value)

    for i in range(4):
        for j in range(4):
            if graph[i][j][0] == 0:
                continue
            fish_dic[graph[i][j][0]] = (i, j)

    for i in range(1, 17):
        y, x = fish_dic[i]

        if y == -1 or x == -1:  # 존재하지 않을 경우 넘기기
            continue

        fish_size, direction = graph[y][x][0], graph[y][x][1]

        for j in range(8):
            di = (direction + j) % 8
            dy, dx = move[di]
            y_tmp, x_tmp = y + dy, x + dx

            if not ((0 <= y_tmp < 4) and (0 <= x_tmp < 4)):
                continue

            if graph[y_tmp][x_tmp][0] == -2:  # 상어
                continue

            if 0 <= graph[y_tmp][x_tmp][0] <= 16:
                fish_size_changed, fish_di_changed = graph[y_tmp][x_tmp][0], graph[y_tmp][x_tmp][1]

                graph[y_tmp][x_tmp][0], graph[y_tmp][x_tmp][1] = fish_size, di
                graph[y][x][0], graph[y][x][1] = fish_size_changed, fish_di_changed

                fish_dic[fish_size] = (y_tmp, x_tmp)
                fish_dic[fish_size_changed] = (y, x)
                break

    return graph

def get_fish_position(graph, y, x, di):
    
    positions = []
    for _ in range(4):
        y, x = y + move[di][0], x + move[di][1]

        if not ((0 <= y < 4) and (0 <= x < 4)):
            break
        
        if 1 <= graph[y][x][0] <= 16:
            positions.append((y, x))
        
    return positions
    

def eat_fish(graph, y, x, total):
    global result
    
    graph = copy.deepcopy(graph)
    total += graph[y][x][0]
    graph[y][x][0] = -2
    
    graph = move_fish(graph)
    graph[y][x][0] = 0
    
    positions = get_fish_position(graph, y, x, graph[y][x][1])
    
    if not positions:
        result = max(result, total)
    
    for y, x in positions:
        eat_fish(graph, y, x, total)    
    

def main():
    
    graph = get_input()
    for g in graph:
        root_logger.debug(f"{g}")

    eat_fish(graph, 0, 0, 0)
    print(result)
    
    
if __name__ == "__main__":
    main()
