from copy import deepcopy
from collections import deque

move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def get_input():
    n, m = map(int, input().split(" "))
    
    graph = [list(map(int, input().split(" "))) for _ in range(n)]
    
    return graph

def get_large_group(graph):

    n = len(graph)
    seen = set()
    group = []
    max_len = 0
    max_rainbow = 0
    # num_normal = 0
    
    for i in range(n):
        for j in range(n):
            group_tmp = set()
            rainbow_tmp = 0
            num_normal = 0
            
            if (i, j) in seen:
                continue
            if graph[i][j] <= 0:
                continue
            
            # print(group_tmp)
            m = graph[i][j]
            q = deque([(i, j)])
            
            group_tmp.add((i, j))
            seen.add((i, j))
            
            while q:
                y, x = q.popleft()
                
                for dy, dx in move:
                    y_tmp, x_tmp = y + dy, x + dx
                    
                    if not ((0 <= y_tmp < n) and (0 <= x_tmp < n)):
                        continue
                
                    if graph[y_tmp][x_tmp] == -1:
                        continue
                    
                    if (y_tmp, x_tmp) not in group_tmp:
                        if (graph[y_tmp][x_tmp] == m or graph[y_tmp][x_tmp] == 0): 
                            group_tmp.add((y_tmp, x_tmp))
                            q.append((y_tmp, x_tmp))
                            
                            if graph[y_tmp][x_tmp] == 0:
                                rainbow_tmp += 1
                            else:
                                num_normal += 1
                                seen.add((y_tmp, x_tmp))

            
            if len(group_tmp) < 2:
                # print(group_tmp)
                # print("continue")
                continue
            
            if len(group_tmp) > max_len:
                max_rainbow = rainbow_tmp
                max_len = len(group_tmp)
                group = deepcopy(group_tmp)
            
            if len(group_tmp) >= max_len:
                if rainbow_tmp >= max_rainbow:
                    max_rainbow = rainbow_tmp
                    max_len = len(group_tmp)
                    group = deepcopy(group_tmp)
                    # print(group)
                    # print("-" * 30)
            
                    

    if len(group) == max_rainbow:
        group = []
    
    return group


def remove_blocks(graph, group, score):
    n = len(group)
    for i, j in group:
        graph[i][j] = -2
    
    score += (n ** 2)
    return graph, score


def gravity(graph):
    
    n = len(graph)
    dy, dx = 1, 0
    
    for i in range(n - 2, -1, -1):
        for j in range(n):
            if graph[i][j] < 0:
                continue
            
            bottom = False
            # print(f"i, j: {i}, {j}")
            y, x = i, j
            while not bottom:
                y_tmp, x_tmp = y + dy, x + dx
                
                
                if not ((0 <= y_tmp < n) and (0 <= x_tmp < n)):
                    bottom = True
                    continue
                
                # print(graph[y][x])
                # print(graph[y_tmp][x_tmp])    
                
                if graph[y_tmp][x_tmp] == -2:
                    graph[y_tmp][x_tmp] = graph[y][x]
                    graph[y][x] = -2
                    y, x = y_tmp, x_tmp
                    
                else:
                    bottom = True
            # print("-" * 30)
                    
    return graph


def rotate(graph):
    n = len(graph)
    graph_new = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            graph_new[n - 1 - j][i] = graph[i][j]
    
    return graph_new    

def main():
    graph = get_input()
    
    if len(graph) == 1:
        print(0)
            
        return
            
    score = 0
    
    end = False
    
    while not end:
        group = get_large_group(graph)
        # print("step")
        # print(group)
        # print("step")
        
        if not group or (len(group) < 2):
            end = True
            continue
            
        graph, score = remove_blocks(graph, group, score)

        # for g in graph:
        #     print(g)
        # print(score)
        
        graph = gravity(graph)
        # for g in graph:
        #     print(g)
        # print("-" * 30)
        graph = rotate(graph)
        # for g in graph:
        #     print(g)
        # print("-" * 30) 
        graph = gravity(graph)
        # for g in graph:
        #     print(g)
        # print("-" * 30)
    
    print(score)
    

if __name__ == "__main__":
    main()
    