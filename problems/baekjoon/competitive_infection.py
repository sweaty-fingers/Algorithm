import heapq
import logging

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

simple_formatter = logging.Formatter("[%(name)s] %(message)s")
console_handler = logging.StreamHandler()
console_handler.setFormatter(simple_formatter)
console_handler.setLevel(logging.INFO)

root_logger = logging.getLogger()
root_logger.addHandler(console_handler)
root_logger.setLevel(logging.WARNING)



def get_input():
    N, K = map(int, input().split(" "))
    graph = [list(map(int, input().split(" "))) for _ in range(N)]
    s, y, x = map(int, input().split(" "))
    
    return graph, s, x, y, K


def bfs_with_heapq(graph, infection_group, s):
    h_q = []
    
    n = len(graph)
    m = len(graph[0])
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] in infection_group:
                heapq.heappush(h_q, (0, graph[i][j], i, j))
    
    while h_q:
        cur_t, infect, y, x = heapq.heappop(h_q)
        
        if cur_t == s:
            return graph
        
        for dy, dx in move:
            y_tmp, x_tmp = y + dy, x + dx
            
            if not ((0 <= y_tmp < n) and (0 <= x_tmp < m)):
                continue
            
            if graph[y_tmp][x_tmp] != 0:
                continue
            
            graph[y_tmp][x_tmp] = infect
            heapq.heappush(h_q, (cur_t + 1, infect, y_tmp, x_tmp))
    
    return graph
    
def main():
    graph, s, x, y, k = get_input()
    infection_group = [i + 1 for i in range(k)]
    
    root_logger.info(infection_group)
    root_logger.info("map_start")
    for g in graph:
        root_logger.info(g)
    
    graph = bfs_with_heapq(graph, infection_group, s)
    
    root_logger.info(f"map_at_time: {s}")
    
    for g in graph:
        root_logger.info(g)
    
    print(graph[y - 1][x - 1])


if __name__ == "__main__":
    main()
    