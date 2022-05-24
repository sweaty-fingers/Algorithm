import heapq

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
INF = 1e9
def get_input():
    n = int(input())
    
    graph = [[] for _ in range((n * n))]
    distance = [INF] * (n * n)
    for i in range(n):
        costs = list(map(int, input().split(" ")))
        for j, c in enumerate(costs):
            
            for di, dj in move:
                i_tmp, j_tmp = i + di, j + dj
                
                if not ((0 <= i_tmp <n) and (0 <= j_tmp <n)):
                    continue
                
                graph[i * n + j].append((i_tmp * n + j_tmp, c))
    
    return graph, distance


def dijkstra(graph, distance, start=0):
    
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, node = heapq.heappop(q)
        
        if dist > distance[node]:
            continue
        
        for g in graph[node]:
            cost = dist + g[1]
            
            if cost < distance[g[0]]:
                distance[g[0]] = cost
                heapq.heappush(q, (cost, g[0]))
    
    return distance[-1] + graph[-1][-1][-1]

def main():
    r = int(input())
    results = []
    for _ in range(r):
        graph, distance = get_input()
        results.append(dijkstra(graph, distance))
    

    for r in results:
        print(r)
    
if __name__ == "__main__":
    main()
    
    
# input
# 3
# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5
# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4
            
        
        