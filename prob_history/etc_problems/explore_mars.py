from collections import deque
move = [(1, 0), (0, 1), (-1, 0), (0, -1)] # 아래, 오른쪽

INF = 1e9

def get_input():
    num_t = int(input())
    graph_total = []

    for _ in range(num_t):
        n = int(input())
        graph = []
        for _ in range(n):
            graph.append(list(map(int, input().split(" "))))
        
        graph_total.append(graph)
    
    return num_t, graph_total

def get_minumum(num_t, graph_total):
    results = []

    for t in range(num_t):
        queue = deque([])
        graph = graph_total[t]
        n = len(graph)
        graph_tmp = [[INF] * n for _ in range(n)]
        queue.append((0, 0, graph[0][0]))

        while queue:
            y, x, dist = queue.popleft()
            graph_tmp[y][x] = dist

            for dy, dx in move:
                y_tmp, x_tmp = y + dy, x + dx

                if not ((0 <= y_tmp < n) and (0 <= x_tmp < n)):
                    continue
                
                
                dist_tmp = graph_tmp[y][x] + graph[y_tmp][x_tmp]
                if dist_tmp < graph_tmp[y_tmp][x_tmp]:
                    graph_tmp[y_tmp][x_tmp] = dist_tmp
                    queue.append((y_tmp, x_tmp, graph_tmp[y_tmp][x_tmp]))
    
        for _ in range(n):
            print(graph_tmp[_])
        
        results.append(graph_tmp[-1][-1])
            
    return results


def main():
    num_t, graph_total = get_input()

    print(get_minumum(num_t, graph_total))

if __name__ == "__main__":
    main()




    
        

