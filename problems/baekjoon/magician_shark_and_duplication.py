from copy import deepcopy

MOVE_FISH = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
MOVE_SHARK = [(-1, 0), (0, -1), (1, 0), (0, 1)]

new_shark = []


def get_input():
    m, s = map(int, input().split(" "))
    fishes = []
    for _ in range(m):
        fishes.append(list(map(int, input().split(" "))))
    
    shark = tuple(map(int, input().split(" ")))
    
    graph = [[[] for _ in range(4)] for _ in range(4)]
    
    for i, j, d in fishes:
        y, x = i - 1, j - 1
        graph[y][x].append(d)
        
    ys, xs = shark[0] - 1, shark[1] - 1
    graph[ys][xs].append(9) # 9 == shark
    
    return fishes, shark, graph, s


def move_fishes(graph):
    
    new_fishes = []
    graph_new = [[[] for _ in range(4)] for _ in range(4)]
    
    for y in range(4):
        for x in range(4):
            if not graph[y][x]:
                continue
            
            is_move = False
            for d in graph[y][x]:
                if d in [-2, -1, 9]:
                    continue
                d = d - 1
                d_prev = d
                for k in range(len(MOVE_FISH)):
                    d = (d_prev - k) % 8
                    dy, dx  = MOVE_FISH[d]
                    
                    y_tmp, x_tmp = y + dy, x + dx
                    if (y, x) == (0, 2):
                        print(y, x)
                        print(dy, dx)
                        print(y_tmp, x_tmp)
                    
                    if not ((0 <= y_tmp < 4) and (0 <= x_tmp < 4)):
                        continue
                    
                    if 9 in graph[y_tmp][x_tmp] or -2 in graph[y_tmp][x_tmp] or -1 in graph[y_tmp][x_tmp]:
                        graph_new[y_tmp][x_tmp] = graph[y_tmp][x_tmp][:]
                        continue
                    
                    graph_new[y_tmp][x_tmp].append(d + 1)
                    is_move = True
                    break
                
                if not is_move:
                    graph_new[y][x].append(d_prev + 1)
                    

    # for g in graph_new:
    #     print(g)
    
    # input()
    
    return graph_new


def move_and_eat(graph, n_ate, move_list, visited, shark, shark_track):
    """
    move_list: 상어의 움직임 순서
    """
    
    ys, xs = shark[0] - 1, shark[1] - 1
    
    if len(move_list) >= 3:
        # print(move_list)
        # print(n_ate)
        shark_track.append((move_list[:], n_ate)) # 리스트를 새로운 메모리에 복사로 넣어야 함
        # print(f"shark_track: {shark_track}")
        return
    
    for i in range(len(MOVE_SHARK)):
        
        dy, dx = MOVE_SHARK[i][0], MOVE_SHARK[i][1]
        y_tmp, x_tmp = ys + dy, xs + dx
        
        if not ((0 <= y_tmp < 4) and (0 <= x_tmp < 4)):
            continue
        
        if visited[y_tmp][x_tmp] == True:
            continue
        
        visited[y_tmp][x_tmp] = True
        if graph[y_tmp][x_tmp]:
            if -2 not in graph[y_tmp][x_tmp] and -1 not in graph[y_tmp][x_tmp]:
                n_ate += len(graph[y_tmp][x_tmp])
        move_list.append(i)
        
        move_and_eat(graph, n_ate, move_list, visited, (y_tmp + 1, x_tmp + 1), shark_track)
        move_list.pop()
        n_ate -= len(graph[y_tmp][x_tmp])
        visited[y_tmp][x_tmp] = False


def get_graph_after_shark(graph, move_list, shark):
    ys, xs = shark[0] - 1, shark[1] - 1
    graph[ys][xs] = []
    
    for i in range(4):
        for j in range(4):
            if -2 in graph[i][j] or -1 in graph[i][j]:
                graph[i][j].sort(reverse=True)
                graph[i][j][-1] += 1
                
                if graph[i][j][-1] == 0:
                    graph[i][j].pop()
                    
    
    print(move_list)
    for d in move_list:
        ys, xs = ys + MOVE_SHARK[d][0], xs + MOVE_SHARK[d][1]
        
        if graph[ys][xs]:
            if -2 not in graph[ys][xs] and -1 not in graph[ys][xs]:
                graph[ys][xs] = [-2]
            
                
    if -2 not in graph[ys][xs] and -1 not in graph[ys][xs]:
        graph[ys][xs] = [9]
    shark = (ys + 1, xs + 1)

    return graph, shark


def duplicate_fishes(graph, fishes):
    new_fishes = []
    for y, x, d in fishes:
        y, x = y - 1, x - 1
        graph[y][x].append(d)
        
    for i in range(4):
        for j in range(4):
            if not graph[i][j]:
                continue
            for d in graph[i][j]:
                new_fishes.append((i + 1, j + 1, d))
            

    return graph, new_fishes
    

def main():
    fishes, shark, graph, s = get_input()
    
    print("Start")
    for g in graph:
        print(g)
    
    print("")
    for _ in range(s):
        # 1. 복제를 위한 물고기 정보 기록
        ys, xs = shark[0] - 1, shark[1] - 1
        fishes_for_duplication = deepcopy(fishes)
        
        graph = move_fishes(graph)
        # graph[ys][xs].append(9)
        print("After fishes moved")
        for g in graph:
            print(g)
        print("")
        
        visited = [[False] * 4 for _ in range(4)]
        visited[ys][xs] = True
        shark_track = []
        move_and_eat(graph, 0, [], visited, shark, shark_track)
        # print(shark_track)
        shark_track = sorted(shark_track, key=lambda x: (-1 * x[-1], x[0]))
        print(shark_track)
        move_list = shark_track[0][0]
        graph, shark = get_graph_after_shark(graph, move_list, shark)
        shark_track = []
        
        print("After shark moved")
        for g in graph:
            print(g)
        print("")

        graph, fishes = duplicate_fishes(graph, fishes_for_duplication)
        
        print("After duplicate")
        for g in graph:
            print(g)
        input()
        # for g in graph:
        #     print(g)
    
    result = 0
    
    for i in range(4):
        for j in range(4):
            if graph[i][j]:
                for k in graph[i][j]:
                    if k in [-1, -2, 9]:
                        continue
                    result += 1
    print(result)
        
        
if __name__ == "__main__":
    main()
    
    
    
    