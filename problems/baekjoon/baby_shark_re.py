import logging
from collections import deque

simple_formatter = logging.Formatter("[%(name)s] %(message)s")
console_handler = logging.StreamHandler()
console_handler.setFormatter(simple_formatter)
console_handler.setLevel(logging.WARNING)

root_logger = logging.getLogger()
root_logger.addHandler(console_handler)
root_logger.setLevel(logging.WARNING)


move = [(-1, 0), (0, -1), (0, 1), (1, 0)] # 상 좌 우 하


def get_input():
    n = int(input())
    
    graph = [list(map(int, input().split(" "))) for _ in range(n)]
    
    return graph


def get_fish(graph, y, x, size_shark):
    
    n = len(graph)
    fish_dist = [[-1] * n for _ in range(n)]
    fish_dist[y][x] = 0 
    root_logger.info("-" * 30)
    
    q = deque([(y, x)]) # (y, x, t)
    n_fish = 0
    
    while q:
        y, x = q.popleft()
        
        for dy, dx in move:
            y_tmp, x_tmp = y + dy, x + dx
            
            if not ((0 <= y_tmp < n) and (0 <= x_tmp < n)):
                continue
            
            
            if graph[y_tmp][x_tmp] <= size_shark and fish_dist[y_tmp][x_tmp] == -1:
                fish_dist[y_tmp][x_tmp] = fish_dist[y][x] + 1
                q.append((y_tmp, x_tmp))
                
                if 0 < graph[y_tmp][x_tmp] < size_shark:
                    n_fish += 1
                
    
    return fish_dist, n_fish


def get_time(graph):
    
    n = len(graph)

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 9:
                y = i
                x = j 
                graph[i][j] = 0
    
    
    size_shark = 2
    t = 0
    n_ate = 0
    
    while True:
        
        fish_dist, n_fish = get_fish(graph, y, x, size_shark)
        
        for f in fish_dist:
            root_logger.info(f"{f}")
        if n_fish == 0:
            break
        
        min_dist = 1e9
            
        for i in range(n):
            for j in range(n):
                if 0 < graph[i][j] < size_shark and 0 < fish_dist[i][j] < min_dist:
                    min_dist = fish_dist[i][j]
                    min_y = i
                    min_x = j
        
        t += min_dist
        n_ate += 1
        graph[min_y][min_x] = 0
        y = min_y
        x = min_x

        if n_ate >= size_shark:
            size_shark += 1
            n_ate = 0
            
    return t

def main():
    graph = get_input()
    
    for g in graph:
        root_logger.info(f"{g}")
        
    print(get_time(graph))
    
if __name__ == "__main__":
    main()