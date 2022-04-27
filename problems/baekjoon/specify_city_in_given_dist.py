from collections import deque
import logging

simple_formatter = logging.Formatter("[%(name)s] %(message)s")
console_handler = logging.StreamHandler()
console_handler.setFormatter(simple_formatter)
console_handler.setLevel(logging.INFO)

root_logger = logging.getLogger()
root_logger.addHandler(console_handler)
root_logger.setLevel(logging.WARNING)

parent_logger = logging.getLogger("parent")
parent_logger.setLevel(logging.WARNING)



def get_input():
    N, M, K, X = map(int, input().split(" "))
    
    graph = [[] for _ in range(N + 1)] 
    for _ in range(M):
        a, b = map(int, input().split(" "))
        graph[a].append(b)
    
    return graph, K, X

def bfs(graph, k, x):
    
    q = deque([(x, 0)])
    visited = set()
    results = []
    
    while q:
        cur, dist = q.popleft()
        if dist == k and cur != x:
            results.append(cur)
        elif dist > k:
            return results
        
        for to in graph[cur]:
            if to not in visited:
                q.append((to, dist + 1))
                visited.add(to)
    
    return results

def main():
    graph, k, x = get_input()
    #parent_logger.info(f"graph: {graph}, k: {k}, x: {x}")
    
    results = bfs(graph, k, x)
    
    if not results:
        print(-1)
    else:
        results.sort()
        for r in results:
            print(r)
        

if __name__ == "__main__":
    main()