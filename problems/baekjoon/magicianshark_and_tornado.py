MOVE = [(0, -1), (1, 0), (0, 1), (-1, 0)]
SPLIT_POS = [()]

def get_input():
    n = int(input())
    
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split(" "))))
    
    return graph


def print_graph(graph):
    print("graph")
    
    for g in graph:
        print(g)
    

def move_and_split_dust(graph):
    y, x = len(graph) // 2, len(graph) // 2
    
    d = 0
    n_change = 0
    n_move = 1
    result = 0
    j = 1
    while 1:
        dy, dx = MOVE[d]
        
        for i in range(n_move):
            y, x = y + dy, x + dx
            graph, dust_out = split_dust(graph, y, x, d)
            result += dust_out
            # print_graph(graph)
            # input()
            
            if (y, x) == (0, 0):
                break
        if (y, x) == (0, 0):
                break
        
        d = (d + 1) % 4
        n_change += 1
        
        if n_change % 2 == 0:
            n_move += 1

    return result
            
def split_dust(graph, y, x, d):
    
    dust_out = 0
    
    dy, dx = MOVE[d]
    total = graph[y][x]
    diffs = [(2 * dy, 2 * dx), (dy + dx, dx + dy), (dy - dx, dx - dy), (dx, dy), (-dx, -dy), (2 * dx, 2 * dy), (-2 * dx, -2 * dy), (-dy + dx, -dx + dy), (-dy - dx, -dx - dy), (dy, dx)]
    per = [0.05, 0.1, 0.1, 0.07, 0.07, 0.02, 0.02, 0.01, 0.01, -1]
    cum_dust = 0
    for p, di in zip(per, diffs):
        y_tmp, x_tmp = y + di[0], x + di[1]
        
        if p == -1:
            
            if not ((0 <= y_tmp < len(graph)) and (0 <= x_tmp < len(graph))):
                dust_out += (total - cum_dust)
            else:
                graph[y_tmp][x_tmp] += (total - cum_dust)
            continue    
        
        if not ((0 <= y_tmp < len(graph)) and (0 <= x_tmp < len(graph))):
            dust_tmp = int(total * p)
            dust_out += dust_tmp
            cum_dust += dust_tmp
            continue
                
        dust_tmp = int(total * p)
        graph[y_tmp][x_tmp] += dust_tmp
        cum_dust += dust_tmp

        # print_graph(graph)
        # input()
        
    # print_graph(graph)
    # input()
    
    return graph, dust_out


def main():
    graph = get_input()
    # print_graph(graph)
    
    print(move_and_split_dust(graph))
    

if __name__ == "__main__":
    main()