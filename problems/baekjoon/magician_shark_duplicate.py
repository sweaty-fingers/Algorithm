from asyncio.base_futures import _FINISHED
from copy import deepcopy
from collections import deque
from io import DEFAULT_BUFFER_SIZE

MOVE_FISH = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
MOVE_SHARK = [(-1, 0), (0, 1), (0, -1), (1, 0)]


fish_smells = []
ate_fishes = 0
shark = (0, 0)
ate_max = 0

def get_input():
    global shark
    
    m, s = map(int, input().split(" "))
    fishes = deque([])
    for _ in range(m):
        fishes.append(tuple(map(int, input().split(" "))))
    
    shark = tuple(map(int, input().split(" ")))

    return fishes, s


def move_fishes(fishes, smell_graph):
    """
    물고기 이동
    """
    
    graph = [[0] * 4 for _ in range(4)]
    n = len(graph)
    m = len(fishes)
    for i in range(m):
        y, x, d = fishes.popleft()
        y, x = y - 1, x - 1
        
        is_move = False
     
        for i in range(8):
            d = (d + i) % 8
            dy, dx = MOVE_FISH[d]
            y_tmp, x_tmp = y + dy, x + dx
            
            if not ((0 <= y_tmp < n) and  (0 <= x_tmp < n)):
                continue
            
            if  smell_graph[y_tmp][x_tmp] <= 0:
                continue
            
            if graph[y_tmp][x_tmp] >= 0:
                graph[y_tmp][x_tmp] += 1
                is_move = True
                break
            
        
        if is_move:
            graph[y_tmp][x_tmp] += 1
            fishes.append((y_tmp + 1, x_tmp + 1, d))
        else:
            graph[y][x] += 1
            fishes.append((y + 1, x + 1, d + 1))
                
                
    return graph, fishes        


def get_shark(graph, visited, shark_tmp, ate_fishes, num_move):
    global ate_max, shark, fish_smells
    
    y, x = shark_tmp[0] - 1, shark_tmp[1] - 1
    
    if num_move >= 3:
        if len(ate_fishes) > ate_max:
            shark = (y + 1, x + 1)
            ate_max = len(ate_fishes)
            fish_smells = ate_fishes
        
        return
    
    for dy, dx in MOVE_SHARK:
        y_tmp, x_tmp = y + dy, x + dx
        
        if not ((0 <= y_tmp < 4) and (0 <= x_tmp < 4)):
            continue
        
        if graph[y_tmp][x_tmp] >= 0:
            ate_fishes.append((y, x))
    
        visited[y_tmp][x_tmp] = True
        num_move += 1
        get_shark(graph, visited, (y_tmp + 1, x_tmp + 1), ate_fishes, num_move)
        num_move -= 1
        visited[y_tmp][x_tmp] = False
        if graph[y_tmp][x_tmp] >= 0:
            ate_fishes.pop()
        

def leave_smell(smell_graph):
    global fish_smells
    
    for i in range(4):
        for j in range(4):
            if smell_graph[i][j] < 0:
                smell_graph[i][j] += 1
    
    for i in range(len(fish_smells)):
        y, x = fish_smells[i][0] - 1, fish_smells[i][1] - 1
        smell_graph[y][x] = -2
    
    
    return smell_graph


def duplicate_fishes(fishes, du_fishes):
    
    for y, x, d in du_fishes:
        fishes.append((y, x, d))

    return fishes

def main():
    global ate_max, shark, fish_smells
    fishes, s = get_input()
    
    smell_graph = [[0] * 4 for _ in range(4)]

    y, x = shark[0] - 1, shark[1] - 1
    
    for i in range(s):
        # 복제를 위한 물고기 위치 기록
        du_fishes = deepcopy(fishes)
        graph, fishes = move_fishes(fishes, smell_graph)
        ate_max, fish_smells = 0, []
        visited = [[0] * 4 for _ in range(4)]
        visited[shark[0] - 1][shark[1] - 1] = True
        shark_prev = shark
        get_shark(graph, visited, (shark[0], shark[1]), [], 0)
        smell_graph = leave_smell(smell_graph)
    
        graph[shark[0] - 1][shark[1] - 1] = -1
        graph[shark_prev[0] - 1][shark_prev[1] - 1] = 0

        fishes = duplicate_fishes(fishes, du_fishes)

    print(len(fishes))


if __name__ == "__main__":
    main()