MOVE = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

N = 0
K = 0

def get_input():
    global N, K
    n, m, k = map(int, input().split(" "))
    N, K = n, k
    
    fireballs = []
    for _ in range(m):
        fireballs.append(tuple(map(int, input().split(" "))))
    
    return fireballs

        
def make_graph(i=0):
    
    if i == -1:
        return [[[] for _ in range(N)] for _ in range(N)]
    else:
        return [[0] * N for _ in range(N)]


def print_graph(graph):
    for g in graph:
        print(g)

def move_and_merge_fireballs(fireballs):
    """
    fireballs
    r, c, m, s, d : 행, 렬, 질량, 속도, 방향
    """
    
    m_graph = make_graph()
    s_graph = make_graph()
    d_graph = make_graph(-1)
    
    # print("m_graph")
    # print_graph(m_graph)
    # print("s_graph")
    # print_graph(s_graph)
    # print("d_graph")
    # print_graph(d_graph)
    # input()
        
    fireballs_pos = []
    for f in fireballs:
        r, c, m, s, d = f
        
        y, x = r - 1, c - 1
        dy, dx = MOVE[d]
        
        y_tmp, x_tmp = (y + (dy * s)) % N, (x + (dx * s)) % N
        
        m_graph[y_tmp][x_tmp] += m
        s_graph[y_tmp][x_tmp] += s
        d_graph[y_tmp][x_tmp].append(d)
        
        
        if (y_tmp, x_tmp) not in fireballs_pos:
            fireballs_pos.append((y_tmp, x_tmp))
        
        # print("m_graph")
        # print_graph(m_graph)
        # print("s_graph")
        # print_graph(s_graph)
        # print("d_graph")
        # print_graph(d_graph)
        # print("fireballs_pos")
        # print(fireballs_pos)
        # input()
        

    return fireballs_pos, (m_graph, s_graph, d_graph)


def get_directions(directions):
    """
    directions: d_graph[y][x]
    """

    for i, d in enumerate(directions):
        if i == 0:
            is_ = d % 2
            continue
        
        if d % 2 != is_:
            return [1, 3, 5, 7]
        
    return [0, 2, 4, 6]
    

def split_fireballs(fireballs_pos, graphs):
    m_graph, s_graph, d_graph = graphs
    fireballs = []
    
    for y, x in fireballs_pos:
        
        if len(d_graph[y][x]) < 2:
            fireballs.append([y + 1, x + 1, m_graph[y][x], s_graph[y][x], d_graph[y][x][0]])
            continue
        
        m = m_graph[y][x] // 5
        
        if m <= 0:
            continue
        
        s = s_graph[y][x] // len(d_graph[y][x])
        directions = get_directions(d_graph[y][x])
        
        for d in directions:
            fireballs.append([y + 1, x + 1, m, s, d])
            
        # print("fireballs")
        # print(fireballs)
        # input()

    return fireballs

def main():
    fireballs = get_input()
    
    for _ in range(K):
        fireballs_pos, graphs = move_and_merge_fireballs(fireballs)
        fireballs = split_fireballs(fireballs_pos, graphs)
    
    result = 0
    for f in fireballs:
        r, c, m, s, d = f
        
        result += m
    
    print(result)

if __name__ == "__main__":
    main()
        
        