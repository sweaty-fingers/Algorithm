from collections import deque

move = [(-1, 0), (0, -1), (1, 0), (0, 1)] # 상 좌 하 우

def get_input():
    n = int(input())
    
    graph = [list(map(int, input().split(" "))) for _ in range(n)]
    
    return graph


def bfs(graph):

    n = len(graph)

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 9:
                y, x = i, j
    
    
    graph[y][x] = 0
    size_shark = 2
    num_ate = 0
    t = 0
    q = deque([(y, x, t)])
    
    if not check_fish(graph, size_shark):
        return t
    
    while q:
        y, x, t_tmp = q.popleft()
    
        if 0 < graph[y][x] < size_shark:
            graph[y][x] = 0
            num_ate += 1
            t += t_tmp
            q = deque([(y, x, 0)])
            
            # for g in graph:
            #     print(g)
            # print(f"t: {t}")
            
            
            # print(f"num_ate: {num_ate}")
            # print(f"size: {size_shark}")
            if num_ate >= size_shark:
                size_shark += 1
                num_ate = 0
            #     print("size_up")
            #     print(f"size: {size_shark}")
            
            # print("-" * 30)
            # print("")
            if not check_fish(graph, size_shark):
                return t
            
            continue
                
        for dy, dx in move:
            y_tmp, x_tmp = y + dy, x + dx
            
            if not ((0 <= y_tmp < n) and (0 <= x_tmp < n)):
                continue
            
            if graph[y_tmp][x_tmp] > size_shark:
                continue
            
            q.append((y_tmp, x_tmp, t_tmp + 1))
            
    return t

def check_fish(graph, size_shark):
    n = len(graph)
    
    for i in range(n):
        for j in range(n):
            if 0 < graph[i][j] < size_shark:
                return True
            
    return False
            
            
def main():
    graph = get_input()
    t = bfs(graph)
    print(t)
        

if __name__ == "__main__":
    main()