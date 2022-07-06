from collections import deque

MOVE = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
SKEW_MOVE = [1, 3, 5, 7]

def get_input():
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    
    steps = deque([])
    
    for _ in range(m):
        d, s = map(int, input().split(" "))
        steps.append((d, s))
        
    cloud_pos = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]
    
    return graph, steps, cloud_pos

def move_cloud(cloud_pos, step, n):
    """
    step은 steps의 하나를 받음
    n 은 그래프 크기
    """
    d, s = step
    dy, dx = MOVE[d - 1]
    # print("before")
    # print_cloud(cloud_pos)
    
    cloud_pos = [((y + (dy * s)) % n, (x + (dx * s)) % n) for y, x in cloud_pos]
    # print("after")
    # print_cloud(cloud_pos)

    return cloud_pos
    
    
def fill_basket(graph, cloud_pos):
    
    # print("before")
    # print_graph(graph)
    for y, x in cloud_pos:
        graph[y][x] += 1
    
    # print("after")
    # print_graph(graph)
    
    return graph

def duplicate_water(graph, cloud_pos):
    """
    cloud_pos == 이전 물이 증가한 위치
    물복사를 할때는 끝과 처음 행렬이 이어져있지 않다.
    """
    n = len(graph)
    
    # print("before")
    # print_graph(graph)
    
    for y, x in cloud_pos:
        for i in SKEW_MOVE:
            dy, dx = MOVE[i]
            y_tmp, x_tmp = y + dy, x + dx
            
            if not ((0 <= y_tmp < n) and (0 <= x_tmp < n)):
                continue
            
            if graph[y_tmp][x_tmp] != 0:
                graph[y][x] += 1
    
    # print("after")
    # print_graph(graph)
    
    return graph


def generate_cloud(graph, cloud_pos):
    
    new_cloud_pos = []
    n = len(graph)
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 2 and (i, j) not in cloud_pos:
                new_cloud_pos.append((i, j))
                graph[i][j] -= 2
                
    # print("previous_cloud_pos")
    # print_cloud(cloud_pos)
    # print("new_cloud_pos")
    # print_cloud(new_cloud_pos)                
    return new_cloud_pos
            

def remove_cloud(cloud_pos):
    cloud_pos = []
    
    return cloud_pos

def print_graph(graph):
    print("graph")
    for g in graph:
        print(g)

def print_steps(steps):
    print("steps")
    for s in steps:
        print(s)
        
def print_cloud(cloud):
    print("cloud_pos")
    for c in cloud:
        print(c)

        
def main():
    graph, steps, cloud_pos = get_input()
    # print_graph(graph)
    # print_steps(steps)
    # print_cloud(cloud_pos)

    while steps:
        n = len(graph)
        # print("move_cloud")
        cloud_pos = move_cloud(cloud_pos, steps.popleft(), n)
        # print("fill_basket")
        graph = fill_basket(graph, cloud_pos)
        # print("duplicate_water")
        graph = duplicate_water(graph, cloud_pos)
        # print("generate_cloud")
        cloud_pos = generate_cloud(graph, cloud_pos)
    
    result = 0
    for i in range(n):
        for j in range(n):
            result += graph[i][j]
            
    print(result)
            
if __name__ == "__main__":
    main()
    
    
    
    