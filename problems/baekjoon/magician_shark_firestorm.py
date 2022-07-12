from copy import deepcopy
from collections import deque

MOVE = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def get_input():
    n, q = map(int, input().split(" "))
    n = 2**n
    
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split(" "))))
        
    
    stages = list(map(int, input().split(" ")))
    
    return graph, stages


def rotate_subgraph(graph, l):
    
    step = 2 ** l
    n = len(graph) // step
    
    rotated_graph = [[0] * len(graph) for _ in range(len(graph))]

    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, step):
                for l in range(0, step):
                    rotated_graph[i * step + l][step * (j + 1) - 1 - k] = graph[i * step + k][j * step + l]

    # for r in rotated_graph:
    #     print(r)
    # input()
            
    return rotated_graph
        

def bfs(graph):
    
    seen = set()
    n = len(graph)
    
    for i in range(n):
        for j in range(n):
            if (i, j) in seen or graph[i][j] <= 0:
                continue
            
            q = deque([(i, j)])
            melt_list = []
            
            while q:
                y, x = q.popleft()
                
                if (y, x) in seen:
                    continue
                
                seen.add((y, x))
                
                inject_ice = 0    
                for dy, dx in MOVE:
                    y_tmp, x_tmp = y + dy, x + dx
                    
                    if not ((0 <= y_tmp < n) and (0 <= x_tmp < n)):
                        continue
                    
                    if graph[y_tmp][x_tmp] <= 0:
                        continue
                    
                    inject_ice += 1
                    
                    if (y_tmp, x_tmp) not in seen:
                        q.append((y_tmp, x_tmp))

                if inject_ice < 3 and graph[y][x] > 0:
                    melt_list.append((y, x))
            
            for y, x in melt_list:
                graph[y][x] -= 1
                
            # print(seen)
            # input()
                
            # print(num_ice)
            # print(len(seen))
            # assert num_ice == len(seen)
    
    return graph


def get_max_ice(graph):
    
    seen = set()
    n = len(graph)
    
    max_ice_size = 0
    for i in range(n):
        for j in range(n):
            if (i, j) in seen or graph[i][j] <= 0:
                continue
            
            q = deque([(i, j)])
            ice_size = 0
            
            while q:
                y, x = q.popleft()
                # print("?")
                
                if (y, x) in seen:
                    continue
                
                seen.add((y, x))
                ice_size += 1
                
                for dy, dx in MOVE:
                    y_tmp, x_tmp = y + dy, x + dx
                    
                    if not ((0 <= y_tmp < n) and (0 <= x_tmp < n)):
                        continue
                    
                    if graph[y_tmp][x_tmp] <= 0:
                        continue
                    
                    if (y_tmp, x_tmp) not in seen:
                        q.append((y_tmp, x_tmp))
            
            max_ice_size = max(ice_size, max_ice_size)

    return max_ice_size
                    

def main():
    graph, stages = get_input()
    n = len(graph)
    # for g in graph:
    #     print(g)
    
    # print(stages)

    for s in stages:
        graph = rotate_subgraph(graph, s)
        graph = bfs(graph)
        
        # print(f"stage: {s}")
        # for g in graph:
        #     print(g)
        # input()
    
    
    total_ice = 0
    for i in range(n):
        for j in range(n):
            total_ice += graph[i][j]
            
    max_ice_num = get_max_ice(graph)
    print(total_ice)
    print(max_ice_num)


if __name__ == "__main__":
    main()