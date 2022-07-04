from collections import deque, defaultdict

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
move_for_fill = [3, 1, 2, 0]
count_explode = defaultdict(int)

def get_input():
    n, m = map(int, input().split(" "))
    
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split(" "))))
    
    directions = [[0] * n for _ in range(n)]
    directions[0][0] = 4
    q = deque([(0, 0)])
    d = 0
    
    while q:
        y, x = q.popleft()
        tmp = 0    
        while tmp < 4:
            dy, dx = move[move_for_fill[d]]
            y_tmp, x_tmp = y + dy, x + dx
            
            if not ((0 <= y_tmp < n) and (0 <= x_tmp < n)):
                d = (d + 1) % 4
                tmp += 1
                continue
            
            if directions[y_tmp][x_tmp] != 0:
                d = (d + 1) % 4
                tmp += 1
                continue
            
            directions[y_tmp][x_tmp] = move_for_fill[d] + 1
            q.append((y_tmp, x_tmp))
            break

    directions[(n // 2)][(n // 2)] = 4
    
    magics = deque([])
    for _ in range(m):
        magics.append(list(map(int, input().split(" "))))
        
    return graph, magics, directions


def do_magic(graph, magic, directions):
    
    p = (len(graph) // 2)
    print(p)
    print(graph[p][p])
    d, s = magic
    
    for i in range(1, s + 1):
        y_tmp, x_tmp = p + i * move[d - 1][0], p + i * move[d - 1][1]
        graph[y_tmp][x_tmp] = 0
    
    print("graph after magic~~")
    for g in graph:
        print(g)
    input()
        
    graph = move_beads(graph, directions)
    return graph


def do_explode(graph, directions):
    global count_explode
    
    p = (len(graph) // 2) + 1
    q = deque([(p, p)])
    beads_conti = []
    
    while q:
        y, x = q.popleft()
        d = directions[y][x]
        dy, dx = -1 * move[d - 1][0], -1 * move[d - 1][1]
        
        y_tmp, x_tmp = y + dy, x + dx
        
        if (not beads_conti or graph[beads_conti[-1][0]][beads_conti[-1][1]] == graph[y_tmp][x_tmp]) and graph[y_tmp][x_tmp] != 0:
            beads_conti.append((y_tmp, x_tmp))
        else:
            if len(beads_conti) >= 4:
                for y_b, x_b in beads_conti:
                    count_explode[graph[y_b][x_b]] += 1
                    graph[y_b][x_b] = 0
            
            beads_conti = []
            if graph[y_tmp][x_tmp] != 0:
                beads_conti.append((y_tmp, x_tmp))
        
        if not (y_tmp == 0 and x_tmp == 0):
            q.append((y_tmp, x_tmp))
    
    print("graph after expode")
    for g in graph:
        print(g)  
    input()
    
    graph = move_beads(graph, directions)
    
    return graph
    

def move_beads(graph, directions):
    p = (len(graph) // 2)
    
    q = deque([(p, p)])
    
    while q:
        y, x = q.popleft()
        d = directions[y][x]
        dy, dx = -1 * move[d - 1][0], -1 * move[d - 1][1]
        
        y_tmp, x_tmp = y + dy, x + dx
        
        if graph[y_tmp][x_tmp] == 0:
            graph = shift_one_step(graph, directions, y_tmp, x_tmp)
           
        if (y_tmp == 0 and x_tmp == 0):
            break
    
    return graph
    
    
def shift_one_step(graph,  directions, y, x):
    
    q = deque([(y, x)])
    while q:
        y, x = q.popleft()
        d = directions[y][x]
        dy, dx = -1 * move[d - 1][0], -1 * move[d - 1][1]
        y_tmp, x_tmp = y + dy, x + dx
        graph[y][x] = graph[y_tmp][x_tmp]
        print(f"y: {y} x: {x}")
        print(f"y_tmp: {y_tmp} x_tmp: {x_tmp}")
        
        if (y_tmp == 0 and x_tmp == 0):
            break
            
    print("after_one_shift")
    for g in graph:
        print(g)
    # input()
    return graph

    
def main():
    global count_explode
    graph, magics, directions = get_input()
    
    
    # print("graph")
    # for g in graph:
    #     print(g)
    
    print("directions")    
    for d in directions:
        print(d)
    
    # print("magic")
    # for m in magics:
    #     print(m)
        
    for m in magics:
        graph = do_magic(graph, m, directions)
        print("graph after filld ~magic")
        for g in graph:
            print(g)
    
        graph = do_explode(graph, directions)

        print("graph after explode filled")
        for g in graph:
            print(g)
        input()
        
    result = 0
    for i in range(1, len(count_explode) + 1):
        result += i * count_explode[i]

    print(result)
    
if __name__ == "__main__":
    main()
    


    
    